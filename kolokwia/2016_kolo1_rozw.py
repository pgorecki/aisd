# -*- encoding: utf8 -*-


# zwroc wieksza z liczb x i y
def wieksza(x,y):
    if x > y:
        return x
    return y


# zostaje w domu gdy pada deszcz lub gdy jest wieczór i mam gości
# Napisz funkcję zwracającą True/False w zależności od wartości argumentów (wartości logiczne)
def zostaje_w_domu(pada_deszcz, jest_wieczor, mam_gosci):
    return pada_deszcz or jest_wieczor and mam_gosci


# zwroc True jeżeli x jest liczba parzysta
def czy_parzysta(x):
    return x % 2 == 0


# sprawdź czy słowo jest palindromem (brzmi tak samo czytane od lewej do prawej i od prawej do lewej)
def palindrom(slowo):
    for i in range(len(slowo)//2):
        if slowo[i] != slowo[-i-1]:
            return False
    return True


# Dla danej listy stringów ze slowami zwróć liczbę takich stringów, których długości wynosi 2 lub więcej
# i których pierwszy i ostatni znak jest taki sam.
def zliczanie_stringow(slowa):
    ile = 0
    for slowo in slowa:
        if len(slowo) >= 2 and slowo[0]==slowo[-1]:
            ile += 1
    return ile


# zwróć True jeżeli w tablicu jest więcej liczb ujemnych niż nieujemnych
def wiecej_ujemnych(tablica):
    ujemnych = 0
    dodatnich = 0
    for x in tablica:
        if x < 0:
            ujemnych += 1
        else:
            dodatnich += 1
    return ujemnych > dodatnich


# przepisuj liczby z tablicy wejsciowej do tablicy wyjsciowej
# gdy natrafisz na 14, nie przepisuj jej i zwroc tablice wyjsciową
def przepisz(tablica):
    i = 0
    while tablica[i] != 14:
        i += 1
    return tablica[:i]


# Sprawdź czy wartości w tablicy są posortowanie od największych do najmniejszych
def czy_posortowane(tablica):
    for i in range(len(tablica)-1):
        if tablica[i] < tablica[i+1]:
            return False
    return True


# zwroc True gdy hasło jest bezpieczne, lub False w przeciwnym razie
# bezpieczne hasło zawiera min. 8 znaków, z czego min. 2 znaki alfanumeryczne(a-z),
# min. 2 cyfry, i min. 1 znak specjalny
def bezpieczne_haslo(haslo):
    if len(haslo) < 8:
        return False
    liter = 0
    cyfr = 0
    specjalnych = 0
    for znak in haslo:
        #if znak.isalpha():
        if 'a' <= znak <= 'z' or 'A' <= znak <= 'Z':
            liter += 1
        #elif znak.isdigit():
        elif '0' <= znak <= '9':
            cyfr += 1
        else:
            specjalnych += 1
    return liter>=2 and cyfr>=2 and specjalnych>=1


# zwróć wszystkie liczby w przedziale [start,koniec] podzielne przez 7
# nie będące wielokrotnością 5. Funkcja powinna zwrócić string zawierający
# te liczby, oddzielone przecinkiem (bez spacji), np.: "2002,2009,2016"
def podzielne_7_nie_5(start, koniec):
    liczby = ''
    for i in range(start, koniec+1):
        if i % 7 == 0 and i % 5 != 0:
            #liczby += "%d," % i
            liczby += str(i) + ','
    return liczby[:-1]

    liczby = []
    for i in range(start, koniec+1):
        if i % 7 == 0 and i % 5 != 0:
            #liczby.append(str(i))
            liczby.append(i)
    #return ",".join(liczby)
    return ",".join([str(x) for x in liczby])


# dla tablicy wejsciowej [a1, a2, .., aN] zwroc tablice 2 wymiarowa postaci:
# [[a1, a2, .., aN]
# [a2, .., aN, a1]
# ...
# [aN, ..., a1, a2]]
#
# Przykladowo, dla tablicy [1,2,3] zwróć tablicę [[1,2,3], [2,3,1], [3,1,2]]
def przesuniecia(tab):
    wyniki = []
    # for i in range(len(tab)):
    #     wyniki.append(tab)
    #     tab = tab[1:] + [tab[0]]
    tab2 = tab * 2
    for i in range(len(tab)):
        wyniki.append(tab2[i:i+len(tab)])
    return wyniki


# Z klawiatury usunięto wszystkie klawisze poza tymi, które są niezbędne do
# wpisania tekstu w tekst1. Napisz funkcję, która zwróci True jeżeli tekst w tekst2 da
# się również zapisać przy użyciu takiej wybrakowanej klawiatury. W przeciwnym
# razie zwróć False. Interesują nas tylko klawisze a-z, 0-9. Wielkość liter nie ma znaczenia.
# Przykładowo:
# wybrakowana_klawiatura('ma', 'mama') == True
# wybrakowana_klawiatura('ab', 'abc') == False
# wybrakowana_klawiatura('abc', 'ab') == True
# wybrakowana_klawiatura('ab', 'AB') == True
def wybrakowana_klawiatura(tekst1, tekst2):
    tekst1 = tekst1.lower()
    tekst2 = tekst2.lower()
    for znak in tekst2:
        if znak not in tekst1:
            return False
    return True


# Na stole leżą stosy książek, na pozycji i znajduje się stos wysokości h_i, stosy te zapisano w
# postaci tablicy stosy = [h0, h1, ...]. Sprzątanie stołu polega na usuwaniu stosów od najwyższych
# do najniższych (po uprzątnięciu pozycji i, przyjmij że wysokość stosu w tym miejscu wynosi 0)
# W przypadku stosów o równej wysokości sprzątnięty zostanie ten o mniejszej pozycji
# Zwróć tablicę zawierającą kolejność sprzątanych pozycji.
# Przykładowo, stosy [5,1,2] będą sprzątnięte w kolejności [0, 2, 1]
def sprzatanie(stosy):
    wyniki = []
    while True:
        # szukam max i jego pozycje
        max_v = 0
        max_i = 0
        for i in range(len(stosy)):
            if stosy[i] > max_v:
                max_v = stosy[i]
                max_i = i

        if max_v == 0:
            break
        stosy[max_i] = 0
        wyniki.append(max_i)
    return wyniki


# Dana jest macierz w postaci tablicy 2-wymiarowej
# Zwróć wartość minimalną spośród sum wierszy i kolumn
def najmniejsza_suma(macierz):
    wyniki = []
    # sumy wierszy
    for w in range(len(macierz)):
        suma = 0
        for k in range(len(macierz[0])):
            suma += macierz[w][k]
        wyniki.append(suma)
    # sumy kolumn
    for k in range(len(macierz[0])):
        suma = 0
        for w in range(len(macierz)):
            suma += macierz[w][k]
        wyniki.append(suma)

    return min(wyniki)


# W tablicy znajdują się wyrazy i cyfry. Przejdź kolejno przez elementy tablicy i:
# gdy napotkasz wyraz, to odłóż go na stos
# gdy napotkasz cyfrę to wykonaj działanie z zależności od wartości:
# 0 - sklej 2 wyrazy z wierzchołka stosu, wynik odłóż na stos
# 1 - pobierz wyraz z wierzchołka stosu, przekształć go na wielkie litery (podpowiedź: "abc".upper()), odłóż na stos
# 2 - pobierz wyraz ze stosu, usuń z niego ostatnią literę, wynik odłóż na stos
# zwróć zawartość stosu począwszy od elementu leżącego najbliżej wierzchołka stosu do tego leżącego najgłębiej
def stos_wyrazow(tablica):
    # podpowiedzi:
    # isinstance(1, int) == True
    # isinstance('abc', int) == False
    # "abc".upper() == "ABC"
    from stos import Stack
    s = Stack()
    for element in tablica:
        if isinstance(element, int):
            if element==0:
                s.push(s.pop()+s.pop())
            if element==1:
                s.push(s.pop().upper())
            if element==2:
                s.push(s.pop()[:-1])
        else:
            s.push(element)

    zawartosc = []
    while not s.is_empty():
        zawartosc.append(s.pop())
    return zawartosc


# Oblicz sumę elementów tablicy, przy czym elementem tablicy może być też tablica,
# w takim przypadku policz sumę używając rekurencji
# Przykładowo:
# suma tablicy z elementami [1, [2, 3], 4] wynosi 10
def suma_rekurencyjna(tablica):
    # podpowiedzi:
    # isinstance([1,2,3], list) == True
    # isinstance(5, list) == False
    suma = 0
    for x in tablica:
        if isinstance(x, list):
            suma += suma_rekurencyjna(x)
        else:
            suma += x
    return suma


# W tablicy "cyfry" znajduja sie cyfry w przedziale [1..9], ktore ksiegowa wpisuje przy pomocy klawiatury
# numerycznej o następującym układzie:
# 789
# 456
# 123
# Ksiegowa rozpoczyna wpisywanie cyfr od cyfry[0] i wprowadza kolejne cyfry z tablicy 1 palcem. Palec przesuwa
# się tylko w pionie i w poziomie, z klawisza na klawisz. Oblicz jaką droge pokonuje palec ksiegowej
# przy wpisywaniu wszystkich liczb (przeskok z klawisza na klawisz to odległość = 1). Przykładowo dla:
# palec_ksiegowej([4, 7, 5]) droga ta wynosi z 1 (z klawisza 4 na klawisz 7) + 2 (z klawisza 7 na klawisz 5) = 4.
def palec_ksiegowej(cyfry):
    def manhattan(a,b):
        x1, y1 = a
        x2, y2 = b
        return abs(x1-x2) + abs(y1-y2)

    # współrzędne (x,y) klawiszy
    wsp = {
        7: (0,0),
        8: (1,0),
        9: (2,0),
        4: (0,1),
        5: (1,1),
        6: (2,1),
        1: (0,2),
        2: (1,2),
        3: (2,2),
    }

    suma = 0
    for i in range(len(cyfry)-1):
        c1 = cyfry[i]
        c2 = cyfry[i+1]
        suma += manhattan(wsp[c1], wsp[c2])
    return suma
