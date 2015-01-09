__author__ = 'Samiam'
"""
1.      The clip must be public (privacy == anybody)
2.      The clip must have over 10 likes and over 200 plays
3.      The clip title must be under 30 characters
"""
import csv

def generator(csvreader):
    """
    Returns a generator...
    """
    for line in csvreader:
        yield line

def parse_csv(g, valid, invalid):
    line = g.next()

def open_and_read(filename):
    try:
        with open(filename, "rU") as csvf:
            csvreader = csv.reader(csvf, delimiter=',')

            #created the file, now make valid and invalid files (these will overwrite previous files of the same name!
            valid = open("valid.csv", "w")
            invalid = open("invalid.csv", "w")
            g = generator(csvreader)
            fieldnames = g.next()

            valid_writer = csv.DictWriter(valid, fieldnames)
            invalid_writer = csv.DictWriter(invalid, fieldnames)
            valid_writer.writeheader()
            invalid_writer.writeheader()

            for line in g:
                asDict = dict(zip(fieldnames, line))

                if (len(asDict['title']) < 30) and (asDict['total_plays'] > 200) and (asDict['privacy'] == "anybody") and (asDict['total_likes'] > 10):
                    valid_writer.writerow(asDict)
                else :
                    invalid_writer.writerow(asDict)

    except (IOError, OSError):
        print("Error opening and or processing file")


open_and_read("clips.csv")