'''
функции для оценки выбросов
'''

'''
оценка выбросов метолом тьюки
'''
def outliers_iqr(data, field):
    x = data[field]
    q25 = x.quantile(0.25)
    q75 = x.quantile(0.75)
    irq = q75 - q25
    bondl = q25 - 1.5 * irq
    bondu = q75 + 1.5 * irq
    outliers = data[(x < bondl) | (x > bondu)]
    cleaned = data[(x >= bondl) & (x <= bondu)]
    return outliers, cleaned


'''
оценка выбросов метолом тьюки
дополнительно задаются границы смещения влево и вправо
'''
def outliers_iqr_mod(data, feature, left = 1.5, right = 1.5):
    x = data[feature]
    q25 = x.quantile(0.25)
    q75 = x.quantile(0.75)
    irq = q75 - q25
    bondl = q25 - left * irq
    bondu = q75 + right * irq
    outliers = data[(x < bondl) | (x > bondu)]
    cleaned = data[(x >= bondl) & (x <= bondu)]
    return outliers, cleaned
    
'''
оценка выбросов методом оценки значений, попавших вне 3-х сигм
'''
def outliers_z_score(data, feature, log_scale=False):
    if log_scale:
        x = np.log(data[feature]+1)
    else:
        x = data[feature]

    mean_ = x.mean()
    sigma = x.std()
    boundl = mean_ - 3 * sigma
    boundu = mean_ + 3 * sigma
    outliers = data[(x < boundl) | (x > boundu)]
    cleaned = data[(x >= boundl) & (x <= boundu)]
    return outliers, cleaned

'''
оценка выбросов методом оценки значений, попавших вне 3-х сигм
дополнительно задаются границы смещения 2 сигмы ,1 сигма и тд
'''
def outliers_z_score_mod(data, feature, log_scale=False, left = 3, right = 3):
    if log_scale:
        x = np.log(data[feature]+1)
    else:
        x = data[feature]

    mean_ = x.mean()
    sigma = x.std()
    boundl = mean_ - left * sigma
    boundu = mean_ + right * sigma
    outliers = data[(x < boundl) | (x > boundu)]
    cleaned = data[(x >= boundl) & (x <= boundu)]
    return outliers, cleaned
