def sumaCzasuOczekiwania(lista : list):
    czasy = [];
    for zadanie in lista:
        czasy.append(zadanie[0]);

    return sum(czasy);



def najkrotszeNajpierw(listaZadan : list):
    krotkie = [];
    while len(listaZadan) > 0:
        czas = None;
        for zadanie in listaZadan:
            if czas is None:
                czas = zadanie;
            elif zadanie[0] < czas[0]:
                czas = zadanie;
            elif zadanie[0] == czas[0]:
                if zadanie[1] > czas[1]:
                    czas = zadanie;
        krotkie.append(czas);
        listaZadan.remove(czas);

    return (krotkie, sumaCzasuOczekiwania(krotkie));


def najlepszeNajpierw(listaZadan : list):
    najlepsze = sorted(map(lambda a : a[1] - a[0], listaZadan), reverse= True);
    """ rozwiazanie bez uzywania map
        while len(listaZadan) > 0:
        dobre = None;
        for zadanie in listaZadan:
            if dobre is None:
                dobre = zadanie;
            elif zadanie[1] - zadanie[0] > dobre[1] - dobre[0]:
                dobre = zadanie;
        najlepsze.append(dobre);
        listaZadan.remove(dobre);
    """
    lista = [];
    for element in najlepsze:
        for zadanie in listaZadan:
            if(zadanie[1] - zadanie[0] == element):
                lista.append(zadanie);
                break;

    return (lista, sumaCzasuOczekiwania(lista));




zadania = [(12, 6), (2, 1), (1, 5), (4, 4), (7, 8), (26, 97), (5, 1), (2, 4)]; # zadania[x] == (czas, nagroda)
print(najkrotszeNajpierw(zadania.copy())); # troche dziwne polecenie bo niezaleznie od kolejnosci wykonywania zadan zawsze bedzie ten sam calkowity czas oczekiwania
print(najlepszeNajpierw(zadania.copy())); # zadania ktore daja najwieksza nagrode za najkrotszy czas sa pierwsze
