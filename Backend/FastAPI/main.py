from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles

# https://fastapi.tiangolo.com/

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return "Hello FastAPI"


@app.get("/url")
async def url():
    return {"url": "https://github.com/s-bauza/hello-python"}

# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc
