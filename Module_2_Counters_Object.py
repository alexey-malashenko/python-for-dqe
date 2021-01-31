# 34567890123456789012345678901234567890123456789012345678901234567890123456789
# 3456789012345678901234567890123456789012345678901234567890123456789012

# Homework:
# Write a code, which will:
# 1. create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example:[{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

# import module random to get randint
import random
import string

# var for random number of dicts (from 2 to 10)
rdic = random.randint(2, 10)

# var list of random number of dicts
lis = []

# this part for list of random number of dicts (from 2 to 10)
for i in range(rdic):
    # English alphabet length
    g = random.randint(1, 26)
    d = {}
    for k in range(g):
        # random word from English alphabet as key
        d.setdefault(random.choice(string.ascii_lowercase),
                     random.randint(0, 100))
    lis.append(d)
# print(lis)

# 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with
# dict number with max value
# if key is only in one dict - take it as is,
# example:{'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

# temporary dicts
tempdict = {}
dictnumber = {}

# iterating over the list
for i in range(len(lis)):
    # iterating over the dicts in the list
     for key, value in lis[i].items():
          # check if the key is in the tempdict - if not, insert it
          if key in tempdict.keys():
               # if the key in the dict and its value is more than in
               # the dictionary - delete the old value in the
               # dictionary and insert a new one
               if value > tempdict.get(key):
                    # a separate dictionary where we collect duplicate
                    # keys and numbers of the largest dictionary number
                    if key in dictnumber.keys():
                        dictnumber.pop(key)
                        dictnumber.setdefault(key, i)
                    else: dictnumber.setdefault(key, i)
                    tempdict.pop(key)
                    tempdict.setdefault(key, value)
          else: tempdict.setdefault(key, value)
# print(tempdict)
# print(tempdict.keys())
# print(dictnumber)

finaldict = {}
# merge two dicts
for key, value in tempdict.items():
     if key in dictnumber.keys():
          finaldict.setdefault(key +'_' + str(dictnumber.get(key)), value)
     else: finaldict.setdefault(key, value)

print(finaldict)