


def sumaListyKrotek(lista: list, element: int = 0):
    suma = 0
    for x in lista:
        suma += x[element]

    return suma


# wybiera jak najlzejsze przedmioty o wysokiej wartosci
def wybierzNajwartosciowszePrzedmiotyWedlugStosunku(listaPrzedmiotow: list, pojemnoscPlecaka: int):
    kopia = listaPrzedmiotow.copy()
    for x in range(len(kopia)-1, -1, -1):
        if kopia[x][0] > pojemnoscPlecaka:
            kopia.pop(x)  # odrzuca przedmioty, ktorych waga jest wieksza niż pojemnosc plecaka

    mapaWagDoWartosci = map(lambda a: a[1]/a[0], kopia)  # a[1]/a[0] - stosunek wartosci do wagi przedmiotu
    mapa = dict()
    i = 0
    for e in mapaWagDoWartosci:
        # rozne przedmioty moga miec taki sam stosunek wartosci do wagi, dlatego przechowuje je w liscie
        if(mapa.keys().__contains__(e)):
            mapa[e].append(kopia[i])
        else:
            mapa[e] = [kopia[i]]

        i += 1

    zapelnienie = 0
    ostatecznaLista = []
    # sortuje klucze i wartosci slownika, aby wybierac najlepsze opcje
    for stosunek in sorted(mapa.keys(), reverse=True):
        # lista elementow jest sortowana na podstawie wartosci
        for element in sorted(mapa[stosunek], key=lambda f: f[1], reverse=True):
            if zapelnienie + element[0] > pojemnoscPlecaka:
                continue
            else:
                ostatecznaLista.append(element)
                zapelnienie += element[0]
                if zapelnienie == pojemnoscPlecaka:
                    break  # unikniecie niepotrzebnych obliczen po zapelnieniu plecaka

    return sumaListyKrotek(ostatecznaLista, 1), ostatecznaLista


# przedmioty[x] == (waga, wartosc)
przedmioty = [(12, 3), (1, 56), (4, 4), (23, 9), (2, 8), (320, 999), (9, 21), (6, 6), (39, 41)]
waga = 40
print(wybierzNajwartosciowszePrzedmiotyWedlugStosunku(przedmioty, waga))
