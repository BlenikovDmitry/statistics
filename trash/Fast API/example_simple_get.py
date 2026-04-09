from fastapi import FastAPI, Response, Path
from fastapi.responses import HTMLResponse, PlainTextResponse, FileResponse

# как запустить веб  сервер
# fastapi dev example_simple_get.py


app = FastAPI()
#создает ендпоинт по умолчанию - может быть главная страница
#отдаем json
@app.get('/')
def root():
    html_content = '''<h1> Адреса endpoints </h1>

                    <h2> /hello : по запросу к ресурсу отдаем html </h2>
                    <h2> /text : запросу отдает простой текст </h2>
                    <h2> /text1 : будто бы то же самое, что и text, но вернет он тут Json по умолчанию </h2>
                    <h2> /text2 : здесь явно указываем, что отдаем текст </h2>
                    <h2> /cb.csv : отдача файла с сервера </h2>
                    <h2> /path_params/{id_} : get запрос с 1 числовым параметром </h2>
                    <h2> /path_params_text/{id_}/{text} : get запрос с 1 числовым и 1 текстовым параметром </h2>
                    <h2> /path_params_adv/{text} : get запрос с параметрами, возвращает текстовый параметh, есть встроенная валидация на длину не менее 3 и не более 20 символов </h2>
                    <h2> /path_params_adv_id/{id_} : get запрос с параметрами, возвращает числовой параметр есть встроенная валидация на длину больше или равно 0 </h2>
                    '''
    return HTMLResponse(content=html_content)
    return {'message':'Hello World!'}
#создаем ресурс hello и по запросу к ресурсу отдаем html
#то есть объект класса HTMLResponse, куда пишется переменная html_content
@app.get('/hello')
def hello_html():
    html_content = '<h1> Hello World </h1>'
    return HTMLResponse(content=html_content)
#создаем ресурс text и по запросу отдает простой текст
#фишка в том, что мы используем родительский класс Response и прямо указываем
#что это простой текст
@app.get('/text')
def get_text():
    data = 'Hello World Simple Text!'
    return Response(content=data, media_type = 'text/plain')
#будто бы то же самое, что и text, но вернет он тут Json по умолчанию
@app.get('/text1')
def get_text():
    data = 'Hello World Simple Text!'
    return data
#а здесб явно указываем, что отдаем текст, поэтому все выводится корректно
@app.get('/text2', response_class = PlainTextResponse)
def get_text():
    data = 'Hello World Simple Text!'
    return data
#отдача файла с сервера
#но есть нюанс - имя файла будет как указано в названии ендпоинта
@app.get('/cb.csv')
def get_some_file():
    return FileResponse(
        path='cb.csv', 
        filename='cb.csv', 
        media_type='text/csv'  # Явно указываем тип файла
    )
#get запрос с параметрами, возвращает числовой параметр,
#есть встроенная валидация
@app.get('/path_params/{id_}')
def path_params(id_: int):
    return {'id':id_}
#get запрос с параметрами, возвращает числовой параметр и текстовый
#есть встроенная валидация
@app.get('/path_params_text/{id_}/{text}')
def path_params(id_: int, text: str):
    return {'id':id_, 'text': text}
#get запрос с параметрами, возвращает текстовый параметр
#есть встроенная валидация на длину не менее 3 и не более 20 символов
#все благодаря классу Path
@app.get('/path_params_adv/{text}')
def path_params(text: str = Path(min_length = 3, msx_length = 20)):
    return {'text': text}
#get запрос с параметрами, возвращает числовой параметр
#есть встроенная валидация на длину больше или равно 0
@app.get('/path_params_adv_id/{id_}')
def path_params(id_: int = Path(ge = 0)):
    return {'text': id_}
