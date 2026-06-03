import streamlit as st
import pandas as pd
from check_normal import prepare_data_field
from check_normal import statistic
from check_normal import qqplot
from check_normal import check_outliers
from check_normal import count_sigmas
from check_normal import hill_graphic_check
from check_normal import hill_method
from check_normal import scatter

st.header('Проверка нормального распределения')

upload = st.file_uploader('Выберите файл')

if upload:
    df = pd.read_csv(upload, encoding='windows-1251')
    prepare_data_field(df, 'Значение')
    st.write(df)
    st.subheader('Статистики')
    mean, median, desc = statistic(df, 'Значение')
    st.write(f'Среднее: {round(mean,2)}')
    st.write(f'Медиана: {median:.2f}')
    st.subheader('Быстрый анализ')
    st.write(desc)

    choose = st.radio('Выберите метод:',
                      ['Сравнение с эталоном', 'z-статистики',
                      'Подсчет сигм',
                      'Оценка применимости метода Хилла',
                      'Метод Хилла',
                      'Диаграмма рассеяния',
                       'Коэффициент асимметрии',
                       'Коэффициент эксцесса'])
    if choose == 'Сравнение с эталоном':
        st.pyplot(qqplot(df, 'Значение'))
    if choose == 'z-статистики':
        st.write('% точек вне нормального диапазона лежит: ')
        st.write(round(check_outliers(df, 'Значение'),2))
    if choose == 'Подсчет сигм':
        count_sigmas(df, 'Значение')
    if choose == 'Оценка применимости метода Хилла':
        st.pyplot(hill_graphic_check(df, 'Изменение(%)'))
    if choose == 'Метод Хилла':
        number = st.number_input('Укажите опорный элемент',
                                 min_value = 1,
                                 max_value = df.shape[0], step = 1)
        if number:
            st.write(round(hill_method(df, 'Изменение(%)', int(number)),2))
    if choose == 'Диаграмма рассеяния':
        df_headers = df.columns
        options = st.multiselect("Выбери столбцы:", (df_headers), max_selections=2,
                                 default = [df_headers[0], df_headers[1]])
        if len(options) > 1:
            st.pyplot(scatter(df, options[0], df, options[1]))
    if choose == 'Коэффициент асимметрии':
        st.write('Коэффициент асимметрии:')
        st.write(round(df['Значение'].skew(),2))
    if choose == 'Коэффициент эксцесса':
        st.write('Коэффициент эксцесса:')
        st.write(round(df['Значение'].kurt(),2))
        
        

        
