import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)  # takes a delimeter if it's not a comma

    # Skip headers (first_name, last_name, email)
    # next(csv_reader)

    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        # produces lists: ['first_name', 'last_name', 'email']['John', 'Doe', 'john-doe@bogusemail.com']...
        for line in csv_reader:
            #  first_name, last_name, email = line

            # write the new line in the new file separated by '-'
            csv_writer.writerow(line)
 