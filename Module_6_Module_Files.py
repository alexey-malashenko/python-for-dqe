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
from time import gmtime, strftime, strptime
from datetime import datetime
from Module_4_Functions_Refactor_Module3 import normalize as norm


# parent object (Inheritance).
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
    def __init__(self, name, text, expiration_date):
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
                break

    # get days left
    def foo_days_left(self):
        last = datetime.strptime(self.expiration_date, '%d/%m/%Y')
        now = datetime.strptime(self.current_date, '%d/%m/%Y')
        self.days_left = (last - now).days


# child from Publication for my oun block
class ZenOfPython(Publication):
    def __init__(self, name, text):
        Publication.__init__(self, name, text)
        self.zen_dict = dict()
        self.principle = dict()
        self.number_of_principle = int

    # get dictionary with Zen principles
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


publ_name = ''
path_name = ''


# additional class to get information (Task module 6)
class GetFromFile:
    def __init__(self):
        self.record_type = int()
        self.publ_name = str
        self.path_name = str

    def input_text(self):
        global publ_name
        while publ_name not in (1, 2):
            try:
                self.publ_name = int(input(f"Please for enter your "
                                           f"{publ_name} manually - enter 1 "
                                           f"or 2 for get {publ_name} "
                                           f"from the file: "))
            except ValueError:
                print("Sorry, I didn't understand that. Only numbers "
                      "please")
            else:
                if self.publ_name == 1:
                    publ_name = input(f"Please enter your {publ_name}: ")
                    break
                if self.publ_name == 2:
                    print('Please note that file name should be Publication.txt')
                    global path_name
                    self.path_name = input(f"Please enter your Catalog or Enter to use default: ")
                    # need to add an error handler
                    if self.path_name == '':
                        script_dir = os.path.dirname(__file__)
                        path_name = os.path.join(script_dir, 'Publikation\\Publication.txt')
                        file = open(path_name, 'r')
                        publ_name = file.read()
                        publ_name = ''.join(map(str, norm(publ_name)))
                        file.close()
                        os.remove(path_name)
                        break
                    if self.path_name != '':
                        path_name = self.path_name
                        file = open(path_name, 'r')
                        publ_name = file.read()
                        publ_name = ''.join(map(str, norm(publ_name)))
                        file.close()
                        os.remove(path_name)
                        break
                if self.publ_name not in (1, 2):
                    print("Please make your choice only between 1 and 2")
        return publ_name

    def read_news_from_text(self):
        pass


# This is the main class
class Main:
    def __init__(self):
        self.record_type = int()

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
                global publ_name
                input_text = GetFromFile()
                if self.record_type == 1:
                    publ_name = 'News'
                    news = News('News -------------------------',
                                # input("Please enter your News: "),
                                input_text.input_text(),
                                input("Please enter your City: "))
                    publication = f'{news.name}\n{news.text}\n{news.city}, ' \
                                  f'{str(news.current_date)}\n'
                    publication = PrintIntoFile(publication)
                    publication.print_publication()
                    self.record_type = 0

                if self.record_type == 2:
                    publ_name = 'Ad'
                    ad = Ad('Private Ad -------------------',
                            # input("Please enter your Ad: "),
                            input_text.input_text(),
                            input("Please enter expiration date: "))
                    ad.checking_expiration_date()
                    ad.foo_days_left()
                    publication = f'{ad.name}\n{ad.text}\nActual until: ' \
                                  f'{str(ad.expiration_date)}, ' \
                                  f'{str(ad.days_left)} days left\n'
                    publication = PrintIntoFile(publication)
                    publication.print_publication()
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


a = Main()
a.input_record_type()
