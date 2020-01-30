# Method 1
import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    # csv_data is actually a generator object, so skip the first 2 lines
    next(csv_data)
    next(csv_data)

    for line in csv_data:
        firstname, lastname, *_ = line

        if firstname == 'No Reward':
            break
        names.append(f'{firstname} {lastname}')

html_output += f'<p>There are currently {len(names)} public contributors. Thank you!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)
