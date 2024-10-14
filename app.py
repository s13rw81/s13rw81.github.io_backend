from fastapi import FastAPI
from data.model_enums import Catagory
from data.pydantic_models import Message

app = FastAPI()

@app.get('/')
async def root():
    return {"message" : "Hello World!"}


@app.post('/contact')
async def contact(message: Message):
    return {'message' : message}


@app.post('/test')
async def contact(message: Message=None):
    if not message:
        message = Message(name='sourav', message='test github actions', datetime=datetime.now(), email='test@test.com', catagory=Catagory.JOB.value)
    return {'message' : message}