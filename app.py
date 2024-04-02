from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain.vectorstores import Pinecone
import pinecone
import psycopg2
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import os
from datetime import datetime,timezone

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

USERNAME = os.environ.get('NEON_USERNAME')
PASSWORD = os.environ.get('NEON_PASSWORD')
HOST = os.environ.get('NEON_HOST')
PORT = os.environ.get('NEON_PORT')
PROJECT = os.environ.get('NEON_PROJECT')

conn_str = f"dbname={PROJECT} user={USERNAME} password={PASSWORD} host={HOST} port={PORT} sslmode=require"

connection = psycopg2.connect(conn_str)

CREATE_CHAT_TABLE = (
    "CREATE TABLE IF NOT EXISTS chats (id SERIAL PRIMARY KEY, question TEXT, answer TEXT, date TEXT);"
)

INSERT_CHAT_RETURN_ID = "INSERT INTO chats (question,answer,date) VALUES (%s,%s,%s) RETURNING id;"

GET_CHAT = "SELECT * FROM chats;"

embeddings = download_hugging_face_embeddings()

#Initializing the Pinecone
pinecone.init(api_key=PINECONE_API_KEY,
              environment=PINECONE_API_ENV)

index_name="medical-chatbot"

#Loading the index
docsearch=Pinecone.from_existing_index(index_name, embeddings)


PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])

chain_type_kwargs={"prompt": PROMPT}

llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                  model_type="llama",
                  config={'max_new_tokens':512,
                          'temperature':0.8})


qa=RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs)

@app.get("/get")
def get_chat():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_CHAT)
            chat_data = cursor.fetchall()
    return chat_data
chat_data = get_chat()

@app.route("/")
def index():
    return render_template('chat.html',data = chat_data)


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    create_chat(input,result["result"])
    return str(result["result"])

def create_chat(qus,ans):
    question = qus
    answer = ans

    now = datetime.now(timezone.utc)
    day = now.day
    month = now.month
    year = now.year
    hour = now.hour
    minute = now.minute
    date = f"{day:02d}/{month:02d}/{year-2000:02d} {hour:02d}:{minute:02d}"

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_CHAT_TABLE)
            cursor.execute(INSERT_CHAT_RETURN_ID, (question,answer,date))
            chat_id = cursor.fetchone()[0]
    return {"id": chat_id, "message": f"chat {question,answer} created in neon DB."}, 201

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)