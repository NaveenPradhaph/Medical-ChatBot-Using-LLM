# Medical Chatbot

This is a Flask-based medical chatbot application that leverages Hugging Face embeddings and Pinecone vector stores and Llama-2 7b model for question answering on medical topics. The chatbot allows users to interact in real-time and stores chat history in a PostgreSQL database.

## Features

- Real-time chat interface.
- Medical question answering leveraging Hugging Face embeddings and Pinecone vector stores.
- Persistent storage of chat history in a PostgreSQL database.

## Requirements

- Python 3.10.9
- Flask
- psycopg2
- Pinecone
- Hugging Face transformers
- dotenv

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/medical-chatbot.git
cd medical-chatbot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables:

```bash
PINECONE_API_KEY = "xxxxx-xxxx-xxxx"
PINECONE_API_ENV = "xxxxx"

NEON_USERNAME = "xxxx"
NEON_PASSWORD = "xxxx"
NEON_HOST = "xx-xxx-xxxxxx"
NEON_PORT = "xxxx"
NEON_PROJECT = "xxxx"
```

4. Run the application:

```bash
python app.py
```

## Usage

- Open your web browser and go to http://localhost:8080.
- Type your medical-related questions in the chatbox and hit Enter.
- Receive real-time responses from the chatbot.
- Chat history is stored in the PostgreSQL database and can be viewed on the web interface.

## API Endpoints

- /get: Retrieve chat history from the database.
- /chat: Send messages to the chatbot.
