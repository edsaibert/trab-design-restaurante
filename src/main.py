# main.py
from fastapi import FastAPI
from src.router import router
from fastapi.responses import FileResponse

app = FastAPI()

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return FileResponse("templates/index.html")

@app.get("/pedido.html")
def pedido():
    return FileResponse("templates/pedido.html")
    
@app.get("/pedido.js")
def pedido_js():
    return FileResponse("templates/pedido.js")

@app.get("/pedido.css")
def pedido_css():
    return FileResponse("templates/pedido.css")

@app.get("/login.css")
def login_css():
    return FileResponse("templates/login.css")

@app.get("/login.js")
def login_js():
    return FileResponse("templates/login.js")