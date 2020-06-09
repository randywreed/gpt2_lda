#wikitext-103
import csv
with open("/home/randy/Downloads/wikitext-103/wiki.train.tokens") as csv_file:
    csv_reader =csv.reader(csv_file)
    for row in csv_reader:
        print(row)
        input("wait")