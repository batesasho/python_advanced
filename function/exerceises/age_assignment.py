def age_assignment(*args, **kwargs):
    names = args
    names_dictionary = kwargs
    name_age_dictionary = {}
    for name in names:
        if name[0] in names_dictionary:
            name_age_dictionary[name] = names_dictionary[name[0]]
    return name_age_dictionary


print(age_assignment("Peter", "George", G = 26, P = 19))
