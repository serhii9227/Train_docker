from fastapi import FastAPI
from os import environ as env
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"details": "Hello, wo"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)



