'''
здесь функции генерации
ВАЖНО! Здесь только определяем функции генерации, сама генерация
в файле generator.py
'''

def init(file):
    with open(file, 'w', encoding='utf-8') as f:
        f.write(" ")
        
'''
код для генерации главной страницы отчета
'''
def header(file):
    with open(file, 'a', encoding='utf-8') as f:
        f.write('''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>Отчет</title>
  
   <style type="text/css">
   
   P { 
    font-size: 40px;
	font-weight: bold;
	text-align: center;
   }
   TD {
    padding: 3px; 
    border: 1px solid black; 
	}
	TABLE {
	text-align: center;
	margin: auto; 
	}
	
 
  </style> 
  
  
 </head>
 <body bgcolor="#FFFACD">''')

def init_main(file):
    with open(file, 'a', encoding='utf-8') as f:
        f.write('''<!doctype html>
<html>
  <head>
  
  <title> Анализ бондов</title>
  <meta charset = "UTF-8">
  
  <link rel="stylesheet" href="styles.css">


</head>
 <body bgcolor="#FFFACD">
 <h1> Статистика ОФЗ </h1>
 <div class = "common_block">''' + '\n')
    
def h2(file, arg):
    with open(file, 'a', encoding='utf-8') as f:
        f.write(''' <h2>Общие данные на ''' + arg + ''':</h2>''' + '\n'  + ''' <div class = "common_text">''' + '\n')

def report_block(file):
    with open(file, 'a', encoding='utf-8') as f:
        f.write(''' <div class = "report_block">
<h2> Отчеты по датам: </h2>
<div class = "report_text">''' + '\n')

def dinamic_block(file):
    with open(file, 'a', encoding='utf-8') as f:
        f.write(''' <div class = "dinamic_block">
<h1> Динамика: </h1>
<div class = "dinamic_text">''' + '\n')
        

def href(file, link, text):
    with open(file, 'a', encoding='utf-8') as f:
        f.write('''<a href= ''' + link + '''>''' + text + '''</a>''' + '\n')
    

def div_close(file):
    with open(file, 'a', encoding='utf-8') as f:
        f.write("</div>" + '\n')

def p_open(file):
    with open(file, 'a', encoding='utf-8') as f:
        f.write("<p>" + '\n')

def p_close(file):
    with open(file, 'a', encoding='utf-8') as f:
        f.write("</p>" + '\n')

def close_document(file):
    with open(file, 'a', encoding='utf-8') as f:
        f.write("</body>" + '\n')
        f.write("</html>" + '\n')
    
    
'''
///////////////////////////////////////////////////////////////////////////////////////////
'''
'''
Код для генерации страниц ежедневного отчета
'''

def floor(file):
    with open(file, 'a', encoding='utf-8') as f:
        f.write(''' </body>
                    </html>
''')


def print_p(arg, file):
    with open(file, 'a', encoding='utf-8') as f:
        f.write("<p>" + arg + "</p>" + '\n')
def print_table_start(file):
    with open(file, 'a', encoding='utf-8') as f:
        f.write("<table>" + '\n')
def print_table_end(file):
    with open(file, 'a', encoding='utf-8') as f:
        f.write("</table>" + '\n')

def print_tr_start(file):
    with open(file, 'a', encoding='utf-8') as f:
        f.write("<tr>" + '\n')
def print_tr_end(file):
    with open(file, 'a', encoding='utf-8') as f:
        f.write("</tr>" + '\n')

def print_td(arg, file):
    with open(file, 'a', encoding='utf-8') as f:
        f.write("<td>" + arg + "</td>" + '\n')
def print_img(arg, alt, file):
    with open(file, 'a', encoding='utf-8') as f:
        f.write('''<img src="''' + arg + '''" alt="''' + alt + '''"''' + ''' width="98%">''' + '\n')
    
'''
//////////////////////////////////////////////////////////////////////////////////////////////
'''
    
    

