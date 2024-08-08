import streamlit as st
from database import create_table, insert_chat, fetch_chat_history
from utils import format_chat_history

# Initialize the database
create_table()

# Streamlit application
st.title("Document Query Application")

# User input
user_id = st.text_input("Enter your User ID:")
question = st.text_area("Ask your question:")

if st.button("Submit"):
    # Here, you would integrate your document querying logic
    # For demonstration, we'll use a dummy answer
    answer = "This is a dummy answer to your question."

    # Store the chat in the database
    insert_chat(user_id, question, answer)
    st.success("Your question has been submitted!")

# Display chat history
if user_id:
    st.subheader("Chat History")
    chat_history = fetch_chat_history(user_id)
    if chat_history:
        for question, answer, timestamp in chat_history:
            st.write(f"**Q:** {question}")
            st.write(f"**A:** {answer}")
            st.write(f"**Timestamp:** {timestamp}")
            st.write("---")
    else:
        st.write("No chat history found.")

# Download chat history
if st.button("Download Chat History"):
    chat_history = fetch_chat_history(user_id)
    if chat_history:
        csv = format_chat_history(chat_history)
        st.download_button("Download CSV", csv, "chat_history.csv", "text/csv")
    else:
        st.warning("No chat history to download.")