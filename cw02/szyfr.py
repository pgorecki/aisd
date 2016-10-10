# -*- encoding: utf8 -*-

# Poniżej znajduje się funkcja szyfrująca wiadomości
# szyfrem gaderypoluki (więcej informacji tutaj: https://pl.wikipedia.org/wiki/Gaderypoluki)
# upewnij się, że funkcja działa poprawnie

def gaderypoluki(wiadomosc):
    szyfr = ''
    for i in range(len(wiadomosc)):
        if wiadomosc[i] == 'g':
            szyfr += 'a'
        elif wiadomosc[i] == 'a':
            szyfr += 'g'
        elif wiadomosc[i] == 'd':
            szyfr += 'e'
        elif wiadomosc[i] == 'e':
            szyfr += 'd'
        elif wiadomosc[i] == 'r':
            szyfr += 'y'
        elif wiadomosc[i] == 'y':
            szyfr += 'r'
        elif wiadomosc[i] == 'p':
            szyfr += 'o'
        elif wiadomosc[i] == 'o':
            szyfr += 'p'
        elif wiadomosc[i] == 'l':
            szyfr += 'u'
        elif wiadomosc[i] == 'u':
            szyfr += 'l'
        elif wiadomosc[i] == 'k':
            szyfr += 'i'
        elif wiadomosc[i] == 'i':
            szyfr += 'k'

    return szyfr

