
def takiSePrzypadek(asc : bool, sElement : int):
    if(sElement == 0 or (sElement == 1 and asc)):
        return not asc;

    return asc;



def porownajTuple(fTuple : tuple, sTuple : tuple, index : int = 0, greater : bool = True):
    if(greater):
        return fTuple[index] > sTuple[index];

    return fTuple[index] < sTuple[index];




def sortujMape(map : dict, element : int = 0, asc : bool = True): # w przypadku takich samych wartosci wybiera lepsza opcje (na podstawie drugiej wartosci)
    if(len(map) < 2):
        return map;
    posortowane = dict();
    sElement = 1;
    if(element == 1):
        sElement = 0;
    while(len(map) > 0):
        najnizszy = None;
        for x in map.keys():
            if(najnizszy is None):
                najnizszy = x;
            elif(porownajTuple(map[najnizszy], map[x], element, asc) or (map[najnizszy][element] == map[x][element] and porownajTuple(map[najnizszy], map[x], sElement, takiSePrzypadek(asc, sElement)))):
                najnizszy = x;

        posortowane[najnizszy] = map.pop(najnizszy);

    return posortowane;


def wybierzZadaniaNaPodstawieCzasu(map : dict, finalList : list = []):
    map = sortujMape(map);
    naPozniej = dict();
    lista = [];
    nagroda = 0;
    repeat = True;
    while(repeat):
        repeat = False;
        for x in map.copy().keys():
            lista.append((x, map[x][0], map[x][1]));
            nagroda += map[x][1];
            for y in map[x][2]:
                if (map.keys().__contains__(y)):
                    naPozniej[y] = map.pop(y);
            if(map.keys().__contains__(x)):
                map.pop(x);
            repeat = True;
            break;

    finalList.append((nagroda, lista));
    if(len(naPozniej) > 1):
        return wybierzZadaniaNaPodstawieCzasu(naPozniej);
    elif(len(naPozniej) > 0):
        for x in naPozniej.keys():
            finalList.append((naPozniej[x][1], [(x, naPozniej[x][0], naPozniej[x][1])]));

    return finalList;





zadania = {
    'A' : (3, 12, ['C', 'F', 'L']),
    'B' : (4, 6, ['C', 'D']),
    'C' : (28, 126, ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L']),
    'D' : (8, 2, ['B', 'C']),
    'E' : (8, 15, ['C']),
    'F' : (1, 4, ['A', 'C', 'L']),
    'G' : (5, 18, ['C', 'I']),
    'H' : (9, 3, ['C']),
    'I' : (5, 19, ['C', 'G']),
    'J' : (4, 11, ['C']),
    'K' : (4, 3, []),
    'L' : (28, 126, ['A', 'C', 'F'])
} # zadania[LITERA] == (czas, nagroda, listaKonfliktow)

lista = wybierzZadaniaNaPodstawieCzasu(zadania);
i = 1;
for x in lista:
    print(f"Lista nr {i}: {x}");
    i += 1;