import html_engine as eng

'''
Здесь прописываем генерацию страницы
'''

def init(arg):
    eng.init()
    eng.header()
    eng.print_p("Статистика за " + str(arg))
    eng.print_p("Муниципальные облигации:")
    eng.print_table_start()



def table(arg):
    eng.print_tr_start()
    for elem in arg:
        eng.print_td(str(elem))
    eng.print_tr_end()

def statistic_header():
    eng.print_table_end()
    eng.print_p("Показатели:")
    eng.print_table_start()

def statistic_body(data):
    eng.print_tr_start()
    eng.print_td("Средняя ставка купона")
    eng.print_td("Отклонение ставки купона")
    eng.print_td("Средняя доходность последней сделки")
    eng.print_td("Отклонение доходности последней сделки")
    eng.print_td("Средняя цена")
    eng.print_td("Отклонение цены")
    eng.print_td("Объем торгов в рублях")
    eng.print_tr_end()
    table(data)
    eng.print_table_end()
    
def graphics():
    eng.print_p("Цена:")
    eng.print_img("price_muni.png", "цена облигаций")
    eng.print_p("Купонная доходность:")
    eng.print_img("kupon_muni.png", "купонная доходность")
    eng.print_p("Доходность последней сделки:")
    eng.print_img("dohod_eff_muni.png", "доходность последней сделки")
    eng.print_p("Распределение купонной доходности по выпускам(%):")
    eng.print_img("interest_distribution_muni.png", "распределение доходности")

    eng.print_p("Отсортированные данные ")
    eng.print_p("Цена:")
    eng.print_img("price_muni_sorted.png", "цена облигаций")
    eng.print_p("Купонная доходность:")
    eng.print_img("kupon_muni_sorted.png", "купонная доходность")
    eng.print_p("График погашения:")
    eng.print_img("end_graphic_muni.png", "доходность последней сделки")
    eng.print_p("Ликвидность:")
    eng.print_img("volume_muni_sorted.png", "Ликвидность")
    eng.floor()
    
