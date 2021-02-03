# without hard-code

import re

# ...copy these Text to variable...

conditions = r'''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

# check initial parameters
# print(conditions)

# count = 0
# for x in conditions:
#     if x.isspace() == True:
#         count += 1
# print(f"Number of whitespace characters is {count}")

# ...fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE...

tempvar = re.sub(r' iz ', ' is ', conditions.lower())
# print(tempvar)

# ...create one MORE senTENCE witH LAST WoRDS of each existING SENtence...

addit = []
for s in re.sub(r'\n|\t', '', tempvar).replace(':', '.').split("."):
    addit.extend(re.findall(r'\w+$', s))
addit = (' '.join(str(e) for e in addit).capitalize()+'.')
# print(addit)

# You NEED TO normalize it fROM letter CASEs point oF View.

tlist = tempvar.split('\t')

applist = []
homework = ''

# Capitalize after "\t"
for t in range(len(tlist)):

    # take parts without last one
    if t < len(tlist) - 1:
        plist = []
        listToString = ''

        # Capitalize after ". "
        for p in range(len(tlist[t].split('. '))):
            # take parts without last one
            if p < len(tlist[t].split('. ')) - 1:
                plist.append(tlist[t].split('. ')[p].capitalize() + '. ')
            # take last one part
            else: plist.append(tlist[t].split('. ')[p].capitalize())
            listToString = ''.join(map(str, plist))
        applist.append(listToString + '\t')
    # take last one part
    else:
        plist = []
        listToString = ''
        for f in range(len(tlist[t].split('. '))):
            if f < (len(tlist[t].split('. ')) - 1):
                plist.append(tlist[t].split('. ')[f].capitalize() + '. ')
            else: plist.append(tlist[t].split('. ')[f].capitalize())
            listToString = ''.join(map(str, plist))
        applist.append(listToString)

# join to string
homework = ''.join(map(str, applist))

# ...and add it to the END OF this Paragraph...
homework = re.sub('paragraph.', 'paragraph. ' + addit, homework)

# count number of whitespace characters
count = 0
for x in homework:
    if x.isspace() == True:
        count += 1

# print the result
print(homework)
print(f"Number of whitespace characters is {count}")