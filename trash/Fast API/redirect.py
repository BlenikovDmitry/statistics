from fastapi import FastAPI
from fastapi.responses import RedirectResponse, PlainTextResponse

app = FastAPI()

#делаем редирект, если пользователь обращается к старой версии страницы
#то мы его перенаправляем на новую
@app.get('/old')
async def old():
    return RedirectResponse('/new', status_code = 302)

@app.get('/new')
async def new():
    return {'new':'new_page'}
