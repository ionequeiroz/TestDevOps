from fastapi import FastAPI

app = FastAPI()

# 127.0.0.1:8000/
@app.get("/")
async def root():
    return {"message": "Hello World"}

# 127.0.0.1:8000/test1
@app.get("/test1")
async def funcaotest():
    return {"test": "deu certo"}