from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def get():
    return {'msg': 'Hello world!!'}