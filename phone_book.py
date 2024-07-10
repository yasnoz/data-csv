'''first_name,last_name,phone_number
John,Lennon,123
George,Harrisson,456
Ringo,Starr,789'''

import csv

with open('data/phone_book.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    next (csv_reader)
    for row in csv_reader:
          print(row[1:3])
          line_count += 1
