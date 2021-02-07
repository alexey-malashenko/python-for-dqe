import re

# ...copy these Text to variable...

conditions = r'''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

# use decorator for debugging


def decorator_function(func):
    def wrapper(a):
        print('Debugging... Intermediate result is:----------------')
        func(a)
        print('Debugging is finished.------------------------------\n')
    return wrapper


@decorator_function
def debug(a):
    print(a)
    return


# count number of whitespace characters

def foo_count_whitespaces(var_text):
    count = 0
    for x in var_text:
        if x.isspace():
            count += 1
    return count


debug(f"Initial number of whitespace characters is: "
      f"{foo_count_whitespaces(conditions)}")

# function to ...fix“iZ” with correct “is”, but ONLY when it Iz
# a mistAKE... and get lower letters


def iz_is(par):
    i = re.sub(r' iz ', ' is ', par.lower())
    return i


debug(f'Check lower case and "is" replaced:\n{iz_is(conditions)}')

# function to ...create one MORE senTENCE witH LAST WoRDS of
# each existING SENtence...


def foo_additional_sent(a):
    add_it = []
    for s in re.sub(r'[\n\t]', '', a).replace(':', '.').split("."):
        add_it.extend(re.findall(r'\w+$', s))
    add_it = (' '.join(str(e) for e in add_it).capitalize() + '.')
    return add_it


debug(f'Check additional sentence:\n{foo_additional_sent(iz_is(conditions))}')

# function to ...You NEED TO normalize it fROM letter CASEs point
# oF View.


def normalize(a):
    t_list = a.split('\t')
    app_list = []

    # Capitalize after "\t"
    for t in range(len(t_list)):

        # take parts without last one
        if t < len(t_list) - 1:
            plist = []
            list_to_string = ''

            # Capitalize after ". "
            for p in range(len(t_list[t].split('. '))):
                # take parts without last one
                if p < len(t_list[t].split('. ')) - 1:
                    plist.append(t_list[t].split('. ')[p].capitalize() + '. ')
                # take last one part
                else:
                    plist.append(t_list[t].split('. ')[p].capitalize())
                list_to_string = ''.join(map(str, plist))
            app_list.append(list_to_string + '\t')
        # take last one part
        else:
            plist = []
            list_to_string = ''
            for f in range(len(t_list[t].split('. '))):
                if f < (len(t_list[t].split('. ')) - 1):
                    plist.append(t_list[t].split('. ')[f].capitalize() + '. ')
                else:
                    plist.append(t_list[t].split('. ')[f].capitalize())
                list_to_string = ''.join(map(str, plist))
            app_list.append(list_to_string)
    debug(f'App_list is:\n{app_list}')
    return app_list


# join to string
homework = ''.join(map(str, normalize(iz_is(conditions))))

# ...and add it to the END OF this Paragraph...
homework = re.sub('paragraph.', 'paragraph. ' + foo_additional_sent(iz_is(conditions)), homework)

# print the result
print(homework)
print(f"Number of whitespace characters is {foo_count_whitespaces(homework)}")
