__author__ = 'Samiam'

import csv

class Verifier:

    valid_fh = None
    invalid_fh = None
    g = None
    fieldnames = None
    valid_writer = None
    invalid_writer = None

    def __init__(self, filename, v_fname="valid.csv", inv_fname="invalid.csv"):
        try:
            csvf = open(filename, "rU")
            csvreader = csv.reader(csvf, delimiter=',')
            self.g = self.__create_generator(csvreader)
            self.__create_output_files(v_fname, inv_fname)

        except (IOError, OSError):
            print("Error opening and or processing file")

    def __create_generator(self, csvreader):
        """
        Returns a generator...
        """
        if csvreader == None:
            return
        for line in csvreader:
            yield line

    def __create_output_files(self, v_fname, inv_fname):

        #created the file, now make valid and invalid files (these will overwrite previous files of the same name!
        try:
            self.valid_fh = open(v_fname, "w")
            self.invalid_fh = open(inv_fname, "w")
        except (IOError, OSError):
            print("Error opening or creating valid and invalid output files")

    def __file_setup(self):
        self.fieldnames = self.g.next()
        self.valid_writer = csv.DictWriter(self.valid_fh, self.fieldnames)
        self.invalid_writer = csv.DictWriter(self.invalid_fh, self.fieldnames)
        self.valid_writer.writeheader()
        self.invalid_writer.writeheader()

    def __parse_file(self):
        for line in self.g:
            asDict = dict(zip(self.fieldnames, line))

            if (len(asDict['title']) < 30) and (asDict['total_plays'] > 200) and (asDict['privacy'] == "anybody") and (asDict['total_likes'] > 10):
                self.valid_writer.writerow(asDict)
            else :
                self.invalid_writer.writerow(asDict)

    def process_file(self):
        self.__file_setup()
        self.__parse_file()

    def finish(self):
        pass


myVF = Verifier("clips.csv", )
myVF.process_file()
# myVF = Verifier("clips.csv")
