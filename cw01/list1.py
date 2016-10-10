# -*- encoding: utf8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Sporządzono na podstawie:
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Podstawowe ćwiczenia na listach
# Napisz kod poniższych finkcji. Fukcja main() wywoła testy sprawdzające
# poprawność napisanych przez ciebie funkcji, poprzez ich wywołanie z przykładowymi danymi.
# Gdy twoja funkcja zadziała poprawnie, to zobaczysz 'OK'
# Początkowy kod każdej funkcji, które powinieneś zaimplementować zawiera
# tylko instrukcjce 'return'.
# Dodatkowe ćwiczenia znajdują się w pliku list2.py.

# A. match_ends
# Dla danej listy stringów, zwróć liczbę takich stringów których długości wynosi 2 lub więcej
# i których pierwszy i ostatni znak jest taki sam.
# Note: Python nie wspiera operatora ++, zamiast tego możesz użyć operatora +=.
def zliczanie(slowa):
    # +++tu wstaw swój kod+++
    return


# B. pierwszy_x
# Dla danej listy stringów, return listę posortowaną,
# ale w taki sposón, że stringi zaczynające się na 'x' będą na liscie pierwsze.
# Np. dla ['mix', 'xyz', 'aproksymacja', 'xero', 'adwokat'] zwróć
# ['xero', 'xyz', 'adwokat', 'aproksymacja', 'mix']
# Podpowiedź: stwórz 2 listy i posortuj je osobno.
def pierwszy_x(slowa):
    # +++tu wstaw swój kod+++
    return


# C. posortuj_ostatni
# Dla danej listy of niepustych krotek, zwróć listę posortowaną wg. ostatniego
# elementu w każdej krotce.
# Np. dla [(1, 7), (1, 3), (3, 4, 5), (2, 2)] zwróć
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Podpowiedź: do funkcji sortującej przekaż przez argument key= funkcję sortującą, która zwracać będzie
# ostatni element krotki.
def sortuj_ostatni(krotki):
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
  print('zliczanie')
  test(zliczanie(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  test(zliczanie(['', 'x', 'xy', 'xyx', 'xx']), 2)
  test(zliczanie(['aaa', 'be', 'abc', 'hello']), 1)
  test(zliczanie([]), 0)

  print
  print('pierwszy_x')
  test(pierwszy_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(pierwszy_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(pierwszy_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])


  print
  print('sortuj_ostatni')
  test(sortuj_ostatni([(1, 3), (3, 2), (2, 1)]),
       [(2, 1), (3, 2), (1, 3)])
  test(sortuj_ostatni([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
  test(sortuj_ostatni([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
  main()
