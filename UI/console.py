from Domain.obiect import toString
from Logic.CRUD import adaugaObiect, stergeObiect, modificaObiect
from Logic.functionalitati import mutareaTuturorObiectelor


def printMenu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("4. Mutarea tuturor obiectelor dintr-o locatie intr-o locatie data")
    print("a. Afisare obiecte")
    print("x. Iesire")


def uiAdaugaObiect(list):
    id= input("Dati id-ul: ")
    nume = input("Dati numele obiectului: ")
    descriere= input("Dati descrierea obiectului: ")
    pretachizitie=float(input("Dati pretul de achizitie: "))
    locatie= input("Dati locatia obiectului: ")
    return adaugaObiect(id,nume,descriere,pretachizitie,locatie,list)


def uiStergeObiect(list):
    id= input("Dati id-ul obiectului de sters: ")
    return stergeObiect(id,list)


def uiModificaObiect(list):
    id = input("Dati id-ul obiectului de modificat: ")
    nume = input("Dati noul nume al obiectului: ")
    descriere = input("Dati noua descriere a obiectului: ")
    pretachizitie = float(input("Dati noul pret de achizitie: "))
    locatie = input("Dati noua locati a obiectului: ")

    return modificaObiect(id,nume,descriere,pretachizitie,locatie,list)


def showAll(list):
    for obiect in list:
        print(toString(obiect))


def uiMutareObiecte(list):
    loc=input("Dati locatia in care vreti sa fie mutate toate obiectele: ")
    return mutareaTuturorObiectelor(loc,list)


def runMenu(list):
    while True:
        printMenu()
        optiune=input("Dati optiunea: ")

        if optiune=="1":
            list=uiAdaugaObiect(list)
        elif optiune=="2":
            list=uiStergeObiect(list)
        elif optiune=="3":
            list=uiModificaObiect(list)
        elif optiune=="4":
            list=uiMutareObiecte(list)
        elif optiune=="a":
            showAll(list)
        elif optiune=="x":
            break
        else:
            print("Optiune gresita! Reincercati: ")