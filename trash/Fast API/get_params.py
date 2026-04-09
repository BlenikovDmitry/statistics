from fastapi import FastAPI, Query

app = FastAPI()
#вызывать, например http://127.0.0.1:8000/user?uid=12&name=bob
@app.get('/user')
async def get_user(uid,name):
    return {'user_name': name, 'id': uid}

#можно проставлять значения по умолчанию, тогда можно вызывать без параметров
#он тогда подставит значения по умолчанию
@app.get('/users')
async def get_user(uid = 12,name = 'Bob'):
    return {'user_name': name, 'uid': uid}
#валидация с помощью класса Query
#отличается от Path тем, что берет данные из параметров(функции), а не из запроса(декоратор)
@app.get('/validation')
async def validation_user(name: str = Query(default = 'Bobby',min_length=3, max_length=20)):
    return {'name': name}
