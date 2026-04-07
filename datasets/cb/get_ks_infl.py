import requests
import pandas as pd
import xml.etree.ElementTree as ET
import io

'''
Довольно старый код, мне его накидала нейросеть
Использует старую методу - soap
Нужно еще как - то получить данные по инфляции
'''
def get_key_rate(start_date, end_date):
    url = "https://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx"
    
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://w3.org" xmlns:xsd="http://w3.org" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <KeyRateXML xmlns="http://web.cbr.ru/">
          <fromDate>{start_date}</fromDate>
          <ToDate>{end_date}</ToDate>
        </KeyRateXML>
      </soap:Body>
    </soap:Envelope>"""
    
    headers = {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': 'http://web.cbr.ru/KeyRateXML'
    }
    
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        # Парсим весь XML
        root = ET.fromstring(response.text)
        
        # Данные лежат внутри секции diffgram, где теги уже без namespace
        # Используем .//KR для поиска всех вхождений ключевой ставки
        data = []
        for kr in root.findall(".//KR"):
            date = kr.find("DT").text.split('T')[0]
            rate = float(kr.find("Rate").text)
            data.append({"Дата": date, "Ставка": rate})
        
        df = pd.DataFrame(data)
        if not df.empty:
            df['Дата'] = pd.to_datetime(df['Дата'])
        return df
    
    print(f"Ошибка запроса: {response.status_code}")
    return None
