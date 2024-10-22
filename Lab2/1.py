import string


def zrobListeSlow(text : string, oddzielacze : set, wyfiltruj : set):
    listaSlow = [];
    slowo = "";
    for x in filter(lambda x: not wyfiltruj.__contains__(x), text):
        if(slowo == ""):
            if(not oddzielacze.__contains__(x)):
                slowo += x;
        else:
            if(oddzielacze.__contains__(x)):
                listaSlow.append(slowo);
                slowo = "";
            else:
                slowo += x;

    listaSlow.append(slowo);

    return listaSlow;




def liczSlowaZdaniaAkapity(text : string):
    odejmowanie = len(list(filter(lambda x: x == '-', text))); # pauzy zostawiaja podwojna spacje i liczy mi 2 slowa
    liczbaSlow = len(list(filter(lambda x: x == ' ', filter(lambda y: y != '-', text)))) - odejmowanie;
    liczbaZdan = len(list(filter(lambda x: x=='.', text)));
    liczbaAkapitow = len(list(filter(lambda x: x == '\n', text)));

    return (liczbaSlow, liczbaZdan, liczbaAkapitow);



def najczesciejWystSlowa(text : string):
    stopWords = {"i", "a", "do", "od", 'w', 'na', 'jest', 'z', 'się'};
    listaSlow = zrobListeSlow(text, {' ', '\n'}, {'-'});
    slownik = dict();
    for x in listaSlow:
        if(stopWords.__contains__(x)):
            continue;
        if(not slownik.keys().__contains__(x)):
            slownik[x] = 1;
        else:
            slownik[x] += 1;

    wynik = [];
    while(len(wynik) < 3):
        najwyzsza = ('', 0);
        for x in slownik.keys():
            if(slownik[x] > najwyzsza[1]):
                najwyzsza = (x, slownik[x]);
        wynik.append(najwyzsza);
        slownik.pop(najwyzsza[0]);

    return wynik;



def transformujWyrazy(text : string):
    listaSlow = zrobListeSlow(text, {' '}, set());
    slowo = "";
    for x in listaSlow:
        if(x[0] == 'a' or x[0] == 'A'):
            x = x[::-1];
        slowo += x + " ";


    return slowo;








artykul = ("Algorytm - skończony ciąg jasno zdefiniowanych czynności koniecznych do wykonania pewnego rodzaju zadań, sposób postępowania prowadzący do rozwiązania problemu. Można go przedstawić na schemacie blokowym. \n"
           "Słowo algorytm pochodzi od łacińskiego słowa algorithmus, oznaczającego wykonywanie działań przy pomocy liczb arabskich (w odróżnieniu od abacism - przy pomocy abakusa), które z kolei wzięło się od nazwy Algoritmi, zlatynizowanej wersji nazwiska al-Chwarizmi Abu Abdullaha Muhammada ibn Musy al-Chuwarizmiego, matematyka perskiego z IX wieku. \n"
           "Zadaniem algorytmu jest przeprowadzenie systemu z pewnego stanu początkowego do pożądanego stanu końcowego. Badaniem algorytmów zajmuje się algorytmika. Algorytm może zostać zaimplementowany w postaci programu komputerowego. \n"
           "Jako przykład stosowanego w życiu codziennym algorytmu podaje się często przepis kulinarny. Dla przykładu, aby ugotować bigos, należy w określonej kolejności oraz odstępach czasowych (imperatyw czasowy) dodawać właściwe rodzaje kapusty i innych składników. Może istnieć kilka różnych przepisów dających na końcu bardzo podobną potrawę. Przykład ten ma wyłącznie charakter poglądowy, ponieważ język przepisów kulinarnych nie został jasno zdefiniowany. Algorytmy zwykle formułowane są w sposób ścisły w oparciu o język matematyki. W niektórych krajach (między innymi Stanach Zjednoczonych) algorytmy mogą zostać opatentowane, jeżeli zostaną zaimplementowane w jakimś praktycznym celu. Przeciwnicy tego podejścia twierdzą, że patentowanie algorytmów spowalnia rozwój informatyki, bo jeden producent może uzyskać monopol na pisanie oprogramowania tworzącego pewne typy plików (jak było to w przypadku GIF). Wiele koncernów komputerowych prowadzi między sobą spory prawne dotyczące praw własności do niektórych patentów. Kontrargumentem zwolenników patentów na oprogramowanie jest prawo własności intelektualnej (którą jest na przykład utwór muzyczny, będący wytworem intelektu i pracy muzyka), zakładające, że program jest intelektualną własnością twórcy.");


print(liczSlowaZdaniaAkapity(artykul));
print(najczesciejWystSlowa(artykul));
print(transformujWyrazy(artykul));