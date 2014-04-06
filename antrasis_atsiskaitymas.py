from string import ascii_lowercase
from collections import Counter
import glob
import os

# Globalus kintamieji bendrai statistikai vesti

GLOBLIST = []
GLOBLINES = 0
GLOBWORDS = 0
GLOBCHARS = 0

# Atidaromas statistiku kaupimo failas

GLOBRESULT = open('STATISTIKA.txt', 'w')

# Funkcija zodziams nuskaityti


def SkaitytiZodzius(skaitomas_failas):
    atidarytas = open(skaitomas_failas, 'r')
    zodziai = []
    contents = atidarytas.readlines()
    for i in range(len(contents)):
        zodziai.extend(contents[i].split())
    return zodziai
    atidarytas.close()

# Funkcija vieno failo statistikoms kaupti


def SurinktiFailoStatistikas(skaitomas_failas):

# Statistiku kintamieji

    num_lines = 0
    num_words = 0
    num_chars = 0

# Rasomo failo kintamojo sukurimas

    GLOBRESULT.write("\nFAILAS " + str(skaitomas_failas))

    with open(str(skaitomas_failas)) as f:
        GLOBRESULT.write("\nRAIDES faile:")

# Raidziu statistikos isvedimas

        GLOBRESULT.write(str(Counter(
            letter for line in f
            for letter in line.lower()
            if letter in ascii_lowercase)))

# Zodziu statistikos isvedimas

    SkaitytiZodzius(skaitomas_failas)
    list = SkaitytiZodzius(skaitomas_failas)

    global GLOBLIST
    GLOBLIST = GLOBLIST + list
    counts = Counter(list)
    GLOBRESULT.write("\nZODZIAI faile: " + "\n" + str(counts))

# Eiluciu skaiciaus, zodziu skaiciaus,
# simboliu skaiciaus statistiku apdorojimas

    with open(str(skaitomas_failas)) as f:
        for line in f:
            words = line.split()
            num_lines += 1
            num_words += len(words)
            num_chars += len(line)

    global GLOBLINES
    GLOBLINES = GLOBLINES + num_lines
    global GLOBWORDS
    GLOBWORDS = GLOBWORDS + num_words
    global GLOBCHARS
    GLOBCHARS = GLOBCHARS + num_chars

# ...ju surasymas

    GLOBRESULT.write("\nEiluciu skaicius: " + str(num_lines) +
                     "\nZodziu skaicius: " + str(num_words) +
                     "\nSimboliu skaicius: " + str(num_chars) + "\n")

# Funkcija bendrai failu statistikai suvedineti


def BendraStatistika():
    GLOBRESULT.write("\nBENDRA STATISTIKA: ")
    visi_zodziai = Counter(GLOBLIST)
    GLOBRESULT.write("\n" + "Zodziai ir daznis: " + str(visi_zodziai))
    GLOBRESULT.write("\n" + "Eilutes: " + str(GLOBLINES))
    GLOBRESULT.write("\n" + "Zodziai: " + str(GLOBWORDS))
    GLOBRESULT.write("\n" + "Simboliai: " + str(GLOBCHARS))

# Direktorijos nuskaitymas

direktorija = raw_input("Iveskite direktorija: ")
print "IVESTIS PRIIMTA."

print ("Rasti tokie failai direktorijoje " + str(direktorija) + ":")

# Ivestos direktorijos apdorojimas

for file in os.listdir(str(direktorija)):
    if file.endswith(".txt"):
        SurinktiFailoStatistikas(str(file))
        print (str(file))

# Bendros failu statistikos isvedimas

BendraStatistika()

GLOBRESULT.close()
