import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # print(csv_reader)
    next(csv_reader)
    count = 0
    for line in csv_reader:
        print(line)
        count += 1
    print(count)
