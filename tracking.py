from bs4 import BeautifulSoup
import mechanize


mtrace = mechanize.Browser()
mtrace.set_handle_robots(False)

main_url = 'https://www.findandtrace.com/trace-mobile-number-location'
mtrace.open(main_url)
mtrace.select_form(name='trace')
mtrace['mobilenumber'] = ' '
response = mtrace.submit().read()

soup = BeautifulSoup(response, 'html.parser')
tbl = soup.find_all('table',class_='shop_table')

data = tbl[0].find('tfoot')
c=0
for i in data:
    c+=1
    if c in (1,4,6,8):
        continue
    th = i.find('th')
    td = i.find('td')
    print(th.text,td.text)

data = tbl[2].find('tfoot')
c=0
for i in data:
    c+= 1
    if c in (2,20,22,26):
        th = i.find('th')
        td = i.find('td')
        print(th.text, td.text)


