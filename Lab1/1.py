
def podzielPaczki(listaWag, maxWaga):
    for waga in listaWag:
        if(waga > maxWaga):
            raise ValueError(f"Paczka o wadze {waga} przekracza maksymalną wagę, czyli {maxWaga}kg");

    wagiSort = sorted(listaWag, reverse = True);
    kursy = [];
    while len(wagiSort) > 0:
        kurs = [];
        for waga in wagiSort:
            if sum(start= 0, __iterable= kurs) + waga <= maxWaga:
                kurs.append(waga);
                wagiSort.remove(waga);
            if sum(kurs) == maxWaga:
                break;
        kursy.append(kurs);

    return (len(kursy), kursy);


wagi = [10, 15, 7, 20, 5, 8, 10];
maxWaga = 25;
print(podzielPaczki(wagi, maxWaga)); #nie wiem czemu sie wywala przy ostatnim, nie dodaje 8 do 7

