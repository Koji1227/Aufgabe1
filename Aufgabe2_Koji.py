# Programmieren vertieft
# Aufgabe 2; 21.03.2024
# Name: Koji Okumura

import csv

def read_csv(file_name: str) -> list:
    '''read a csv and return a double list'''
    with open(file_name, 'r', encoding = 'utf-8') as f_r:
        reader = csv.reader(f_r)
        header = next(reader) # Skip the header
        data = [row for row in reader]
    return data

def filter_1(data: list, char: str) -> list:
    '''check if the name of a town contains a certain character'''
    result = []
    for row in data:
        result.append(bool(char in row[0].lower()))
    return result

def filter_2(data: list, min: int) -> list:
    '''check if the population is larger than a certain number'''
    result = []
    for row in data:
        result.append(bool(int(row[3]) > min))
    return result

def select(data: list, fil_1: list, fil_2: list) -> list:
    '''select rows that meet the two criteria'''
    selected_rows = []
    for counter, row in enumerate(data):
        if (fil_1[counter] == True) and (fil_2[counter] == True):
            selected_rows.append(row)
    return selected_rows

def sort(selected_rows: list, crt_1: int, crt_2: int) -> list:
    '''sort the rows according to the two criteria'''
    result = sorted(selected_rows, key = lambda x: (x[crt_1], x[crt_2]))
    return result

def write_csv(result: list, file_name: str):
    '''write the result to a csv file'''
    with open(file_name, 'w', encoding = 'utf-8') as f_w:
        writer = csv.writer(f_w)
        writer.writerow(['Stadt', 'Bezirk', 'Bundesland', 'Einwohner'])
        writer.writerows(result)

data = read_csv('cities.csv')
fil_1 = filter_1(data, 'a')
fil_2 = filter_2(data, 10000)
selected_rows = select(data, fil_1, fil_2)
result = sort(selected_rows, 2, 0)
write_csv(result, 'results.csv')

# Feedback:
# - The code works correctly and the output is correct.
# - if __name__ == '__main__': would be a good addition.
# - the name of the functions filter_1 and filter_2 could be more descriptive.
