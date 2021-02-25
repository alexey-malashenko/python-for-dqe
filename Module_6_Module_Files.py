# Homework:
# Create a tool, which will do user generated news feed:
# User select what data type he wants to add
# Provide record type required data
# Record is published on text file in special format
#
# You need to implement:
# News – text and city as input. Date is calculated during publishing.
# Privat ad – text and expiration date as input. Day left is calculated
# during publishing.
# Your unique one with unique publish rules.
#
# Each new record should be added to the end of file. Commit file in
# git for review.
# ---------------------------------------------------------------------
# News feed:
# News -------------------------
# Something happened
# London, 03/01/2021 13.45
#
# News -------------------------
# Something other happened
# Minsk, 24/01/2021 20.33
#
# Private Ad ------------------
# I want to sell a bike
# Actual until: 01/03/2021, 21 days left
#
# Joke of the day ------------
# Did you hear about the claustrophobic astronaut?
# He just needed a little space
# Funny meter – three of ten

# --------------------------  HOME WORK -------------------------------
import os
import re
import Module_7_CSV_Parsing as Csv
from time import gmtime, strftime, strptime
from datetime import datetime
from Module_4_Functions_Refactor_Module3 import normalize as norm


# some global variables
publication_type = ''
path_name = ''
text_from_file = []


# parent object (Inheritance). Have common attributes with News, Ad and Zen
class Publication:

    def __init__(self, name, text):
        self.name = name
        self.text = text


# child from Publication for News
class News(Publication):
    def __init__(self, name, text, city):
        Publication.__init__(self, name, text)
        self.city = city
        self.current_date = strftime('%d/%m/%Y %H:%M', gmtime())


# child from Publication for Advertisement
class Ad(Publication):
    def __init__(self, name, text, expiration_date='01/01/1900'):
        Publication.__init__(self, name, text)
        self.expiration_date = expiration_date
        self.current_date = strftime('%d/%m/%Y', gmtime())
        self.days_left = ''

    # expiration date should be date and correct
    def checking_expiration_date(self):
        while True:
            try:
                self.expiration_date == strptime(self.expiration_date,
                                                 '%d/%m/%Y')
            except ValueError:
                print('Invalid date!')
                self.expiration_date = input("Please enter correct "
                                             "expiration date DD/MM/YYYY\n")
            else:
                self.expiration_date = str(self.expiration_date)
                self.get_days_left()
                break

    # get days left
    def get_days_left(self):
        last = datetime.strptime(self.expiration_date, '%d/%m/%Y')
        now = datetime.strptime(self.current_date, '%d/%m/%Y')
        self.days_left = (last - now).days
        # return self.days_left


# child from Publication for my oun block
class ZenOfPython(Publication):
    def __init__(self, name, text):
        Publication.__init__(self, name, text)
        self.zen_dict = dict()
        self.principle = dict()
        self.number_of_principle = int

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
            self.zen_dict[i] = principle.replace('    ', '')
            i += 1
        return self.zen_dict

    # get principle from dictionary with Zen principles
    def get_principle(self):
        self.principle = self.get_zen_dict().get(int(self.text))

    # principle number should be a number
    def checking_principle_number(self):
        while True:
            try:
                self.text == int(self.text)
            except ValueError:
                print('Invalid input!')
                self.text = input("Please enter correct number 1-19: ")
            else:
                self.text = str(self.text)
                break

    # principle number should be between 1 and 19
    def checking_correct_principle_number(self):
        while True:
            if 1 <= int(self.text) <= 19:
                break
            else:
                print('Invalid input!')
                self.text = input("Please choose between 1 and 19: ")


# Print Into File
class PrintIntoFile:
    def __init__(self, publication):
        self.publication = publication

    def print_publication(self):
        f = open('module_5_homework_result.txt', 'a')
        f.write(self.publication + '\n')
        f.close()
        Csv.CSVParsing().create_word_count_csv()
        Csv.CSVParsing().create_letters_csv()


