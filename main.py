from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
import time

app = FastAPI()

# CORSの設定を追加
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",  # すべてのオリジンを許可する場合
    allow_credentials=True,
    allow_methods=["*"],  # すべてのHTTPメソッドを許可 (GET, POSTなど)
    allow_headers=["*"],  # すべてのHTTPヘッダーを許可
)

class CodeExecutionRequest(BaseModel):
    source_code: str
    language: str
    api_key: str
    longpoll: bool

@app.post("/run")
async def run_code(request: CodeExecutionRequest):
    api_url = "https://api.paiza.io/runners/create"
    try:
        response = requests.post(api_url, json=request.dict())
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/details/{job_id}")
async def get_job_details(job_id: str):
    api_url = f"https://api.paiza.io/runners/get_details"
    try:
        response = requests.get(api_url, params={"id": job_id, "api_key": "guest"})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))