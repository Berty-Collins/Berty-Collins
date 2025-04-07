import csv

with open("test.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
