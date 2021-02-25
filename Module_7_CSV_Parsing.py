# Calculate number of words and letters from previous Homeworks 5/6 output
# test file.
# Create two csv:
# word-count (all words are preprocessed in lowercase)
# letter, cout_all, count_uppercase, percentage (add header, spacecharacters
# are not included)
# CSVs should be recreated each time new record added.


import Module_6_Module_Files
import csv
import re
import collections


class CSVParsing:
    def __init__(self):
        self.text_input = str
        self.words = str
        self.letters = str
        self.count_all = {}
        self.count_uppercase = {}
        self.percentage = int

    def get_data_from_txt(self):
        f = open('module_5_homework_result.txt')
        self.text_input = f.read()
        return self.text_input

    def get_count_letters(self):

        self.count_all = collections.Counter(
                re.compile('[^A-Z]').sub('',
                                         self.get_data_from_txt().
                                         upper())).items()
        self.count_uppercase = collections.Counter(
            re.compile('[^A-Z]').sub('', str(self.text_input))).items()
        return self.count_all, self.count_uppercase

    def get_count_words(self):
        self.words = len(self.get_data_from_txt().lower().split())
        return self.words

    def create_word_count_csv(self):
        with open('word_count.csv', 'w') as csvfile:
            csvfile.write(f'{self.get_count_words()}')

    def create_letters_csv(self):
        with open('letter_count.csv', 'w', newline='') as csvfile:
            headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
            writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter=',')
            writer.writeheader()
            self.get_count_letters()
            dd = collections.defaultdict(list)
            for key in set(list(dict(self.count_uppercase).keys()) +
                           list(dict(self.count_all).keys())):
                if key in dict(self.count_all):
                    dd[key].append(dict(self.count_all)[key])
                if key in dict(self.count_uppercase):
                    dd[key].append(dict(self.count_uppercase)[key])
                else:
                    dd[key].append(0)
            for key, value in dict(dd).items():
                csvfile.write(f'{key},{value[0]},{value[1]},'
                              f'{round(value[1]/value[0]*100, 2)}\n')


if __name__ == "__main__":
    a = Module_6_Module_Files.Main()
    a.input_record_type()
