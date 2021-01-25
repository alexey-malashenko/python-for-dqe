# import module random to get randint
import random

# a variable to repeat the loop 100 times to get random numbers
loop = range(100)

# a variable to get empty list
list = []

# varables for even and odd
even = 0
e = 0
odd = 0
o = 0

# cycle to fill list with random 100 values
for i in loop:
    # print(random.randint(0, 1000))
    list.append(random.randint(0, 1000))
# print(list)

# sort list values from min to max
list.sort()
# print(list)

# cycle to separate even and odd values, summarise and count values
for x in list:
    # print(x)
    # summarise and count values for even
    if x % 2 == 0:
        even = even + x
        e += 1
    # summarise and count values for odd
    else:
        odd = odd + x
        o += 1

# print(even)
# print(odd)
# print(e)
# print(o)
# print(list)

# calculate average value
even = even / e
odd = odd / o

# print the result
print("average even =", even, "|", "average odd =", odd)