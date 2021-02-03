import re

conditions = r'''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

tempvar = re.sub(r' iz ', ' is ', conditions.lower())
# print(tempvar)

tlist = tempvar.split('\t')
applist = []
homework = ''

for t in range(len(tlist)):
    if t < len(tlist) - 1:
        plist = []
        listToString = ''
        for p in range(len(tlist[t].split('. '))):
            if p < len(tlist[t].split('. ')) - 1:
                plist.append(tlist[t].split('. ')[p].capitalize() + '. ')
            else: plist.append(tlist[t].split('. ')[p].capitalize())
            listToString = ''.join(map(str, plist))
        applist.append(listToString + '\t')
    else:
        plist = []
        listToString = ''
        for f in range(len(tlist[t].split('. '))):
            if f < (len(tlist[t].split('. ')) - 1):
                plist.append(tlist[t].split('. ')[f].capitalize() + '. ')
            else: plist.append(tlist[t].split('. ')[f].capitalize())
            listToString = ''.join(map(str, plist))
        applist.append(listToString)

homework = ''.join(map(str, applist))

print('applist ', applist)
print('homework ', homework)

