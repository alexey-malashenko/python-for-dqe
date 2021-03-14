# ---------------------------------- PLEASE ----------------------------------

# ----------------------------------- NOTE -----------------------------------

# ----------------------------- FULL REFACTORING -----------------------------

# Homework:
#
# Description
# Expand previous Homework 5/6/7/8/9 with additional class, which allow
# to save records into database:
# 1.Different types of records require different data tables
# 2.New record creates new row in data table
# 3.Implement “no duplicate” check.

# --------------------------  HOME WORK -------------------------------
import os
import json
import csv
import re
import collections
import pyodbc
import xml.etree.ElementTree as ElTr
from time import gmtime, strftime, strptime
from datetime import datetime
from Module_4_Functions_Refactor_Module3 import normalize as norm


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
        py_zen = """Beautiful is better than ugly.
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
        for principle in py_zen.split('\n'):
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
        return str(principle_number)

    def get_full_publication(self, i):
        self.full_publication = f'{self.name} {self.decoration_line}\n' \
                                f'{self.text[i]}\n' \
                                f'Number of Zen is: ' \
                                f'{self.number_of_principle[i]}\n' \
                                f'{self.delimited_line}\n'


class InputParameters:
    def __init__(self):
        self.type_of_input = 0
        self.path_name = str

    def get_type_of_input(self):
        while self.type_of_input not in (1, 2, 3, 4, 5):
            try:
                self.type_of_input = int(
                    input(f"Please select input mode.\n"
                          f"To enter your Publication manually enter 1. \n"
                          f"To get Publication from the TXT file enter 2\n"
                          f"To get Publication from the JSON file enter 3\n"
                          f"To get Publication from the XML file enter 4\n"
                          f"For Exit enter 5: "))
            except ValueError:
                print("Sorry, I didn't understand that. Only numbers "
                      "please")
            else:
                if self.type_of_input == 1:
                    break
                if self.type_of_input == 2 or self.type_of_input == 3\
                        or self.type_of_input == 4:
                    print('File path definition.')
                    self.get_path_name()
                if self.type_of_input == 5:
                    exit()

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
            if self.type_of_input == 4:
                print('Please note that default file name is '
                      'Publication.xml in Publikation catalog')
                script_dir = os.path.dirname(__file__)
                self.path_name = os.path.join(script_dir,
                                              'Publikation\\'
                                              'Publication.xml')
            self.check_path_to_file()

    def check_path_to_file(self):
        x: int = 1
        while x > 0:
            try:
                test_file = open(self.path_name)
                test_file.close()
            except IOError:
                print('File not found or cannot be opened')
                self.path_name = input(f"Please enter your file path. "
                                       f"For Exit enter 5: ")
            if self.path_name == '':
                x = 0
            if self.path_name == '5':
                exit()
            else:
                x = 0


class GetPublicationManually:
    def __init__(self):
        self.type_of_content = 0
        self.get_manual_type_of_content()
        self.text = str
        self.other = str

    def get_manual_type_of_content(self):
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
            self.setup_text()

    def setup_text(self):
        if self.type_of_content == 1:
            self.text = input(f"Please enter your {news.name}: ")
            news.text.append(self.text)
            self.other = input(f"Please enter your City: ")
            news.city.append(self.other)
        if self.type_of_content == 2:
            self.text = input(f"Please enter your {ad.name}: ")
            ad.text.append(self.text)
            self.other = input(f"Please enter expiration date (DD/MM/YYYY): ")
            ad.expiration_date.append(
                ad.checking_expiration_date(self.other))
            ad.days_left.append(
                ad.get_days_left(ad.expiration_date[0]))
        if self.type_of_content == 3:
            self.text = input(f"Please enter your {zen.name}: ")
            zen.text.append(self.text)
            zen.number_of_principle.\
                append(zen.get_principle_number(zen.text[0]))


class GetPublicationFromTXT:
    def __init__(self):
        self.text = []
        self.parse_rows_from_text_file()

    def parse_rows_from_text_file(self):
        print('Note, Publication in a single row. Delimiter should be "|".')
        f = open(str(input_parameters.path_name), 'r')
        self.text = f.read()
        for row in self.text.split('\n'):
            row = row.split('|')
            if row[0] == 'News':
                news.text.append(norm(str(row[1]))[0])
                news.city.append(norm(str(row[2]))[0])
            if row[0] == 'Ad':
                ad.text.append(norm(str(row[1]))[0])
                ad.expiration_date.append(ad.checking_expiration_date(
                    str(row[2])))
                ad.days_left.append(ad.get_days_left(str(row[2])))
            if row[0] == 'Zen':
                zen.text.append(norm(str(row[1]))[0])
                zen.number_of_principle.append(zen.get_principle_number(
                    str(row[1])))

        f.close()

    # print(f'News {news.text} {news.city}, Ad {ad.text} {ad.expiration_date} '
    #       f'{ad.days_left}, Zen {zen.text}, {zen.number_of_principle}')

        # Delete file after reading all rows
        os.remove(str(input_parameters.path_name))


class GetPublicationFromJSON:
    def __init__(self):
        self.text = []
        self.parse_rows_from_json_file()

    def parse_rows_from_json_file(self):
        print('Note, Publication in a single Array.')
        f = open(str(input_parameters.path_name), 'r')
        self.text = json.load(f)

        for row in range(len(self.text)):
            pub = self.text[row]
            for key, value in self.text[row].items():
                if key == 'name' and value == 'News':
                    news.text.append(pub.get('text'))
                    news.city.append(pub.get('city'))
                if key == 'name' and value == 'Ad':
                    ad.text.append(pub.get('text'))
                    ad.expiration_date.append(ad.checking_expiration_date(
                        pub.get('date')))
                    ad.days_left.append(ad.get_days_left(pub.get('date')))
                if key == 'name' and value == 'Zen':
                    zen.text.append(pub.get('text'))
                    zen.number_of_principle.append(zen.get_principle_number(
                        pub.get('text')))

        f.close()

    # print(f'News {news.text} {news.city}, Ad {ad.text} {ad.expiration_date} '
    #       f'{ad.days_left}, Zen {zen.text}, {zen.number_of_principle}')

        # Delete file after reading all rows
        os.remove(str(input_parameters.path_name))


class GetPublicationFromXML:
    def __init__(self):
        self.text = []
        self.parse_rows_from_xml_file()

    def parse_rows_from_xml_file(self):
        print('Note, Publication in a single Attribute.')
        f = open(str(input_parameters.path_name), 'r')
        self.text = ElTr.parse(f)
        root = self.text.getroot()

        for publication_xml in root.findall('publication'):

            if publication_xml.attrib.get('name') == 'News':
                for text in publication_xml.findall('text'):
                    news.text.append(text.text)
                for city in publication_xml.findall('city'):
                    news.city.append(city.text)

            if publication_xml.attrib.get('name') == 'Ad':
                for text in publication_xml.findall('text'):
                    ad.text.append(text.text)
                for date in publication_xml.findall('date'):
                    ad.expiration_date.append(ad.checking_expiration_date(
                        date.text))
                    ad.days_left.append(ad.get_days_left(
                        date.text))

            if publication_xml.attrib.get('name') == 'Zen':
                for text in publication_xml.findall('text'):
                    zen.text.append(text.text)
                    zen.number_of_principle.append(zen.get_principle_number(
                        text.text))

        f.close()

        # Delete file after reading all rows
        os.remove(str(input_parameters.path_name))


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


# add data to database
class InsertIntoDB:
    def __init__(self, database_name):
        with pyodbc.connect(f"Driver=SQLite3 ODBC Driver;Database="
                            f"{database_name}") as self.conn:
            self.cur = self.conn.cursor()
        self.create_tables_if_not_exist()

    def create_tables_if_not_exist(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS news '
                         '(text text NOT NULL, '
                         'other text NOT NULL, '
                         'CONSTRAINT new_pk PRIMARY KEY (text, other))')
        self.cur.execute('CREATE TABLE IF NOT EXISTS ad '
                         '(text text NOT NULL, '
                         'other text NOT NULL, '
                         'CONSTRAINT new_pk PRIMARY KEY (text, other))')
        self.cur.execute('CREATE TABLE IF NOT EXISTS zen '
                         '(text text not null, '
                         'other text not null, '
                         'CONSTRAINT new_pk PRIMARY KEY (text, other))')

    def insert(self, text, other, table_name):
        try:
            self.cur.execute(f'INSERT INTO {table_name} VALUES ({text}, '
                             f'{other})')
            self.cur.commit()
        except pyodbc.Error:
            print(f'To {table_name} have been not added {text}, {other}, '
                  f'because this values exist in the table')


class CreateFile:
    def __init__(self):
        self.path_name = str

    def create_test_txt_file_if_needed(self):
        self.path_name = os.path.dirname(__file__)
        self.path_name = os.path.join(self.path_name, 'Publikation\\'
                                                      'Publication.txt')
        try:
            def_file = open(self.path_name, 'x')
            def_file.write(f'Ad|Sell the txt.|01/01/2025\n'
                           f'News|Happy New txt.|London\n'
                           f'Zen|Unless explicitly silenced.\n'
                           f'Ad|Sell txt dog.|01/12/2023\n'
                           f'News|Happy txt.|Addis Ababa\n'
                           f'Zen|Flat is better than nested.')
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
            def_file.write(json.dumps(
                [{"name": "Ad", "text": "Sell the json.",
                  "date": "01/10/2028"},
                 {"name": "News", "text": "Happy New json.",
                  "city": "London"},
                 {"name": "Zen", "text": "Unless explicitly silenced."},
                 {"name": "Ad", "text": "Sell json dog.",
                  "date": "01/12/2023"},
                 {"name": "News", "text": "Happy json me.",
                  "city": "Addis Ababa"},
                 {"name": "Zen", "text": "Flat is better than nested."}]))
            def_file.close()
        except IOError:
            return True
        else:
            return True

    def create_test_xml_file_if_needed(self):
        self.path_name = os.path.dirname(__file__)
        self.path_name = os.path.join(self.path_name, 'Publikation\\'
                                                      'Publication.xml')
        try:
            def_file = open(self.path_name, 'x')
            def_file.write('''<root>
    <publication name="Ad">
        <text>Sell the xml.</text>
        <date>01/03/2028</date>
    </publication>
    <publication name="News">
        <text>Happy New xml.</text>
        <city>London</city>
    </publication>
    <publication name="Zen">
        <text>Unless explicitly silenced.</text>
    </publication>
    <publication name="Ad">
        <text>Sell the xml second.</text>
        <date>01/03/2022</date>
    </publication>
    <publication name="News">
        <text>Test news for xml.</text>
        <city>Paris</city>
    </publication>
    <publication name="Zen">
        <text>Although practicality beats purity.</text>
    </publication>
</root>''')
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
        file.create_test_xml_file_if_needed()

        # main code
        # global variables
        news = News()
        ad = Ad()
        zen = ZenOfPython()
        insert_to_db = InsertIntoDB('publication.db')

        # get input parameters and type of input
        input_parameters = InputParameters()
        input_parameters.get_type_of_input()

        # manual type of publication
        if input_parameters.type_of_input == 1:
            GetPublicationManually()

        # get from TXT
        if input_parameters.type_of_input == 2:
            GetPublicationFromTXT()

        # get from JSON
        if input_parameters.type_of_input == 3:
            GetPublicationFromJSON()

        # get from XML
        if input_parameters.type_of_input == 4:
            GetPublicationFromXML()

        # print News
        if len(news.text) > 0:
            for p in range(len(news.text)):
                insert_to_db.insert(text=f'"{news.text[p]}"',
                                    other=f'"{news.city[p]}"',
                                    table_name=f'news')
                news.get_full_publication(p)
                print_into = PrintIntoFile(news.full_publication)
                print_into.print_publication()

        # print Ad
        if len(ad.text) > 0:
            for p in range(len(ad.text)):
                insert_to_db.insert(text=f'"{ad.text[p]}"',
                                    other=f'"{ad.expiration_date[p]}"',
                                    table_name=f'ad')
                ad.get_full_publication(p)
                print_into = PrintIntoFile(ad.full_publication)
                print_into.print_publication()

        # print Zen
        if len(zen.text) > 0:
            for p in range(len(zen.text)):
                insert_to_db.insert(text=f'"{zen.text[p]}"',
                                    other=f'"'
                                          f'{str(zen.number_of_principle[p])}'
                                          f'"',
                                    table_name=f'zen')
                zen.get_full_publication(p)
                print_into = PrintIntoFile(zen.full_publication)
                print_into.print_publication()
