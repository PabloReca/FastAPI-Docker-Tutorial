from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!"}


@app.get("/suma/{n1}/{n2}")
async def say_hello(n1: int, n2: int):
    resultado = n1 + n2
    return {"message": f"resultado= {resultado}"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/test")
async def root():
    return {"message": "TEST"}
