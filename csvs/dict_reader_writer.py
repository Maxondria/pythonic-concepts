import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names_dict_rw.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(
            new_file, delimiter='\t', fieldnames=fieldnames)

        # write header - fname, lname, email
        csv_writer.writeheader()

        # produces ordered dict objects with a list of tuples:
        for line in csv_reader:
            # print(line) produces
            #Eg. OrderedDict([('first_name', 'John'), ('last_name', 'Doe'), ('email', 'john-doe@bogusemail.com')])
            # literally: {'first_name', 'John', 'last_name', 'Doe','email', 'john-doe@bogusemail.com' }

            # we can access keys easily
            # print(line['first_name']) -> 'John'

            # we can write to the file now
            csv_writer.writerow(line)
