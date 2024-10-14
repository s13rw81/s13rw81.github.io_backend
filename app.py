from fastapi import FastAPI
from data.pydantic_models import Message

app = FastAPI()

@app.get('/')
async def root():
    return {"message" : "Hello World!"}


@app.post('/contact')
async def contact(message: Message):
    return {'message' : message}