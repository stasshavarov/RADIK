from bs4 import BeautifulSoup
import csv

items = list()

with open('text_5_var_14', encoding='utf-8') as file:
    lines = file.readlines()
    html = ''
    for line in lines:
        html += line
        
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all('tr')
    rows = rows[1:]
    for row in rows:
        cells = row.find_all('td')
        item = {
            'company': cells[0].text,
            'contact': cells[1].text,
            'country': cells[2].text,
            'price': cells[3].text,
            'item': cells[4].text
        }
        items.append(item)
        
with open('text_5_otvet_var_14', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for item in items:
        writer.writerow(item.values())