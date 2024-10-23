

def najwiekszaLiczba(lista : list):
    najwieksza = None;
    for x in lista:
        liczba = None;
        if(type(x) == list or type(x) == tuple or type == set):
            liczba = najwiekszaLiczba(x);
        elif(type(x) == dict):
            liczba = najwiekszaLiczba(list((dict)(x).values()));
        elif(type(x) != bool and type(x) != str):
            liczba = x;

        if(liczba != None):
            if(najwieksza == None):
                najwieksza = liczba;
            elif(najwieksza < liczba):
                najwieksza = liczba;


    return najwieksza;



def najdluzszyNapis(lista : list):
    najwieksza = None;
    for x in lista:
        naj = None;
        if(type(x) == list or type(x) == tuple or type == set):
            naj = najdluzszyNapis(x);
        elif(type(x) == dict):
            naj = najdluzszyNapis(list((dict)(x).values()));
        elif(type(x) == str):
            naj = x;

        if(naj != None):
            if(najwieksza == None):
                najwieksza = naj;
            elif(len(najwieksza) < len(naj)):
                najwieksza = naj;


    return najwieksza;



def najdluzszaKrotka(lista : list):
    najwieksza = None;
    for x in lista:
        naj = None;
        if(type(x) == list or type == set):
            naj = najdluzszaKrotka(x);
        elif(type(x) == dict):
            naj = najdluzszaKrotka(list(dict(x).values()));
        elif(type(x) == tuple):
            naj = najdluzszaKrotka(list(x));
            if(naj != None):
                if(len(naj) <= len(x)):
                    naj = x;
            else:
                naj = x;


        if(naj != None):
            if(najwieksza == None):
                najwieksza = naj;
            elif(len(najwieksza) < len(naj)):
                najwieksza = naj;


    return najwieksza;



A = [1, "szyszka", {"cos": 5, "tam": 'a'}, 5.5, "bez sensu", 9, True, [False, False, False], (10, 4.5)];

print(najwiekszaLiczba(A));
print(najdluzszyNapis(A));
print(najdluzszaKrotka(A));