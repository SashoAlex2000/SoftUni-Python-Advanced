
def concatenate(*args,**kwargs):
    initial_list = []

    for wd in args:
        initial_list.append(wd)
    word = "".join(initial_list)

    for key, value in kwargs.items():
        if key in word:
            word = word.replace(key,value)

    return word

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
