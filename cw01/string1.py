# -*- encoding: utf8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Sporządzono na podstawie:
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Podstawowe ćwiczenia z manipulacji stringów
# Napisz kod poniższych finkcji. Fukcja main() wywoła testy sprawdzające
# poprawność napisanych przez ciebie funkcji, poprzez ich wywołanie z przykładowymi danymi.
# Gdy twoja funkcja zadziała poprawnie, to zobaczysz 'OK'
# Początkowy kod każdej funkcji, które powinieneś zaimplementować zawiera
# tylko instrukcjce 'return'.
# Dodatkowe ćwiczenia znajdują się w pliku string2.py.


# A. Paczki
# Dla zadanego argumentu wejściowego typu int, zwróć string
# tekst o treści 'Liczba paczek: <liczba>', gdzie <liczba> to przekazana do
# funkcj wartość. W przypadku gdy liczba ta jest równa lub większa od 10
# zamiast przekazanej wartości użyj słowa 'dużo'.
# Przykładowo, paczki(5) zwraca 'Liczba paczek: 5'
# a paczki(23) returns 'Liczba paczek: dużo'
def paczki(count):
    # +++tu wstaw swój kod+++
    return


# B. dwa_konce
# Dla stringa s, zwróć string składający się z 2 pierwszych
# i 2 ostatnich znaków oryginalnego stringa, przykładowo
# dla 'wiosna' zwróć 'wina'.
# W przypadku gdy długość stringa s jest mniejsza niż 2
# zwróć pusty string.
def dwa_konce(s):
    # +++tu wstaw swój kod+++
    return


# C. gwiazdki
# Dla stringa s, zwróć string
# w którym wszystkie wystąpienia pierwszego znaku
# zmienione są na znak '*'. Pierwszy znak w s powinien
# jednak pozostać niezmieniony
# np. dla 'ciecierzyca' zwróć 'cie*ierzy*a'
# Przyjmij, że string s nigdy nie jest pusty.
# Podpowiedź: s.replace(stra, strb) zwraca zmieniony string s
# w którym wszystkie wystąpienia stra zostały zastąpione przez strb.
def gwiazdki(s):
    # +++tu wstaw swój kod+++
    return


# D. miszmasz
# Dla stringów a and b, zwróć jeden string złożony z a i b oddzielonych spacją, tj.
# '<a> <b>', dodatkowo zamień miejscami 2 pierwsze znaki w tych stringach.
# np.
#   'abcd', xyz' -> 'xycd abz'
#   'pies', 'owad' -> 'owies piad'
# Przyjmij, że a i b mają długość minimum 2.
def miszmasz(a, b):
    # +++tu wstaw swój kod+++
    return

#
# NIE MODYFIKUJ PONIŻSZEGO KODU
#

# Poniższa funkcja test() sprawdza czy oczekiwana wartość zwraca się z aktualną
def test(got, expected):
    if got == expected:
        prefix = '    OK '
    else:
        prefix = ' BŁĄÐ '
    print('%s dostałem: %s oczekiwałem: %s' % (prefix, repr(got), repr(expected)))


# Poniższa funkcja main() wywołuje napisane przez ciebie funkcje i sprawdza czy zwróciły one
# poprawne wyniki.
def main():
    print('paczki')
    test(paczki(4), 'Liczba paczek: 4')
    test(paczki(9), 'Liczba paczek: 9')
    test(paczki(10), 'Liczba paczek: dużo')
    test(paczki(99), 'Liczba paczek: dużo')

    print
    print('dwa_konce')
    test(dwa_konce('spring'), 'spng')
    test(dwa_konce('Hello'), 'Helo')
    test(dwa_konce('a'), '')
    test(dwa_konce('xyz'), 'xyyz')

    print
    print('gwiazdki')
    test(gwiazdki('babble'), 'ba**le')
    test(gwiazdki('aardvark'), 'a*rdv*rk')
    test(gwiazdki('google'), 'goo*le')
    test(gwiazdki('donut'), 'donut')

    print
    print('miszmasz')
    test(miszmasz('mix', 'pod'), 'pox mid')
    test(miszmasz('dog', 'dinner'), 'dig donner')
    test(miszmasz('gnash', 'sport'), 'spash gnort')
    test(miszmasz('pezzy', 'firm'), 'fizzy perm')


# Boilerplate uruchamiający funkcję main().
if __name__ == '__main__':
    main()
