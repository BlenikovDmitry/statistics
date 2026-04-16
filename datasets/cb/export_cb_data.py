from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import requests
import pandas as pd
import json
from fastapi.responses import FileResponse
from parse_json import parse_to_csv, write_raw_json, create_graphic
import os
'''
ендпоинты для получения данных с сайта ЦБ РФ
'''

#нужно будет поменять 2026 на текущий год
def is_data_fetched(path, y1,y2):
    print(path)
    if os.path.exists(path) or y1 == 2026 or y2 == 2026:
        return True
    else:
        return False
    
    
app = FastAPI()
#https://www.cbr.ru/dataservice/data?y1=2026&y2=2026&publicationId=18&datasetId=37&measureId=2
#1) Средневзвешенные процентные ставки по привлеченным кредитными организациями вкладам (депозитам) физических лиц
@app.get('/deposit/{y1}/{y2}')
def export_deposit_interest(y1:int, y2:int):
    if not is_data_fetched(f'deposit/from_{y1}_to_{y2}.csv', y1,y2):
        req = requests.get(f'https://www.cbr.ru/dataservice/data?y1={y1}&y2={y2}&publicationId=18&datasetId=37&measureId=2')
        print(req.status_code)
        print( write_raw_json(f'deposit/from_{y1}_to_{y2}.json', req))
        print( parse_to_csv(f'deposit/from_{y1}_to_{y2}.json'))
        create_graphic(f'deposit/from_{y1}_to_{y2}.csv')
        #в будущем написать отдельную страницу
        return FileResponse('public/index.html')
    else:
        print('Данные уже есть! открываю локальную копию')
        create_graphic(f'deposit/from_{y1}_to_{y2}.csv')
        #в будущем написать отдельную страницу
        return FileResponse('public/index.html')
        

#2) Средневзвешенная ставка по ипотечным жилищным кредитам, предоставленным физическим лицам-резидентам
#https://www.cbr.ru/dataservice/data?y1=2026&y2=2026&publicationId=14&datasetId=29&measureId=
@app.get('/mort/{y1}/{y2}')
def export_mortgage_interest(y1:int, y2:int):
    if not is_data_fetched(f'mortgage/from_{y1}_to_{y2}.csv', y1,y2):
        req = requests.get(f'https://www.cbr.ru/dataservice/data?y1={y1}&y2={y2}&publicationId=14&datasetId=29&measureId=')
        print( write_raw_json(f'mortgage/from_{y1}_to_{y2}.json', req))
        print( parse_to_csv(f'mortgage/from_{y1}_to_{y2}.json'))
        create_graphic(f'mortgage/from_{y1}_to_{y2}.csv')
        #в будущем написать отдельную страницу
        return FileResponse('public/index.html')
    else:
        print('Данные уже есть! открываю локальную копию')
        create_graphic(f'mortgage/from_{y1}_to_{y2}.csv')
        #в будущем написать отдельную страницу
        return FileResponse('public/index.html')
        
    

#3) Средневзвешенные процентные ставки по кредитам, предоставленным кредитными организациями физическим лицам
#https://www.cbr.ru/dataservice/data?y1=2026&y2=2026&publicationId=14&datasetId=27&measureId=2
@app.get('/credit/{y1}/{y2}')
def export_credit_interest(y1:int, y2:int):
    if not is_data_fetched(f'credit/from_{y1}_to_{y2}.csv', y1,y2):
        req = requests.get(f'https://www.cbr.ru/dataservice/data?y1={y1}&y2={y2}&publicationId=14&datasetId=27&measureId=2')
        print (write_raw_json(f'credit/from_{y1}_to_{y2}.json', req))
        print( parse_to_csv(f'credit/from_{y1}_to_{y2}.json'))
        create_graphic(f'credit/from_{y1}_to_{y2}.csv')
        #в будущем написать отдельную страницу
        return FileResponse('public/index.html')
    else:
        print('Данные уже есть! открываю локальную копию')
        create_graphic(f'credit/from_{y1}_to_{y2}.csv')
        #в будущем написать отдельную страницу
        return FileResponse('public/index.html')
        


#4) Задолженность по кредитам, предоставленным физическим лицам-резидентам
#https://www.cbr.ru/dataservice/data?y1=2026&y2=2026&publicationId=20&datasetId=42&measureId=22
@app.get('/credit_debt/{y1}/{y2}')
def export_credit_debt(y1:int, y2:int):
    if not is_data_fetched(f'credit_debt/from_{y1}_to_{y2}.csv', y1,y2):
        req = requests.get(f'https://www.cbr.ru/dataservice/data?y1={y1}&y2={y2}&publicationId=20&datasetId=42&measureId=22')
        print( write_raw_json(f'credit_debt/from_{y1}_to_{y2}.json', req))
        print( parse_to_csv(f'credit_debt/from_{y1}_to_{y2}.json'))
        create_graphic(f'credit_debt/from_{y1}_to_{y2}.csv')
        #в будущем написать отдельную страницу
        return FileResponse('public/index.html')
    else:
        print('Данные уже есть! открываю локальную копию')
        create_graphic(f'credit_debt/from_{y1}_to_{y2}.csv')
        #в будущем написать отдельную страницу
        return FileResponse('public/index.html')
        

#41) Просроченная задолженность по кредитам, предоставленным физическим лицам-резидентам
#https://www.cbr.ru/dataservice/data?y1=2026&y2=2026&publicationId=20&datasetId=43&measureId=22
@app.get('/credit_overdue_debt/{y1}/{y2}')
def export_credit_overdue_debt(y1:int,y2:int):
    if not is_data_fetched(f'credit_overdue_debt/from_{y1}_to_{y2}.csv', y1,y2):
        req = requests.get(f'https://www.cbr.ru/dataservice/data?y1={y1}&y2={y2}&publicationId=20&datasetId=43&measureId=22')
        print( write_raw_json(f'credit_overdue_debt/from_{y1}_to_{y2}.json', req))
        print( parse_to_csv(f'credit_overdue_debt/from_{y1}_to_{y2}.json'))
        create_graphic(f'credit_overdue_debt/from_{y1}_to_{y2}.csv')
        #в будущем написать отдельную страницу
        return FileResponse('public/index.html')
    else:
        print('Данные уже есть! открываю локальную копию')
        create_graphic(f'credit_overdue_debt/from_{y1}_to_{y2}.csv')
        #в будущем написать отдельную страницу
        return FileResponse('public/index.html')
        

#установка главной страницы приложения
#потом переписать через явной енпоинт / и явную отдачу файла
#и впредь не смей монтировать каталоги с heml страницами
#монтируй только ресурсы(звуки, стили ,нюдсы и тд)
app.mount('/', StaticFiles(directory='public', html=True), name = 'static')
