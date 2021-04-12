import csv

with open("C:\\Users\\Honey\\Desktop\\Book1.csv") as list_csv:
    print(list_csv.read())
    csv_reader = csv.reader(list_csv)
    print(csv_reader)
    line_count = 0
    for row in csv_reader:
        print(row)
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} {row[1]} was born in {row[2]}.')
            line_count += 1
with open("C:\\Users\\Honey\\Desktop\\Book1.csv",'a',newline='') as list_csv:
    csv_file=csv.writer(list_csv)
    csv_file.writerow(['maryam2','moeinian','july'])
    csv_file.writerow(['armin2','moeinian','august'])
    csv_file.writerow(['arman2','moeinian','june'])
with open("C:\\Users\\Honey\\Desktop\\Book1.csv") as list_csv:
    csv_file=csv.DictReader(list_csv)
    line_count = 0
    for row in csv_file:
        print(row)
        if line_count == 0:
            print(f'Column names are {", ".join(row.keys())}')
            line_count += 1
        else:
            print(f'\t{row["name"]} {row["family"]} was born in {row["month"]}.')
            line_count += 1
with open("new_csv.csv", 'w', newline='') as list_csv:
    csv_file = csv.DictWriter(list_csv, fieldnames=['name', 'family', 'month'])
    csv_file.writeheader()
    csv_file.writerow({'family': 'moeinian', 'name': 'maryam', 'month': 'july'})
    csv_file.writerow({'name': 'armin', 'family': 'moeinian', 'month': 'august'})
    csv_file.writerow({'name': 'arman', 'family': 'moeinian', 'month': 'june'})

import json
x={'name':'hanieh'}
print(json.dumps(x))