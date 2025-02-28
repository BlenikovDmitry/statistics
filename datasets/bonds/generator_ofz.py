import html_engine as eng

'''
Здесь прописываем генерацию страницы
'''

def init(arg, file):
    eng.init(file)
    eng.header(file)
    eng.print_p("Статистика за " + str(arg), file)
    eng.print_p("ОФЗ:", file)
    eng.print_table_start(file)



def table(arg, file):
    eng.print_tr_start(file)
    for elem in arg:
        eng.print_td(str(elem),file)
    eng.print_tr_end(file)

def statistic_header(file):
    eng.print_table_end(file)
    eng.print_p("Показатели:", file)
    eng.print_table_start(file)

def statistic_body(data, file):
    eng.print_tr_start(file)
    eng.print_td("Средняя ставка купона", file)
    eng.print_td("Отклонение ставки купона", file)
    eng.print_td("Средняя доходность последней сделки", file)
    eng.print_td("Отклонение доходности последней сделки", file)
    eng.print_td("Средняя цена", file)
    eng.print_td("Отклонение цены", file)
    eng.print_td("Объем торгов в рублях", file)
    eng.print_tr_end(file)
    table(data, file)
    eng.print_table_end(file)
    
def graphics(file, file_name):
    eng.print_p("Цена:", file)
    eng.print_img("site/" + file_name + "price_ofz.png", "цена облигаций", file)
    eng.print_p("Купонная доходность:", file)
    eng.print_img("site/" + file_name + "kupon_ofz.png", "купонная доходность", file)
    eng.print_p("Доходность последней сделки:", file)
    eng.print_img("site/" + file_name + "dohod_eff_ofz.png", "доходность последней сделки", file)
    eng.print_p("Распределение купонной доходности по выпускам(%):", file)
    eng.print_img("site/" + file_name + "interest_distribution_ofz.png", "распределение доходности", file)

    eng.print_p("Отсортированные данные ", file)
    eng.print_p("Цена:", file)
    eng.print_img("site/" + file_name + "price_ofz_sorted.png", "цена облигаций", file)
    eng.print_p("Купонная доходность:", file)
    eng.print_img("site/" + file_name + "kupon_ofz_sorted.png", "купонная доходность", file)
    eng.print_p("График погашения:", file)
    eng.print_img("site/" + file_name + "end_graphic_ofz.png", "доходность последней сделки", file)
    eng.print_p("Доходность последней сделки:", file)
    eng.print_img("site/" + file_name + "dohod_eff_ofz_sorted.png", "доходность последней сделки", file)
    eng.print_p("Ликвидность:", file)
    eng.print_img("site/" + file_name + "volume_ofz_sorted.png", "Ликвидность", file)
    eng.floor(file)
    
    
