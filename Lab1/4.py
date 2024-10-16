

def sumaListy(lista : list, element : int = 0):
    suma = 0;
    for x in lista:
        suma += x[element];

    return suma;



def wsadzNajwartosciowszePrzedmiotyWedlugStosunku(listaPrzedmiotow : list, pojemnoscPlecaka : int): # wybiera jak najlzejsze przedmioty o wysokiej wartosci
    for x in range(len(listaPrzedmiotow)-1, -1, -1):
        if(listaPrzedmiotow[x][0] > pojemnoscPlecaka):
            listaPrzedmiotow.pop(x); # usuwam przedmioty ktore nie zmieszcza sie do plecaka

    mapaWagDoWartosci = map(lambda a: (a[1] - a[0])/a[0], listaPrzedmiotow); # (a[1] - a[0])/a[0] - stosunek wagi do wartosci przedmiotu
    mapa = dict();
    i = 0;
    for e in mapaWagDoWartosci:
        mapa[e] = listaPrzedmiotow[i];
        i += 1;

    ostatecznaLista = [];
    while(len(mapa) > 0):
        najwyzszyStosunek = max(mapa.keys());
        if(sumaListy(ostatecznaLista) + mapa[najwyzszyStosunek][0] <= pojemnoscPlecaka):
            ostatecznaLista.append(mapa[najwyzszyStosunek]);
        mapa.pop(najwyzszyStosunek);

    return (sumaListy(ostatecznaLista, 1), ostatecznaLista);


def wsadzNajwartosciowszePrzedmiotyWedlugWartosci(listaPrzedmiotow : list, pojemnoscPlecaka : int): # wybiera przedmioty o najwyzszej wartosci nie zwracajac uwagi na wage
    for x in range(len(listaPrzedmiotow)-1, -1, -1):
        if(listaPrzedmiotow[x][0] > pojemnoscPlecaka):
            listaPrzedmiotow.pop(x); # usuwam przedmioty ktore nie zmieszcza sie do plecaka

    lista = [];
    while(len(listaPrzedmiotow) > 0 and sumaListy(lista) != pojemnoscPlecaka):
        maxWartosc = None;
        for x in listaPrzedmiotow:
            if(maxWartosc is None):
                maxWartosc = x;
            elif(x[1] > maxWartosc[1] or (x[1] == maxWartosc[1] and x[0] < maxWartosc[0])):
                maxWartosc = x;
        if(sumaListy(lista) + maxWartosc[0] <= pojemnoscPlecaka):
            lista.append(maxWartosc);
        listaPrzedmiotow.remove(maxWartosc);

    return (sumaListy(lista, 1), lista);


def porownajObaSposobyZwrocLepszy(listaPrzedmiotow : list, pojemnoscPlecaka : int):
    stosunek = wsadzNajwartosciowszePrzedmiotyWedlugStosunku(listaPrzedmiotow.copy(), pojemnoscPlecaka);
    wartosc = wsadzNajwartosciowszePrzedmiotyWedlugWartosci(listaPrzedmiotow.copy(), pojemnoscPlecaka);
    if(wartosc[0] > stosunek[0]):
        listaPrzedmiotow = wartosc;
    else:
        listaPrzedmiotow = stosunek;

    return  listaPrzedmiotow;






przedmioty = [(12, 3), (1, 56), (4, 4), (23, 9), (2, 8), (320, 999), (9, 21), (15, 18), (39, 41)] # przedmioty[x] == (waga, wartosc)
waga = 40;
print(wsadzNajwartosciowszePrzedmiotyWedlugStosunku(przedmioty.copy(), waga));
print(wsadzNajwartosciowszePrzedmiotyWedlugWartosci(przedmioty.copy(), waga));
print(f"Wybrano: {porownajObaSposobyZwrocLepszy(przedmioty.copy(), waga)}");
print("");
waga = 50;
print(wsadzNajwartosciowszePrzedmiotyWedlugStosunku(przedmioty.copy(), waga));
print(wsadzNajwartosciowszePrzedmiotyWedlugWartosci(przedmioty.copy(), waga));
print(f"Wybrano: {porownajObaSposobyZwrocLepszy(przedmioty.copy(), waga)}");