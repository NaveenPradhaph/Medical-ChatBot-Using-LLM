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

1. **Clone the repository**:

    ```bash
    git clone https://github.com/NaveenPradhaph/D-Nexus
    cd medical-chatbot
    ```


3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
2. **Create a `.env` file**

4. **Set up environment variables:**

    ```bash
    PINECONE_API_KEY = "xxxxx-xxxx-xxxx"
    PINECONE_API_ENV = "xxxxx"

    NEON_USERNAME = "xxxx"
    NEON_PASSWORD = "xxxx"
    NEON_HOST = "xx-xxx-xxxxxx"
    NEON_PORT = "xxxx"
    NEON_PROJECT = "xxxx"
    ```

4. **Download the model from huggingface:**

    *Select the model according to the system requirements if the RAM is less than **16GB** it is advisable to select the lesser bit model such as 2-bit or 4-bit model*
    
    You can use this 
    [TheBloke/Llama-2-7B-GGML](https://huggingface.co/TheBloke/Llama-2-7B-GGML/tree/main)

    *save the model in the folder named **model***

5. **Data for the model:**

    *The data for the model are multiple pdf's that are store in the folder named **data***
    >Important note the pdf's must be editable not scanned pdf

    *run the following code to store the vectors in the Pinecone vector stores*

    ```bash
    python store_index.py
    ```

5. **Run the application:**

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
