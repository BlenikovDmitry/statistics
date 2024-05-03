'''
здесь функции генерации
ВАЖНО! Здесь только определяем функции генерации, сама генерация
в файле generator.py
'''

def init():
    with open('example.html', 'w', encoding='utf-8') as f:
        f.write(" ")
    
def header():
    with open('example.html', 'a', encoding='utf-8') as f:
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
 <body>''')

def floor():
    with open('example.html', 'a', encoding='utf-8') as f:
        f.write(''' </body>
                    </html>
''')
    

def print_p(arg):
    with open('example.html', 'a', encoding='utf-8') as f:
        f.write("<p>" + arg + "</p>" + '\n')
def print_table_start():
    with open('example.html', 'a', encoding='utf-8') as f:
        f.write("<table>" + '\n')
def print_table_end():
    with open('example.html', 'a', encoding='utf-8') as f:
        f.write("</table>" + '\n')

def print_tr_start():
    with open('example.html', 'a', encoding='utf-8') as f:
        f.write("<tr>" + '\n')
def print_tr_end():
    with open('example.html', 'a', encoding='utf-8') as f:
        f.write("</tr>" + '\n')

def print_td(arg):
    with open('example.html', 'a', encoding='utf-8') as f:
        f.write("<td>" + arg + "</td>" + '\n')
def print_img(arg, alt):
    with open('example.html', 'a', encoding='utf-8') as f:
        f.write('''<img src="''' + arg + '''" alt="''' + alt + '''"''' + ''' width="98%">''' + '\n')
    
    
    
    


