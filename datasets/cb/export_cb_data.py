from fastapi import FastAPI
import requests
import pandas as pd
from pandas import json_normalize
import json
from parse_json import parse_deposit_to_csv
'''
ендпоинты для получения данных с сайта ЦБ РФ
- распарсить json в dataframe:
+ deposit
- подумать над статистическими показателями
'''
#вспомогательная функция чтобы не было дублирования кода
#сохраняет файл json если запрос успешен
def write_raw_json(path, req):
    if req.status_code == 200:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(req.text, f,ensure_ascii=False, indent=4)
        return {'Данные загружены в файл json' }
    else:
        return req.status_code
    
app = FastAPI()
#https://www.cbr.ru/dataservice/data?y1=2026&y2=2026&publicationId=18&datasetId=37&measureId=2
#1) Средневзвешенные процентные ставки по привлеченным кредитными организациями вкладам (депозитам) физических лиц
@app.get('/deposit/{y1}/{y2}')
def export_deposit_interest(y1:int, y2:int):
    req = requests.get(f'https://www.cbr.ru/dataservice/data?y1={y1}&y2={y2}&publicationId=18&datasetId=37&measureId=2')
    print( write_raw_json(f'deposit/from_{y1}_to_{y2}.json', req))
    return { parse_deposit_to_csv(f'deposit/from_{y1}_to_{y2}.json')} 

#2) Средневзвешенная ставка по ипотечным жилищным кредитам, предоставленным физическим лицам-резидентам
#https://www.cbr.ru/dataservice/data?y1=2026&y2=2026&publicationId=14&datasetId=29&measureId=
@app.get('/mort/{y1}/{y2}')
def export_mortgage_interest(y1:int, y2:int):
    req = requests.get(f'https://www.cbr.ru/dataservice/data?y1={y1}&y2={y2}&publicationId=14&datasetId=29&measureId=')
    return write_raw_json(f'mortgage/from_{y1}_to_{y2}.json', req)
    

#3) Средневзвешенные процентные ставки по кредитам, предоставленным кредитными организациями физическим лицам
#https://www.cbr.ru/dataservice/data?y1=2026&y2=2026&publicationId=14&datasetId=27&measureId=2
@app.get('/credit/{y1}/{y2}')
def export_credit_interest(y1:int, y2:int):
    req = requests.get(f'https://www.cbr.ru/dataservice/data?y1={y1}&y2={y2}&publicationId=14&datasetId=27&measureId=2')
    return write_raw_json(f'credit/from_{y1}_to_{y2}.json', req)


#4) Задолженность по кредитам, предоставленным физическим лицам-резидентам
#https://www.cbr.ru/dataservice/data?y1=2026&y2=2026&publicationId=20&datasetId=42&measureId=22
@app.get('/credit_debt/{y1}/{y2}')
def export_credit_debt(y1:int, y2:int):
    req = requests.get(f'https://www.cbr.ru/dataservice/data?y1={y1}&y2={y2}&publicationId=20&datasetId=42&measureId=22')
    return write_raw_json(f'credit_debt/from_{y1}_to_{y2}.json', req)

#41) Просроченная задолженность по кредитам, предоставленным физическим лицам-резидентам
#https://www.cbr.ru/dataservice/data?y1=2026&y2=2026&publicationId=20&datasetId=43&measureId=22
@app.get('/credit_overdue_debt/{y1}/{y2}')
def export_credit_overdue_debt(y1:int,y2:int):
    req = requests.get(f'https://www.cbr.ru/dataservice/data?y1={y1}&y2={y2}&publicationId=20&datasetId=43&measureId=22')
    return write_raw_json(f'credit_overdue_debt/from_{y1}_to_{y2}.json', req)
