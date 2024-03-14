# Programmieren vertieft
# Aufgabe 1; 07.03.2024
# Name: Koji Okumura

import csv

result = []

## newline = '' does not make sense here
with open('cities.csv', 'r', encoding = 'utf-8', newline = '') as f_r:
    reader = csv.reader(f_r)
    header = next(reader) # Skip the header
    for row in reader:
        ## This would miss all Cities with 'A' as first letter
        ## Better: 'a' in row[0].lower()
        if ('a' in row[0]) and (int(row[3]) > 10000):
            result.append(row)

sorted_result = sorted(result, key = lambda x: (x[2], x[0]))

## newline = '' does not make sense here 
with open('results.csv', 'w', encoding = 'utf-8', newline = '') as f_w:
    writer = csv.writer(f_w)
    writer.writerow(['Stadt', 'Bezirk', 'Bundesland', 'Einwohner'])
    writer.writerows(sorted_result)
