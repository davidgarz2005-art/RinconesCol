# main.py
from fastapi import FastAPI

# Crear la instancia de la aplicación
app = FastAPI(
    title="RinconesCol",
    description="APP WEB donde encontraras turismo y gastronomia ",
    version="1.0.0",
)

# Definir un endpoint
@app.get("/")
async def root():
    return {"message": "¡Bienvenido a nuestra web RinconesCol, disfruta tu experiencia en nuestra maravillosa Web!"}
