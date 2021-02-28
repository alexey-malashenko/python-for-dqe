# ---------------------------------- PLEASE ----------------------------------

# ----------------------------------- NOTE -----------------------------------

# ----------------------------- FULL REFACTORING -----------------------------

# Homework:
#
# Expand previous Homework 5/6/7 with additional class, which allow to provide
# records by JSON file:
# Define your input format (one or many records)
# Default folder or user provided file path
# Remove file if it was successfully processed


# --------------------------  HOME WORK -------------------------------
import os
import json
import csv
import re
import collections
from time import gmtime, strftime, strptime
from datetime import datetime
from Module_4_Functions_Refactor_Module3 import normalize as norm


# some global variables
publication_type = ''
path_name = ''
text_from_file = []


# parent object (Inheritance). Have common attributes with News, Ad and Zen
class Publication:

    def __init__(self):
        self.name = str
        self.text = []
        self.decoration_line = '--------------------'
        self.delimited_line = '-----------------------------------------------'
        self.full_publication = ''


# child from Publication for News
class News(Publication):
    def __init__(self):
        Publication.__init__(self)
        self.city = []
        self.current_date = strftime('%d/%m/%Y %H:%M', gmtime())
        self.name = 'News'

    def get_full_publication(self, i):
        self.full_publication = f'{self.name} {self.decoration_line}\n' \
                                f'{self.text[i]}\n' \
                                f'{self.city[i]}, {str(self.current_date)}\n' \
                                f'{self.delimited_line}\n'


# child from Publication for Advertisement
class Ad(Publication):
    def __init__(self):
        Publication.__init__(self)
        self.expiration_date = []
        self.current_date = strftime('%d/%m/%Y', gmtime())
        self.days_left = []
        self.name = 'Private Ad'

    # expiration date should be date and correct
    def checking_expiration_date(self, expiration_date):
        x = 1
        while x > 0:
            try:
                expiration_date == strptime(expiration_date,
                                            '%d/%m/%Y')
            except ValueError:
                print('Invalid date!')
                expiration_date = input("Please enter correct "
                                        "expiration date DD/MM/YYYY: ")
            else:
                if strptime(expiration_date, '%d/%m/%Y') >= \
                        strptime(self.current_date, '%d/%m/%Y'):
                    expiration_date = str(expiration_date)
                    x = 0
                if strptime(expiration_date, '%d/%m/%Y') < \
                        strptime(self.current_date, '%d/%m/%Y'):
                    expiration_date = input("Please enter expiration date the "
                                            "biggest than current date "
                                            "DD/MM/YYYY: ")
        return expiration_date

    # get days left
    def get_days_left(self, expiration_date):
        last = datetime.strptime(expiration_date, '%d/%m/%Y')
        now = datetime.strptime(self.current_date, '%d/%m/%Y')
        days_left = (last - now).days
        return days_left

    def get_full_publication(self, i):
        self.full_publication = f'{self.name} {self.decoration_line}\n' \
                                f'{self.text[i]}\n' \
                                f'Actual until: {self.expiration_date[i]}, ' \
                                f'{str(self.days_left[i])} days left\n' \
                                f'{self.delimited_line}\n'


# child from Publication for my oun block
class ZenOfPython(Publication):
    def __init__(self):
        Publication.__init__(self)
        self.zen_dict = self.get_zen_dict()
        self.number_of_principle = []
        self.name = 'The Zen of Python'

    # get a dictionary with Zen principles. It could be public and it
    # could be called once, but I want to implement it as is
    def get_zen_dict(self):
        zen = """Beautiful is better than ugly.
        Explicit is better than implicit.
        Simple is better than complex.
        Complex is better than complicated.
        Flat is better than nested.
        Sparse is better than dense.
        Readability counts.
        Special cases aren't special enough to break the rules.
        Although practicality beats purity.
        Errors should never pass silently.
        Unless explicitly silenced.
        In the face of ambiguity, refuse the temptation to guess.
        There should be one-- and preferably only one --obvious way to do it.
        Although that way may not be obvious at first unless you're Dutch.
        Now is better than never.
        Although never is often better than *right* now.
        If the implementation is hard to explain, it's a bad idea.
        If the implementation is easy to explain, it may be a good idea.
        Namespaces are one honking great idea -- let's do more of those!"""
        self.zen_dict = dict()
        i = 1
        for principle in zen.split('\n'):
            self.zen_dict[principle.replace('    ', '')] = i
            i += 1
        return self.zen_dict

    # check principle
    def checking_principle(self, principle):
        x = 1
        while x > 0:
            if principle in self.zen_dict.keys():
                return principle
            else:
                principle = input('Please, insert correct principle: ')

    # get number of principle
    def get_principle_number(self, principle):
        principle_number = self.zen_dict.get(principle)
        return principle_number

    def get_full_publication(self, i):
        self.full_publication = f'{self.name} {self.decoration_line}\n' \
                                f'{self.text[i]}\n' \
                                f'Number of Zen is: ' \
                                f'{self.number_of_principle[i]}\n' \
                                f'{self.delimited_line}\n'


