import sqlite3
import os

# Connect to the database
def create_connection():
    conn = sqlite3.connect('document_query.db')
    return conn

# Create tables
def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            content TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            query TEXT,
            response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Insert document
def insert_document(filename, content):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO documents (filename, content) VALUES (?, ?)', (filename, content))
    conn.commit()
    conn.close()

# Fetch documents
def fetch_documents():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM documents')
    rows = cursor.fetchall()
    conn.close()
    return rows

# Insert user query history
def insert_user_history(user_id, query, response):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_history (user_id, query, response) VALUES (?, ?, ?)', (user_id, query, response))
    conn.commit()
    conn.close()

# Fetch user history
def fetch_user_history(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT query, response, timestamp FROM user_history WHERE user_id = ?', (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows