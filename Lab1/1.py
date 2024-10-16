
def podzielPaczki(listaWag : list, maxWaga : int):
    for waga in listaWag:
        if(waga > maxWaga):
            raise ValueError(f"Paczka o wadze {waga} przekracza maksymalną wagę, czyli {maxWaga}kg");

    listaWag.sort(reverse= True);
    #print(listaWag);
    kursy = [];
    while len(listaWag) > 0:
        kurs = [];
        listaWagKopia = listaWag.copy();
        for waga in listaWagKopia:
            #print(f"waga: {waga} i suma kursu: {sum(kurs)}");
            if sum(kurs) + waga <= maxWaga:
                kurs.append(waga);
                listaWag.remove(waga);
            if sum(kurs) == maxWaga:
                break;
        kursy.append(kurs);

    return (len(kursy), kursy);


wagi = [10, 15, 7, 20, 5, 8, 10];
print(podzielPaczki(wagi, 25));

