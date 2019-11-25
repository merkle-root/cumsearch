import csv

print("Remember to delete the final 'END' entries before running this")

with open("raw_regular.csv") as in_file:
    with open("combined.csv", 'w') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if row[0] != "":
                writer.writerow(row)

with open("raw_premium.csv") as in_file:
    with open("combined.csv", 'a') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if row[0] != "":
                writer.writerow(row)
