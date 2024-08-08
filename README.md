<h1>Document Querying Application</h1>

<p>Welcome to the Document Querying Application! This tool allows users to upload documents in various formats (.pdf, .docx, .txt), query the documents for relevant information, and maintain a history of user interactions. This project demonstrates the potential of AI in enhancing document management and retrieval.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#features">Features</a></li>
    <li><a href="#tech-stack">Tech Stack</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#key-learnings">Key Learnings</a></li>
    <li><a href="#project-showcase">Project Showcase</a></li>
</ul>

<h2 id="features">Features</h2>
<ul>
    <li>Upload documents in .pdf, .docx, and .txt formats</li>
    <li>Efficiently query documents for relevant information</li>
    <li>Maintain a history of user queries and responses</li>
    <li>Download chat history in readable formats</li>
</ul>

<h2 id="tech-stack">Tech Stack</h2>
<ul>
    <li>Streamlit for the frontend interface</li>
    <li>SQLite for secure data storage</li>
    <li>Python for backend processing</li>
    <li>PyPDF2 and python-docx for document handling</li>
</ul>

<h2 id="installation">Installation</h2>
<p>To run this project, you need to have Python installed on your machine. Follow these steps to set up the environment:</p>
<ol>
    <li>Clone the repository:</li>
    <pre><code>git clone [insert repository link]</code></pre>
    
    <li>Navigate to the project directory:</li>
    <pre><code>cd Document-Querying-Application</code></pre>
    
    <li>Create a <code>requirements.txt</code> file with the following content:</li>
    <pre><code>streamlit
PyPDF2
python-docx
cryptography</code></pre>
    
    <li>Install the required packages:</li>
    <pre><code>pip install -r requirements.txt</code></pre>
</ol>

<h2 id="usage">Usage</h2>
<p>To use the Document Querying Application, run the main Python script. You will be prompted to upload documents and enter queries:</p>
<pre><code>streamlit run app.py</code></pre>
<p>Follow the on-screen instructions to upload documents, query them, and view your query history.</p>

<h2 id="key-learnings">Key Learnings</h2>
<ul>
    <li>Integrating document handling libraries in Python</li>
    <li>Implementing secure database interactions</li>
    <li>Designing a user-friendly interface with Streamlit</li>
    <li>Managing user sessions and query history</li>
</ul>

<h2 id="project-showcase">Project Showcase</h2>
<p>You can view the full project on my GitHub: <a href="https://github.com/coodeslayed/dataabaseai">LINK</a></p>

</body>
</html>
