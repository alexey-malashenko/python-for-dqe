# Warning!!! Hard-code detected!!!

# ...copy these Text to variable...

a = r'''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

# print(int(a.count(' ')) + int(a.count('\t')) + int(a.count('\n')))

# ...normalize it fROM letter CASEs point oF View...

import re
# print(re.split('\t',a))
addit = []
templist = []

for x in re.split('\t',a):
    for s in [(re.sub("^\s+|\n|\r|\s+$", '', x).lower())]:
        templist.append(re.sub("^\s+|\n|\r|\s+$", '', '. '.join([i.strip().capitalize() for i in re.sub(r' iz ', ' is ', s).split('.')])))
        addit.extend(re.findall('\s(\S+)(?:\n|\Z)', s.replace('.', '')))

addit = [' '.join(str(e) for e in addit).capitalize()+'.']

a = (templist[0]+'\n\t'+templist[1]+' '+'\n\n\t'+templist[2]+' '+(addit[0])+'\n\n\t'+templist[3]+' '+'\n\n\t'+templist[4]+'\n')

print(a)
print('Number of whitespace characters is '+str(int(a.count(' ')) + int(a.count('\t')) + int(a.count('\n'))))