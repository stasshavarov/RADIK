import csv

aver_salary = 0
items = list()

with open('text_4_var_14', newline='\n', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        item = {
            'number': int(row[0]),
            'name': row[2] + ' ' + row[1],
            'age': int(row[3]),
            'salary': int(row[4][0:-1])
        }
        
        aver_salary += item['salary']
        items.append(item)
        
aver_salary /= len(items)

filtered = list()
for item in items:
    if (item['salary'] > aver_salary) and item['age'] > 39:
        filtered.append(item)
        
filtered = sorted(filtered, key=lambda x: x['number'])

with open('text_4_otvet_var_14', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for item in filtered:
        writer.writerow(item.values())
    