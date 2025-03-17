import html_engine as eng

'''
Здесь прописываем генерацию страницы
'''
#заголовок страницы
def init(arg, file):
    eng.init(file)
    eng.header(file)
    eng.h1_report("Статистика ОФЗ за " + str(arg), file)
    eng.p_open(file)
    eng.href_download(file, "site/" + str(arg)+"ofz_cleared.csv", "Скачать список бумаг")
    eng.p_close(file)
    #eng.print_p("Статистика ОФЗ за " + str(arg), file)
    #eng.print_p("ОФЗ:", file)
    #eng.print_table_start(file)


#вывод таблицы на страницу(!не используется)
def table(arg, file):
    eng.print_tr_start(file)
    for elem in arg:
        eng.print_td(str(elem),file)
    eng.print_tr_end(file)
#заголовок таблицы общих показателей
def statistic_header(file):
    #eng.print_table_end(file)
    eng.print_p("Показатели:", file)
    eng.print_table_start(file)
#таблица общих показателей
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
#вывод графиков показателей    
def graphics(file, file_name):
    eng.print_p("Цена:", file)
    eng.p_open(file)
    eng.href_download(file, "site/" + file_name+"price_ofz.png", "Скачать")
    eng.print_img("site/" + file_name + "price_ofz.png", "цена облигаций", file)
    eng.p_close(file)
    eng.print_p("Купонная доходность:", file)
    eng.p_open(file)
    eng.href_download(file, "site/" + file_name+"kupon_ofz.png", "Скачать")
    eng.p_close(file)
    eng.print_img("site/" + file_name + "kupon_ofz.png", "купонная доходность", file)
    eng.print_p("Доходность последней сделки:", file)
    eng.p_open(file)
    eng.href_download(file, "site/" + file_name+"dohod_eff_ofz.png", "Скачать")
    eng.p_close(file)
    eng.print_img("site/" + file_name + "dohod_eff_ofz.png", "доходность последней сделки", file)
    eng.print_p("Распределение купонной доходности по выпускам(%):", file)
    eng.p_open(file)
    eng.href_download(file, "site/" + file_name+"interest_distribution_ofz.png", "Скачать")
    eng.p_close(file)
    eng.print_img("site/" + file_name + "interest_distribution_ofz.png", "распределение доходности", file)

    eng.print_p("Отсортированные данные ", file)
    eng.print_p("Цена:", file)
    eng.p_open(file)
    eng.href_download(file, "site/" + file_name+"price_ofz_sorted.png", "Скачать")
    eng.p_close(file)
    eng.print_img("site/" + file_name + "price_ofz_sorted.png", "цена облигаций", file)
    eng.print_p("Купонная доходность:", file)
    eng.p_open(file)
    eng.href_download(file, "site/" + file_name+"kupon_ofz_sorted.png", "Скачать")
    eng.p_close(file)
    eng.print_img("site/" + file_name + "kupon_ofz_sorted.png", "купонная доходность", file)
    eng.print_p("График погашения:", file)
    eng.p_open(file)
    eng.href_download(file, "site/" + file_name+"end_graphic_ofz.png", "Скачать")
    eng.p_close(file)
    eng.print_img("site/" + file_name + "end_graphic_ofz.png", "доходность последней сделки", file)
    eng.print_p("Доходность последней сделки:", file)
    eng.p_open(file)
    eng.href_download(file, "site/" + file_name+"dohod_eff_ofz_sorted.png", "Скачать")
    eng.p_close(file)
    eng.print_img("site/" + file_name + "dohod_eff_ofz_sorted.png", "доходность последней сделки", file)
    eng.print_p("Ликвидность:", file)
    eng.p_open(file)
    eng.href_download(file, "site/" + file_name+"volume_ofz_sorted.png", "Скачать")
    eng.p_close(file)
    eng.print_img("site/" + file_name + "volume_ofz_sorted.png", "Ликвидность", file)
    eng.floor(file)
    
    
