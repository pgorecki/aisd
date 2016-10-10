# -*- encoding: utf8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Sporządzono na podstawie:
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Dodatkowe ćwiczenia na listach

# D. Dla listy zawierającej liczby, zwróć listę w której wszystkie
# powtórzenia sąsiadujących elementów zostały usunięte,
# np. dla [1, 2, 2, 3] zwróć [1, 2, 3]. Możesz zmodyfikować listę wejściową lub
# utworzyć nową listę.
def usun_powtorzenia(liczby):
    # +++tu wstaw swój kod+++
    return


# E. Dla dwóch posortowanych list wejściowych, stwórz listę wyjściową
# zawierające posortowane elementy z obydwu list. Możesz zmodyfikować listy wejściowe.
# Spróbuj napisać taki algorytm, który zadziała w czasie liniowym, tzn. możesz odczytać
# każdy element z list wejściowych tylko raz.
def zlaczenie_liniowe(lista1, lista2):
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
    print('usun_powtorzenia')
    test(usun_powtorzenia([1, 2, 2, 3]), [1, 2, 3])
    test(usun_powtorzenia([2, 2, 3, 3, 3]), [2, 3])
    test(usun_powtorzenia([]), [])

    print
    print('zlaczenie_liniowe')
    test(zlaczenie_liniowe(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(zlaczenie_liniowe(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(zlaczenie_liniowe(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
    main()
