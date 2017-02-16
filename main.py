import urllib.request
from bs4 import BeautifulSoup
import xlwt
from tempfile import TemporaryFile


url = "http://www.morganbrown.com/attorneys/index.php"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

sidebar = soup.find('div', {'id':'sidebar'})
ul = sidebar.find('ul')
l = []

#extract lawyer pages
for i in ul.find_all('li'):
    x = []
    x.append(i.find('a').text)
    x.append('http://www.morganbrown.com/attorneys/'+i.find('a').get('href'))

    #has 'labor' keyword
    x.append(0)
    #has 'bargaining' keywork
    x.append(0)

    l.append(x)

for index in l:
    page = urllib.request.urlopen(index[1])
    soup = BeautifulSoup(page, 'html.parser')
    main = soup.find('div', {'id':'main'})
    p = main.findAll('p')
    for j in p:
        if 'labor' in j.text.lower():
            index[2] = 1
        if 'bargaining' in j.text.lower():
            index[3] = 1

#print(l)


excel = xlwt.Workbook()
sheet1 = excel.add_sheet('sheet1')


sheet1.write(0, 0, 'Name')
sheet1.write(0, 1, 'URL')
sheet1.write(0, 2, 'Has "labor" keyword')
sheet1.write(0, 3, 'Has "bargaining" keyword')
for i in range(1, len(l)):
    for j in range(4):
       sheet1.write(i, j, l[i-1][j])

name = 'name.xls'
excel.save(name)
excel.save(TemporaryFile())




