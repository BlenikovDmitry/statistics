import json
import pandas as pd
'''
Функция парсит json файл данных
- загружает файл .json
- вытаскивает оттуда два датафрейма - данные и обозначения
- схлопывает и записывает в отдельный файл
'''
def parse_to_csv(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    data = json.loads(data)
    df = pd.DataFrame(data['RawData'])
    df1 = pd.DataFrame(data['headerData'])

    df_merged = df.merge(df1, left_on='element_id', right_on='id')
    df_merged = df_merged[['obs_val', 'dt', 'elname']]
    df_merged.rename(columns = {'obs_val': 'Значение',
                                'dt': 'Период',
                                'elname': 'Вид'}, inplace = True)
    df_merged.to_csv(path[:-4] + 'csv', encoding='utf8', index = False)
    return 'Json преобразован в файл .csv: ' + path[:-4] + 'csv'

'''
Вспомогательная функция чтобы не было дублирования кода
сохраняет файл json если запрос успешен
'''
def write_raw_json(path, req):
    if req.status_code == 200:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(req.text, f,ensure_ascii=False, indent=4)
        return {'Данные загружены в файл json' }
    else:
        return req.status_code
