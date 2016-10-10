# -*- encoding: utf8 -*-

# W przypadku błędu:
# SyntaxError: Non-ASCII character ... in file ... zmień kodowanie w pierwszej linii


# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Sporządzono na podstawie:
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Dodatkowe ćwiczenia z manipulacji stringami

# D. zdrobnienie
# Dla danego stringa, którego długość wynosi minimu 3,
# dodaj 'ek' na jego końcu.
# W przypadku gdy string już ma na końcu 'ek', zamień `ek`
# na 'eczek'
# Gdy string ma mniej niż 3 znaki, to nie modyfikuj go.
def zdrobnienie(s):
    # +++tu wstaw swój kod+++
    return


# E. not_bad
# Dla danego stringa, znajdź pierwsze wystąpienie podciągu
# 'not' oraz 'bad'. Jeżeli 'not' poprzedza 'bad', zamień cały
# podciąg 'not'...'bad' na 'good'.
# Zwróć zmodyfikowany string.
# Np. dla 'This dinner is not that bad!' zwróć:
# 'This dinner is good!'
def not_bad(s):
    # +++tu wstaw swój kod+++
    return


# F. polowki
# Rozważ podział stringa na 2 połowy.
# Jeżeli stringa nie da się podzielić na 2 połowy o tej samej długości,
# to pierwsza połowa powinna być dłuższa od drugiej.
# Przykładowo, dla 'abcde', pierwsza połowa to 'abc', druga połowa to 'de'.
# Dla 2 stringów, a and b, zwróć nowy string powstały przez złączenie pierwszych połówek,
# a następnie  drugich połówek.
# Np. dla a='123', b='abcd' zwróć '12ab3cd'
def polowki(a, b):
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
    print('zdrobnienie')
    test(zdrobnienie('pies'), 'piesek')
    test(zdrobnienie('domek'), 'domeczek')
    test(zdrobnienie('ul'), 'ul')

    print
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print('polowki')
    test(polowki('abcd', 'xy'), 'abxcdy')
    test(polowki('abcde', 'xyz'), 'abcxydez')
    test(polowki('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
    main()