# additional class to get information from File
# and batch method (Task module 6)
class GetFromFile:
    def __init__(self):
        self.record_type = int()
        self.type_of_input = str
        self.path_name = str
        self.text = str
        self.list_temp = []
        self.x = int

    def input_text(self):
        while publication_type not in (1, 2):
            try:
                self.type_of_input = int(input(f"Please for enter your "
                                               f"{publication_type} manually "
                                               f"enter 1. To get "
                                               f"{publication_type} from the "
                                               f"file enter 2: "))
            except ValueError:
                print("Sorry, I didn't understand that. Only numbers "
                      "please")
            else:
                if self.type_of_input == 1:
                    text_from_file.append(input(f"Please enter your "
                                                f"{publication_type}: "))
                    break
                if self.type_of_input == 2:
                    print('Please note that default file name is '
                          'Publication.txt in Publikation catalog')
                    global path_name
                    self.path_name = input(f"Please enter your file path or "
                                           f"Enter to use default: ")

                    if self.path_name == '':
                        script_dir = os.path.dirname(__file__)
                        path_name = os.path.join(script_dir, 'Publikation\\'
                                                             'Publication.txt')
                        self.check_path_to_file()
                        self.parse_rows_from_text_file()
                        break
                    if self.path_name != '':
                        path_name = self.path_name
                        self.check_path_to_file()
                        self.parse_rows_from_text_file()
                        break
                if self.type_of_input not in (1, 2):
                    print("Please make your choice only between 1 and 2")
        return text_from_file

    def check_path_to_file(self):
        self.x: int = 1
        while self.x > 0:
            global path_name
            try:
                test_file = open(path_name)
                test_file.close()
            except IOError:
                print('File not found or cannot be opened')
                path_name = input(f"Please enter your file path: ")
            else:
                self.x = 0

    def parse_rows_from_text_file(self):
        self.text = open(path_name, 'r')
        global text_from_file
        text_from_file = self.text.read()
        text_from_file = ''.join(map(str, norm(text_from_file)))
        text_from_file = os.linesep.join([s for s in
                                          text_from_file.splitlines() if s])
        text_from_file = text_from_file.split('\n')
        for row in text_from_file:
            reg = re.compile('[^a-zA-Z ,.]')
            row = reg.sub('', row)
            self.list_temp.append(row)
        self.text.close()
        text_from_file = self.list_temp

        # Delete file after reading all rows
        os.remove(path_name)


# This is the main class
class Main:
    def __init__(self):
        self.record_type = int()
        self.publication = ''

    def input_record_type(self):
        while True:
            while self.record_type not in (1, 2, 3, 5):
                try:
                    self.record_type = int(input("Please choose the type of "
                                                 "content:\n"
                                                 "1 - News\n"
                                                 "2 - Ad\n"
                                                 "3 - The Zen of Python\n"
                                                 "5 - For Exit\n"
                                                 "Please type here: "))
                except ValueError:
                    print("Sorry, I didn't understand that. Only numbers "
                          "please")
                else:
                    if self.record_type == 5:
                        exit()
                    if self.record_type not in (1, 2, 3, 5):
                        print("Please make your choice 1, 2, 3 or 5")
            else:
                global publication_type
                input_text = GetFromFile()
                if self.record_type == 1:
                    publication_type = 'News'

                    news = News('News -------------------------',
                                # input("Please enter your News: "),
                                input_text.input_text(),
                                input("Please enter your City: "))
                    self.decomposition_batch(news)
                    self.record_type = 0

                if self.record_type == 2:
                    publication_type = 'Ad'
                    ad = Ad('Private Ad -------------------',
                            # input("Please enter your Ad: "),
                            input_text.input_text(),
                            input("Please enter expiration date: "))

                    ad.checking_expiration_date()

                    self.decomposition_batch(ad)
                    self.record_type = 0

                if self.record_type == 3:
                    zen = ZenOfPython('The Zen of Python ------------',
                                      input("Please enter 1-19: "))
                    zen.get_zen_dict()
                    zen.checking_principle_number()
                    zen.checking_correct_principle_number()
                    zen.get_principle()
                    publication = f'{zen.name}\nSelected number is: ' \
                                  f'{str(zen.text)}\n{zen.principle}\n'
                    publication = PrintIntoFile(publication)
                    publication.print_publication()
                    self.record_type = 0

    def decomposition_batch(self, name):
        global text_from_file
        for batch in text_from_file:
            name.text = batch
            if publication_type == 'News':
                self.publication = f'{name.name}\n{name.text}\n{name.city}, ' \
                                   f'{str(name.current_date)}\n'
            if publication_type == 'Ad':
                self.publication = f'{name.name}\n{name.text}\nActual until: '\
                                   f'{str(name.expiration_date)}, ' \
                                   f'{str(name.days_left)} days left\n'
            publication = PrintIntoFile(self.publication)
            publication.print_publication()
        # global text_from_file
        text_from_file = []


class CreateFile:
    def __init__(self):
        self.path_name = str

    def create_test_file_if_nedeed(self):
        self.path_name = os.path.dirname(__file__)
        self.path_name = os.path.join(self.path_name, 'Publikation\\'
                                                      'Publication.txt')
        try:
            def_file = open(self.path_name, 'x')
            def_file.write(r'''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
''')
            def_file.close()
        except IOError:
            return True
        else:
            return True


if __name__ == "__main__":
    # if you need a test file - please uncomment the text below
    # file = CreateFile()
    # file.create_test_file_if_nedeed()
    a = Main()
    a.input_record_type()