class InputParameters:
    def __init__(self):
        self.type_of_content = 0
        self.type_of_input = 0
        self.type_of_file = 0
        self.path_name = str

    def get_input_parameters(self):
        while self.type_of_content not in (1, 2, 3, 5):
            try:
                self.type_of_content = int(input("Please choose the type of "
                                                 "content:\n"
                                                 "1 - News\n"
                                                 "2 - Ad\n"
                                                 "3 - Guess The Zen of "
                                                 "Python\n"
                                                 "5 - For Exit\n"
                                                 "Please type here: "))
            except ValueError:
                print("Sorry, I didn't understand that. Only numbers "
                      "please")
            else:
                if self.type_of_content == 5:
                    exit()
                if self.type_of_content not in (1, 2, 3, 5):
                    print("Please make your choice 1, 2, 3 or 5")
        else:
            self.get_type_of_input()

    def get_type_of_input(self):
        while self.type_of_input not in (1, 2, 3):
            try:
                self.type_of_input = int(
                    input(f"Please for enter your Publication manually "
                          f"enter 1. \nTo get "
                          f"Publication from the "
                          f"txt file enter 2\nTo get "
                          f"Publication from the "
                          f"JSON file enter 3\n: "))
            except ValueError:
                print("Sorry, I didn't understand that. Only numbers "
                      "please")
            else:
                if self.type_of_input == 1:
                    break
                if self.type_of_input == 2 or self.type_of_input == 3:
                    print('File path definition.')
                    self.get_path_name()

    def get_path_name(self):
        self.path_name = input(
            f"Please enter your file path or "
            f"Enter to use default: ")
        if self.path_name != '':
            self.check_path_to_file()
        if self.path_name == '':
            if self.type_of_input == 2:
                print('Please note that default file name is '
                      'Publication.txt in Publikation catalog')
                script_dir = os.path.dirname(__file__)
                self.path_name = os.path.join(script_dir,
                                              'Publikation\\'
                                              'Publication.txt')
            if self.type_of_input == 3:
                print('Please note that default file name is '
                      'Publication.json in Publikation catalog')
                script_dir = os.path.dirname(__file__)
                self.path_name = os.path.join(script_dir,
                                              'Publikation\\'
                                              'Publication.json')

    def check_path_to_file(self):
        x: int = 1
        while x > 0:
            try:
                test_file = open(self.path_name)
                test_file.close()
            except IOError:
                print('File not found or cannot be opened')
                self.path_name = input(f"Please enter your file path: ")
            if self.path_name == '':
                x = 0
            else:
                x = 0

    def setup_publication_parameters(self):
        global publication
        if self.type_of_content == 1:
            publication = News()
        if self.type_of_content == 2:
            publication = Ad()
        if self.type_of_content == 3:
            publication = ZenOfPython()


class GetPublicationManually:
    def __init__(self):
        self.text = str
        self.setup_text()
        self.other = str
        self.setup_other_param()

    def setup_text(self):
        global publication
        self.text = input(f"Please enter your {publication.name}: ")
        publication.text.append(self.text)

    def setup_other_param(self):
        global publication
        if input_parameters.type_of_content == 1:
            self.other = input(f"Please enter your City: ")
            publication.city.append(self.other)
        if input_parameters.type_of_content == 2:
            self.other = input(f"Please enter expiration date (DD/MM/YYYY): ")
            publication.expiration_date.append(
                publication.checking_expiration_date(self.other))
            publication.days_left.append(
                publication.get_days_left(publication.expiration_date[0]))
        if input_parameters.type_of_content == 3:
            publication.number_of_principle.\
                append(publication.get_principle_number(publication.text[0]))


