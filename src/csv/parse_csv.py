import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # print(csv_reader)

    with open('new_names.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')

        for line in csv_reader:
            csv_writer.writerow(line)
