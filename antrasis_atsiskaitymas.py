from string import ascii_lowercase
from collections import Counter
import glob

#Globalus kintamieji bendrai statistikai kaupti

GLOBLINES = 0
GLOBWORDS = 0
GLOBCHARS = 0

#Funkcija vieno failo statistikoms kaupti


def SurinktiFailoStatistikas(SkaitomasFailas, RezultatuFailas):

#Statistiku kintamieji

    num_lines = 0
    num_words = 0
    num_chars = 0

#Rasomo failo kintamojo sukurimas

    result = open(RezultatuFailas, 'w')

#Raidziu tipo ir ju pasikartojimo daznumo algoritmas

    with open(str(SkaitomasFailas)) as f:
        result.write("Raidziu yra:")

#Raidziu statistikos isvedimas

        result.write(str(Counter(
            letter for line in f
            for letter in line.lower()
            if letter in ascii_lowercase)))

#Eiluciu skaiciaus, zodziu skaiciaus,
#simboliu skaiciaus statistiku apdorojimas

    with open(str(SkaitomasFailas)) as f:
        for line in f:
            words = line.split()
            num_lines += 1
            num_words += len(words)
            num_chars += len(line)

#...ju irasymas i atskira faila ir jo uzdarymas

    result.write('\nEiluciu skaicius:')
    result.write(str(num_lines))
    result.write('\nZodziu skaicius:')
    result.write(str(num_words))
    result.write('\nSimboliu skaicius:')
    result.write(str(num_chars))
    result.close()

#Globalios statistikos kintamuju apdorojimas

    global GLOBLINES
    GLOBLINES = GLOBLINES + num_lines
    global GLOBWORDS
    GLOBWORDS = GLOBWORDS + num_words
    global GLOBCHARS
    GLOBCHARS = GLOBCHARS + num_chars

    result.close()

#Funkcija sujungti visiems failu tekstams i viena


def SujungtiFailus(RezultatuFailas):

#Kintamasis atskirti tik fialus, prasidedancius
#su Read + simbolis kiekvieno identifikacijai

    read_files = glob.glob('Read*.txt')

#Bendro teksto rasymo algoritmas

    with open(str(RezultatuFailas), "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())

#Funkcija ivesti bendrai visu failu statistikai
#i atskira faila (globalus kintamieji)


def SurinktiFailuStatistikas(RezultatuFailas):

#Iseities failo kintamasis result

    result = open(RezultatuFailas, 'w')

#Irasymo ir uzdarymo metodai

    result.write('\nBendras failu eiluciu skaicius:')
    result.write(str(GLOBLINES))
    result.write('\nBendras failu zodziu skaicius:')
    result.write(str(GLOBWORDS))
    result.write('\nBendras failu simboliu skaicius:')
    result.write(str(GLOBCHARS))
    result.close()

#Statistiku isvedimas

SurinktiFailoStatistikas('Read1.txt', 'Statistika1.txt')
SurinktiFailoStatistikas('Read2.txt', 'Statistika2.txt')
SurinktiFailoStatistikas('Read3.txt', 'Statistika3.txt')
SujungtiFailus('BendrasTekstas.txt')
SurinktiFailuStatistikas('VisuFailuBendraStatistika')
SurinktiFailoStatistikas('BendrasTekstas.txt', 'BendraStatistika.txt')
