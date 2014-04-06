from string import ascii_lowercase
from collections import Counter

def SutvarkytiFaila(SkaitomasFailas, RezultatuFailas):
    
    num_lines = 0
    num_words = 0
    num_chars = 0

    result = open(RezultatuFailas, 'w')

    with open(str(SkaitomasFailas)) as f:
        result.write("Raidziu yra:")
        result.write(str(Counter(
            letter for line in f
            for letter in line.lower()
            if letter in ascii_lowercase)))

    with open(str(SkaitomasFailas)) as f:
        for line in f:
            words = line.split()
            num_lines += 1
            num_words += len(words)
            num_chars += len(line)

    result.write('\nEiluciu skaicius:')
    result.write(str(num_lines))
    result.write('\nZodziu skaicius:')
    result.write(str(num_words))
    result.write('\nSimboliu skaicius:')
    result.write(str(num_chars))

    result.close()
