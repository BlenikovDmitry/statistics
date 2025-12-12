'''
что нужно запомнить, но пока не запомнил =((
'''


'''
простая функция фильтрации series
df передается по ссылке
'''
def filt_series(series, filt, df):
    for index, value in series.items():
        if value > filt:
            df = df.drop(index)
    return df
