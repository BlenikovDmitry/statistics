import streamlit as st
import pandas as pd
from check_normal import prepare_data_field
from check_normal import statistic
from check_normal import qqplot
from check_normal import check_outliers
from check_normal import count_sigmas
from check_normal import hill_graphic_check
from check_normal import hill_method

st.header('Проверка нормального распределения')

upload = st.file_uploader('Выберите файл')

if upload:
    df = pd.read_csv(upload, encoding='windows-1251')
    prepare_data_field(df, 'Значение')
    st.write(df)
    st.subheader('Статистики')
    mean, median, desc = statistic(df, 'Значение')
    st.write(f'Среднее: {mean}')
    st.write(f'Медиана: {median}')
    st.subheader('Быстрый анализ')
    st.write(desc)

    choose = st.radio('Выберите метод:',
                      ['QQplot', 'z-статистики',
                      'Подсчет сигм',
                      'Оценка применимости метода Хилла',
                      'Метод Хилла',
                      'Диаграмма рассеяния'])
    if choose == 'QQplot':
        st.pyplot(qqplot(df, 'Значение'))
    if choose == 'z-статистики':
        st.write('% точек вне нормального диапазона лежит: ')
        st.write(check_outliers(df, 'Значение'))
    if choose == 'Подсчет сигм':
        count_sigmas(df, 'Значение')
    if choose == 'Оценка применимости метода Хилла':
        st.pyplot(hill_graphic_check(df, 'Изменение(%)'))
    if choose == 'Метод Хилла':
        number = st.number_input('Укажите опорный элемент',
                                 min_value = 1,
                                 max_value = df.shape[0], step = 1)
        if number:
            st.write(hill_method(df, 'Изменение(%)', int(number)))
        

        
