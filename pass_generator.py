from random import randint

dictionary = []


def pass_gen():
    password = ""
    with open('dictionary.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = ''.join(sorted(set(line), key=line.index))
            if len(line) == 9:
                dictionary.append(line.strip().title())
    n = dictionary[randint(1, len(dictionary) - 1)]
    m = dictionary[randint(1, len(dictionary) - 1)]
    number = randint(100, 999)
    heda_pass = m + str(number)
    dc_pass = n + str(number)
    control = True
    while control:
        if n != m:
            password = n + m + str(number)
            control = False
        else:
            control = True
    return dc_pass, heda_pass, password


def eesti_speller(x):
    for i in range(len(x) - 1):
        x = x.replace("š", "sh")
        x = x.replace("Š", "Sh")
        x = x.replace("ž", "zh")
        x = x.replace("Ž", "Zh")
        x = x.replace("Ä", "A")
        x = x.replace("ä", "a")
        x = x.replace("Ö", "O")
        x = x.replace("Õ", "O")
        x = x.replace("ö", "o")
        x = x.replace("õ", "y")
        x = x.replace("Ü", "U")
        x = x.replace("u", "u")
    return x