class GetPublicationFromTXT:
    def __init__(self):
        self.text = []
        self.parse_rows_from_text_file()

    def parse_rows_from_text_file(self):
        print('Note, Publication in a single row. Delimiter should be "|".')
        f = open(input_parameters.path_name, 'r')
        self.text = f.read()
        for row in self.text.split('\n'):
            row_pub = []
            for parameter in row.split('|'):
                par = norm(str(parameter))
                row_pub.append(par[0])
            publication.text.append(str(row_pub[0]))
            if input_parameters.type_of_content == 1:
                publication.city.append(str(row_pub[1]))
            if input_parameters.type_of_content == 2:
                publication.expiration_date.\
                    append(publication.
                           checking_expiration_date(str(row_pub[1])))
                publication.days_left.append(publication.
                                             get_days_left(str(row_pub[1])))
            if input_parameters.type_of_content == 3:
                publication.number_of_principle.\
                    append(publication.get_principle_number(str(row_pub[0])))

        f.close()

        # Delete file after reading all rows
        os.remove(input_parameters.path_name)


class GetPublicationFromJSON:
    def __init__(self):
        self.text = []
        self.parse_rows_from_json_file()

    def parse_rows_from_json_file(self):
        f = open(input_parameters.path_name, 'r')
        self.text = json.load(f)

        for row in range(len(self.text)):
            for key, value in self.text[row].items():
                if key == 'text':
                    publication.text.append(value)
                    if input_parameters.type_of_content == 3:
                        publication.number_of_principle.\
                            append(publication.get_principle_number(value))
                if key == 'other_param':
                    if input_parameters.type_of_content == 1:
                        publication.city.append(value)
                    if input_parameters.type_of_content == 2:
                        publication.expiration_date.\
                            append(publication.
                                   checking_expiration_date(value))
                        publication.days_left.append(publication.
                                                     get_days_left(value))

        f.close()

        # Delete file after reading all rows
        os.remove(input_parameters.path_name)


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


# Print Into File
class PrintIntoFile:
    def __init__(self, full_publication):
        self.publication = full_publication

    def print_publication(self):
        f = open('module_5_homework_result.txt', 'a')
        f.write(self.publication + '\n')
        f.close()
        CSVParsing().create_word_count_csv()
        CSVParsing().create_letters_csv()


class CreateFile:
    def __init__(self):
        self.path_name = str

    def create_test_txt_file_if_needed(self):
        self.path_name = os.path.dirname(__file__)
        self.path_name = os.path.join(self.path_name, 'Publikation\\'
                                                      'Publication.txt')
        try:
            def_file = open(self.path_name, 'x')
            def_file.write(f'Readability counts.|01/01/2025\n'
                           f'Although practicality beats purity.|15/10/2022\n'
                           f'Errors should never pass silently.|01/09/2032\n'
                           f'Unless explicitly silenced.|01/10/2028')
            def_file.close()
        except IOError:
            return True
        else:
            return True

    def create_test_json_file_if_needed(self):
        self.path_name = os.path.dirname(__file__)
        self.path_name = os.path.join(self.path_name, 'Publikation\\'
                                                      'Publication.json')
        try:
            def_file = open(self.path_name, 'x')
            def_file.write(json.dumps([{"text": "Readability counts.",
                                        "other_param": "01/10/2028"},
                                       {"text": "Although practicality beats "
                                                "purity.", "other_param":
                                           "05/01/2022"}]))
            def_file.close()
        except IOError:
            return True
        else:
            return True


if __name__ == "__main__":
    while True:
        # if you need a test file - please uncomment the text below
        file = CreateFile()
        file.create_test_txt_file_if_needed()
        file.create_test_json_file_if_needed()

        # main code
        input_parameters = InputParameters()
        input_parameters.get_input_parameters()
        publication = Publication()
        input_parameters.setup_publication_parameters()
        if input_parameters.type_of_input == 1:
            GetPublicationManually()
            publication.get_full_publication(0)
            print_into = PrintIntoFile(publication.full_publication)
            print_into.print_publication()
        if input_parameters.type_of_input == 2:
            GetPublicationFromTXT()
            for p in range(len(publication.text)):
                publication.get_full_publication(p)
                print_into = PrintIntoFile(publication.full_publication)
                print_into.print_publication()
        if input_parameters.type_of_input == 3:
            GetPublicationFromJSON()
            for p in range(len(publication.text)):
                publication.get_full_publication(p)
                print_into = PrintIntoFile(publication.full_publication)
                print_into.print_publication()
