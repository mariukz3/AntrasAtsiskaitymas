from string import ascii_lowercase
from collections import Counter
import glob

GLOBLINES = 0
GLOBWORDS = 0
GLOBCHARS = 0

def SurinktiFailoStatistikas(SkaitomasFailas, RezultatuFailas):
    
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

    global GLOBLINES
    GLOBLINES = GLOBLINES + num_lines
    global GLOBWORDS
    GLOBWORDS = GLOBWORDS + num_words
    global GLOBCHARS
    GLOBCHARS = GLOBCHARS + num_chars

    result.close()

def SujungtiFailus(RezultatuFailas):

    read_files = glob.glob('Read*.txt')

    with open(str(RezultatuFailas), "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())

def SurinktiFailuStatistikas(RezultatuFailas):

    result = open(RezultatuFailas, 'w')
    result.write('\nBendras failu eiluciu skaicius:')
    result.write(str(GLOBLINES))
    result.write('\nBendras failu zodziu skaicius:')
    result.write(str(GLOBWORDS))
    result.write('\nBendras failu simboliu skaicius:')
    result.write(str(GLOBCHARS))
    result.close()
