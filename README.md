# hallucination_score_demo
This is a simple demo project built with Django. It’s designed to test how people interact with large language model (LLM) answers and whether showing a hallucination score changes how much they trust the response.

**Features:**
1. A chat-style survey UI (looks like you’re talking to an AI)

2. Two modes: with hallucination scores or without

3. Options to either accept the AI’s answer or look it up

4. A simple scoring system to track decisions

5. Results stored for later analysis

**Tech Stack**
Backend: Django (Python), 
Frontend: Django Templates, 
Database: SQLite

**Getting Started**

1. Clone the repository
<pre> git clone https://github.com/rajathashree/hallucination_score_demo.git </pre>
2. Set up a virtual environment and install the requirements
<pre>python -m venv venv
source venv/bin/activate </pre>
3. Run migrations
<pre>python manage.py makemigrations
python manage.py migrate </pre>
4. Start the server
<pre> python manage.py runserver </pre>
5. Open http://127.0.0.1:8000/ in your browser




