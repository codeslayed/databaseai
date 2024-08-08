# utils.py
import pandas as pd

def format_chat_history(chat_history):
    df = pd.DataFrame(chat_history, columns=['Question', 'Answer', 'Timestamp'])
    return df.to_csv(index=False)