from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()
'''
пример простого post запроса
>curl -X POST http://127.0.0.1:8000/simple_post -H "Content-Type: application/json" -d "{\"param1\": \"val1\", \"param2\": \"val2\"}"
вот так передавать через post запрос к ресурсу simple_post
'''
class Param(BaseModel):
    param1: str
    param2: str

@app.post('/simple_post')
def hello(data: Param):
    return {'message': f'Hello {data.param1} + {data.param2}'}
