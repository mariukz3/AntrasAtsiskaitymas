def SutvarkytiFaila(SkaitomasFailas, RezultatuFailas):
    
    num_lines = 0
    num_words = 0
    num_chars = 0

    with open(str(SkaitomasFailas)) as f:
        result.write("Raidziu yra:")
        result.write(str(Counter(
            letter for line in f
            for letter in line.lower()
            if letter in ascii_lowercase)))
