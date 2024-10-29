import string



class Employee:



    def __init__(self, name : string, age : int, salary : float):
        self.__name = name;
        self.__age = age;
        self._salary = salary;


    def getName(self):
        return self.__name;

    def getAge(self):
        return self.__age;

    def getSalary(self):
        return self._salary;



class EmployeeManager:
    __listaPracownikow = [];

    def getListaPracownikow(self):
        return self.__listaPracownikow;

    def addEmployeeToList(self, employee : Employee):
        self.getListaPracownikow().append(employee);

    def printListaPracownikow(self):
        print(self.getListaPracownikow());

    def usunPracownikowNaPodstawieWieku(self, odWieku : int, doWieku : int):
        lista = self.getListaPracownikow();
        for i in range(len(lista)-1, 0):
            if(lista[i].getAge() > odWieku and lista[i].getAge() < doWieku):
                lista.remove(lista[i]);
    '''od i do jest exclusive'''

    def wyszukajPracownika(self, nazwa : string):
        for x in self.getListaPracownikow():
            if(x.getName() == nazwa):
                return x;

        return None;

    def zmienWynagrodzenie(self, nazwaPracownika : string, noweWynagrodzenie : int):
        pracownik = self.wyszukajPracownika(nazwaPracownika);
        if(pracownik != None):
            pracownik._salary = noweWynagrodzenie;


class FrontendManager(EmployeeManager):



