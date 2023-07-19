from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4
import json
import uvicorn
import requests
import time

class Mensagem(BaseModel):
    id: Optional[str]
    message: str
    alexa: int

app = FastAPI()

origins = [
    "http://127.0.0.1:5500/public/index.html",
    "http://127.0.0.1:5500/public",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
dict = {}
banco: List[Mensagem] = []

@app.get("/mensagem")
def listar_mensagens():
    return banco

@app.post("/mensagem")
def criar_mensagem(mensagem : Mensagem):
    mensagem.id = str(uuid4())
    banco.append(mensagem)
    dict = mensagem

    return None

@app.get("/")
async def teste():
    return banco[-1]


# @app.post("/alexa_message")
# async def enviarDados(item: Item):
#         urlPost = " "

#         msg = {
#             "id": item.id,
#             "message": item.message,
#             "alexa": item.alexa
#         }

#         payload = json.dumps(msg)
#         headers = {
#         'x-api-key': ' ',
#         'Content-Type': 'application/json'
#         }

#         response = requests.request("POST", urlPost, headers=headers, data=payload)
#         if id == 1:
#             #celular
#             url = 
#             headers = 
#             response = requests.request("GET", url, headers=headers)
#         elif id == 2:
#             #alexa
#             url = 
#             headers = 
#             response = requests.request("GET", url, headers=headers)
#         elif id == 3:
#             # ipad
#             url = 
#             headers = 
#             response = requests.request("GET", url, headers=headers)
#         return "Mensagem reproduzida com sucesso"

