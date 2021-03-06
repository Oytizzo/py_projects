import csv

field_names = ["Name", "Author", "Publisher", "Price", "Category"]

book_1 = ["Computer Programming Part 1", "Tamim Shahriar Subeen", "Onnorokom Prokashoni", "240.0", "Programming"]
book_2 = ["Computer Programming Part 2", "Tamim Shahriar Subeen", "Dimik Prokashoni", "250.0", "Programming"]
book_3 = ["Learn Programming with Python", "Tamim Shahriar Subeen", "Dimik Prokashoni", "200.0", "Programming"]

book_list = [book_1, book_2, book_3]

with open("csv/book_test_3.csv", "w", newline='') as csvf:
    csv_writer = csv.writer(csvf, delimiter=',', quotechar="\"", quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(field_names)
    csv_writer.writerows(book_list)
