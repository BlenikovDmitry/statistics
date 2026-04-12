from fastapi import FastAPI
import requests

'''
ендпоинты для получения данных с сайта ЦБ РФ
'''

app = FastAPI()
#https://www.cbr.ru/dataservice/data?y1=2026&y2=2026&publicationId=18&datasetId=37&measureId=2
#1) Средневзвешенные процентные ставки по привлеченным кредитными организациями вкладам (депозитам) физических лиц
@app.get('/deposit/{y1}/{y2}')
def export_deposit_interest(y1:int, y2:int):
    return { requests.get(f'https://www.cbr.ru/dataservice/data?y1={y1}&y2={y2}&publicationId=18&datasetId=37&measureId=2').text }

#2) Средневзвешенная ставка по ипотечным жилищным кредитам, предоставленным физическим лицам-резидентам
#https://www.cbr.ru/dataservice/data?y1=2026&y2=2026&publicationId=14&datasetId=29&measureId=
@app.get('/mort/{y1}/{y2}')
def export_mortgage_interest(y1:int, y2:int):
    return { requests.get(f'https://www.cbr.ru/dataservice/data?y1={y1}&y2={y2}&publicationId=14&datasetId=29&measureId=').text }
    

#3) Средневзвешенные процентные ставки по кредитам, предоставленным кредитными организациями физическим лицам
#https://www.cbr.ru/dataservice/data?y1=2026&y2=2026&publicationId=14&datasetId=27&measureId=2
@app.get('/credit/{y1}/{y2}')
def export_credit_interest(y1:int, y2:int):
    return { requests.get(f'https://www.cbr.ru/dataservice/data?y1={y1}&y2={y2}&publicationId=14&datasetId=27&measureId=2').text }


#4) Задолженность по кредитам, предоставленным физическим лицам-резидентам
#https://www.cbr.ru/dataservice/data?y1=2026&y2=2026&publicationId=20&datasetId=42&measureId=22
@app.get('/credit_debt/{y1}/{y2}')
def export_credit_debt(y1:int, y2:int):
    return { requests.get(f'https://www.cbr.ru/dataservice/data?y1={y1}&y2={y2}&publicationId=20&datasetId=42&measureId=22').text }

#41) Просроченная задолженность по кредитам, предоставленным физическим лицам-резидентам
#https://www.cbr.ru/dataservice/data?y1=2026&y2=2026&publicationId=20&datasetId=43&measureId=22
@app.get('/credit_overdue_debt/{y1}/{y2}')
def export_credit_overdue_debt(y1:int,y2:int):
    return { requests.get(f'https://www.cbr.ru/dataservice/data?y1={y1}&y2={y2}&publicationId=20&datasetId=43&measureId=22').text }
