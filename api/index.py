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
#         urlPost = "https://tn8wvrqqe5.execute-api.us-east-1.amazonaws.com/prod/alexa/1"

#         msg = {
#             "id": item.id,
#             "message": item.message,
#             "alexa": item.alexa
#         }

#         payload = json.dumps(msg)
#         headers = {
#         'x-api-key': 'iWE86lUsQY3hwNCwiNDIi4s6whrnRee27KbjVj8A',
#         'Content-Type': 'application/json'
#         }

#         response = requests.request("POST", urlPost, headers=headers, data=payload)
#         if id == 1:
#             #celular
#             url = "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=88e09717-19cb-43c8-aaf4-9d7a11adb91b&token=5b9ec73c-7e61-4326-912e-d17594073aaf&response=json"
#             headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
#             response = requests.request("GET", url, headers=headers)
#         elif id == 2:
#             #alexa
#             url = "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=f89bb1f5-cb88-4d49-b644-54c0b2f69d44&token=c73a4ad6-f560-4dda-aca5-4f16209a7f14&response=json"
#             headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
#             response = requests.request("GET", url, headers=headers)
#         elif id == 3:
#             # ipad
#             url = "https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=2de9458b-4423-4a96-91a0-fc96fe604744&token=4bc67e38-ceb5-4f88-a35a-a86f5f2d7c16&response=json"
#             headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
#             response = requests.request("GET", url, headers=headers)
#         return "Mensagem reproduzida com sucesso"
    


# @app.get("/list_alexas")
# def listarAlexas():
#     return Alexas.alexas_list

