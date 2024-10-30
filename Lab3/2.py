import string
import json
from abc import ABC
from abc import abstractmethod



class Employee:
    def __init__(self, name : string, age : int, salary : float):
        self.__name = name;
        self.__age = age;
        self.salary = salary;


    def getName(self):
        return self.__name;

    def getAge(self):
        return self.__age;

    def getSalary(self):
        return self.salary;


class FrontendManager(ABC):

    @abstractmethod
    def printListaPracownikow(self):
        pass

    @abstractmethod
    def getListaPracownikow(self):
        pass

    @abstractmethod
    def addEmployeeToList(self, employee: Employee):
        pass

    @abstractmethod
    def zmienWynagrodzenie(self, nazwaPracownika: string, noweWynagrodzenie: int):
        pass

    @abstractmethod
    def usunPracownikowNaPodstawieWieku(self, odWieku: int, doWieku: int):
        pass



class EmployeeManager(FrontendManager):
    def __init__(self, login : string, haslo : string):
        if(login != "admin" and haslo != "admin"):
            raise ValueError("Niepoprawne haslo lub login");
        self.__listaPracownikow = [];
        self.readFromJsonFile();


    def getListaPracownikow(self):
        return self.__listaPracownikow;

    def addEmployeeToList(self, employee : Employee):
        self.getListaPracownikow().append(employee);
        self.saveToJsonFile();

    def printListaPracownikow(self):
        i = 1;
        for x in self.getListaPracownikow():
            print(f"{i}. Name: {x.getName()}, Age: {x.getAge()}, Salary: {x.getSalary()}");
            i += 1;

    def usunPracownikowNaPodstawieWieku(self, odWieku : int, doWieku : int):
        lista = self.getListaPracownikow();
        for i in range(len(lista)-1, -1, -1):
            if(lista[i].getAge() > odWieku and lista[i].getAge() < doWieku):
                lista.remove(lista[i]);
        self.saveToJsonFile();
    '''odWieku i doWieku jest exclusive'''

    def wyszukajPracownika(self, nazwa : string):
        for x in self.getListaPracownikow():
            if(x.getName() == nazwa):
                return x;

        return None;

    def zmienWynagrodzenie(self, nazwaPracownika : string, noweWynagrodzenie : int):
        pracownik = self.wyszukajPracownika(nazwaPracownika);
        if(pracownik != None):
            pracownik.salary = noweWynagrodzenie;
        self.saveToJsonFile();


    def saveToJsonFile(self):
        forJson = [];
        for x in self.getListaPracownikow():
            forJson.append(json.dumps({
                "name": x.getName(),
                "age": x.getAge(),
                "salary": x.getSalary()
            }));
        f = open("dane.json", "w");
        f.write(json.dumps(forJson));
        f.close();

    def readFromJsonFile(self):
        f = open("dane.json", "r");
        jsonStr = f.read();
        jsonArr = json.loads(jsonStr);
        for x in jsonArr:
            employee = json.loads(x);
            self.getListaPracownikow().append(Employee(employee["name"], employee["age"], employee["salary"]));
        f.close();





manager = EmployeeManager("admin", "admin");
#manager.addEmployeeToList(Employee("Ukasz Fryc", 22, 20.0));
#manager.addEmployeeToList(Employee("Frycasz Uk", 44, 2000.30));
#manager.addEmployeeToList(Employee("Ktos Tam", 28, 4462.0));


employee = manager.wyszukajPracownika("Ktos Tam");
if(employee != None):
    print(f"Znaleziono pracownika: {employee.getName()}, lat {employee.getAge()}, ktory zarabia {employee.getSalary()}zl");
else:
    print("Nie znaleziono pracownika");

manager.printListaPracownikow();
manager.usunPracownikowNaPodstawieWieku(10, 29);
manager.printListaPracownikow();

employee = manager.wyszukajPracownika("Ktos Tam");
if(employee != None):
    print(f"Znaleziono pracownika: {employee.getName()}, lat {employee.getAge()}, ktory zarabia {employee.getSalary()}zl");
else:
    print("Nie znaleziono pracownika");

