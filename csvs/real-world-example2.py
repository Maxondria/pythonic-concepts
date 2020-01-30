# Method 2 - Using DictReader
import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    # csv_data is actually a generator object, we use next to read values
    # The first line is not included as it's considered a header when using DictReader()
    # we just skip the first description line
    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f'{line["FirstName"]} {line["LastName"]}')

html_output += f'<p>There are currently {len(names)} public contributors. Thank you!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)
