# Homework:
# Write a code, which will:
# 1. create a list of random number of dicts (from 2 to 10)
# dicts random numbers of keys should be letter,
# dicts values should be a number (0-100),
# example:[{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
# 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with
# dict number with max value
# if key is only in one dict - take it as is,
# example:{'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

import string
import random
import dis

# use decorator for debugging


def decorator_function(func):
    def wrapper(a):
        print('Debugging... Intermediate result is:')
        func(a)
        print('Debugging is finished\n')
    return wrapper


@decorator_function
def debug(f):
    print(f)
    return


# function to get random value


def foo_rand(x, y):
    rand_value = random.randint(x, y)
    return rand_value


# function to get a filled list of random number of dicts


def foo_list_of_dicts():
    # var list of random number of dicts
    temp_list_of_dicts = []

    # this part for list of random number of dicts (from 2 to 10)
    for ti in range(foo_rand(2, 10)):
        debug(f'Next dict {ti + 1}')
        # English alphabet length
        g = foo_rand(1, 26)
        d = {}
        for k in range(g):
            # random word from English alphabet as key
            d.setdefault(random.choice(string.ascii_lowercase),
                         foo_rand(0, 100))
        temp_list_of_dicts.append(d)
        debug(f'list append for {ti + 1} dict: {temp_list_of_dicts}')
    return temp_list_of_dicts


# print(foo_list_of_dicts())

# function to get one common dict from a list of random number of dicts
def foo_common_list():

    # temporary dicts
    temp_dict = {}
    dict_number = {}
    final_dict = {}

    # iterating over the list
    # get a filled list from function to list_of_dicts
    list_of_dicts = foo_list_of_dicts()

    # iterating over the dicts in the list
    for i in range(len(list_of_dicts)):

        # iterating over keys and values in each dict
        for key, value in list_of_dicts[i].items():

            # check if the key is in the temp_dict - if not, insert it
            if key in temp_dict.keys():
                # if the key in the dict and its value is more than in
                # the dictionary - delete the old value in the
                # dictionary and insert a new one
                if value > temp_dict.get(key):
                    # a separate dictionary where we collect duplicate
                    # keys and numbers of the largest dictionary number
                    if key in dict_number.keys():
                        dict_number.pop(key)
                        dict_number.setdefault(key, i)
                    else:
                        dict_number.setdefault(key, i)
                    temp_dict.pop(key)
                    temp_dict.setdefault(key, value)
            else:
                temp_dict.setdefault(key, value)

    # merge all dicts
    for key, value in temp_dict.items():
        if key in dict_number.keys():
            final_dict.setdefault(key + '_' + str(dict_number.get(key)), value)
        else:
            final_dict.setdefault(key, value)
    return final_dict


print(f'Result: {foo_common_list()}')
