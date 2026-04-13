import json
import pandas as pd
'''
Функция парсит json файл дл депозитов
- загружает файл .json
- вытаскивает оттуда два датафрейма - данные и обозначения
- схлопывает и записывает в отдельный файл
'''
def parse_deposit_to_csv(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    data = json.loads(data)
    df = pd.DataFrame(data['RawData'])
    df1 = pd.DataFrame(data['headerData'])

    df_merged = df.merge(df1, left_on='element_id', right_on='id')
    df_merged = df_merged[['obs_val', 'dt', 'elname']]
    df_merged.rename(columns = {'obs_val': 'Значение',
                                'dt': 'Период',
                                'elname': 'Вид депозита'}, inplace = True)
    df_merged.to_csv(path[:-4] + 'csv', encoding='utf8', index = False)
    return 'Json преобразован в файл .csv: ' + path[:-4] + 'csv'


#parse_deposit_to_csv()
