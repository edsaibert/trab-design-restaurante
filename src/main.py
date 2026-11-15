# main.py
from fastapi import FastAPI
from router import router

app = FastAPI()

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "API do Restaurante Universitário"}