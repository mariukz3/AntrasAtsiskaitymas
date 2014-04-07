from string import ascii_lowercase
from collections import Counter
import glob
import os

# Globalus kintamieji bendrai statistikai vesti

glob_list = []
glob_lines = 0
glob_words = 0
glob_chars = 0

# Atidaromas statistiku kaupimo failas

glob_result = open('STATISTIKA.txt', 'w')

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

    glob_result.write("\nFAILAS " + str(skaitomas_failas))

    with open(str(skaitomas_failas)) as f:
        glob_result.write("\nRAIDES faile:")

# Raidziu statistikos isvedimas

        glob_result.write(str(Counter(
            letter for line in f
            for letter in line.lower()
            if letter in ascii_lowercase)))

# Zodziu statistikos isvedimas

    SkaitytiZodzius(skaitomas_failas)
    list = SkaitytiZodzius(skaitomas_failas)

    global glob_list
    glob_list = glob_list + list
    counts = Counter(list)
    glob_result.write("\nZODZIAI faile: " + "\n" + str(counts))

# Eiluciu skaiciaus, zodziu skaiciaus,
# simboliu skaiciaus statistiku apdorojimas

    with open(str(skaitomas_failas)) as f:
        for line in f:
            words = line.split()
            num_lines += 1
            num_words += len(words)
            num_chars += len(line)

    global glob_lines
    glob_lines = glob_lines + num_lines
    global glob_words
    glob_words = glob_words + num_words
    global glob_chars
    glob_chars = glob_chars + num_chars

# ...ju surasymas

    glob_result.write("\nEiluciu skaicius: " + str(num_lines) +
                     "\nZodziu skaicius: " + str(num_words) +
                     "\nSimboliu skaicius: " + str(num_chars) + "\n")

# Funkcija bendrai failu statistikai suvedineti


def BendraStatistika():
    glob_result.write("\nBENDRA STATISTIKA: ")
    visi_zodziai = Counter(glob_list)
    glob_result.write("\n" + "Zodziai ir daznis: " + str(visi_zodziai))
    glob_result.write("\n" + "Eilutes: " + str(glob_lines))
    glob_result.write("\n" + "Zodziai: " + str(glob_words))
    glob_result.write("\n" + "Simboliai: " + str(glob_chars))

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

glob_result.close()
