import os
import streamlit as st
from database import create_table, insert_document, fetch_documents, insert_user_history, fetch_user_history
from utils import process_document

# Initialize the database
create_table()

# Create the documents directory if it doesn't exist
if not os.path.exists("documents"):
    os.makedirs("documents")

# Streamlit UI
st.title("Document Querying Application")

# User ID input
user_id = st.text_input("Enter your User ID:")

# Upload documents
uploaded_files = st.file_uploader("Upload documents (.pdf, .docx, .txt)", type=['pdf', 'docx', 'txt'], accept_multiple_files=True)

if st.button("Upload", key="upload_button"):
    for uploaded_file in uploaded_files:
        file_path = os.path.join("documents", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Process and store the document content
        content = process_document(file_path)
        insert_document(uploaded_file.name, content)
        st.success(f"Uploaded and processed {uploaded_file.name}")

# Define the query input
query = st.text_input("Enter your query:")

# Querying documents
if st.button("Search", key="search_button"):
    if query:  # Check if the query is not empty
        documents = fetch_documents()
        responses = []
        for doc in documents:
            if query.lower() in doc[2].lower():  # Check if query is in document content
                responses.append(f"Found in {doc[1]}")
        
        if responses:
            response_text = "\n".join(responses)
            st.write("Results:")
            st.write(response_text)
            insert_user_history(user_id, query, response_text)
        else:
            st.write("No results found.")
    else:
        st.warning("Please enter a query before searching.")

# Display user history
if user_id:
    st.subheader("Your Query History")
    history = fetch_user_history(user_id)
    if history:
        for record in history:
            st.write(f"**Query:** {record[0]}")
            st.write(f"**Response:** {record[1]}")
            st.write(f"**Timestamp:** {record[2]}")
            st.write("---")
    else:
        st.write("No query history found.")

# Download chat history
if st.button("Download Chat History"):
    history = fetch_user_history(user_id)
    if history:
        with open(f"{user_id}_chat_history.txt", "w") as f:
            for record in history:
                f.write(f"Query: {record[0]}\nResponse: {record[1]}\nTimestamp: {record[2]}\n\n")
        st.success("Chat history downloaded.")
    else:
        st.warning("No chat history to download.")
        
if st.button("Upload"):
    for uploaded_file in uploaded_files:
        file_path = os.path.join("documents", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Process and store the document content
        content = process_document(file_path)
        insert_document(uploaded_file.name, content)
        st.success(f"Uploaded and processed {uploaded_file.name}")
        st.write(f"Content of {uploaded_file.name}: {content}")  # Debug message