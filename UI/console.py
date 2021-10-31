from Domain.obiect import toString
from Logic.CRUD import adaugaObiect, stergeObiect, modificaObiect
from Logic.functionalitati import mutareaTuturorObiectelor, concatenareString, celMaiMarePretLocatii, ordonareDupaPret, \
    sumaPretPerLocatie


def printMenu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("4. Mutarea tuturor obiectelor dintr-o locatie intr-o locatie data")
    print("5. Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.")
    print("6. Determinarea celui mai mare preț pentru fiecare locație.")
    print("7. Ordonarea obiectelor crescător după prețul de achiziție.")
    print("8. Afișarea sumelor prețurilor pentru fiecare locație.")
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


def uiConcatenareString(list):
    string=input("Dati stringul pe care doriti sa il concatenati la descriere la obiectele cu pretul mai mare decat un pret dat: ")
    valoare=int(input("Dati pretul: "))

    lista = concatenareString(string,list,valoare)
    for obiect in lista:
        print(toString(obiect))


def uiCelMaiMarePretLocatii(list):
    rezultat=celMaiMarePretLocatii(list)
    for locatie in rezultat:
        print("Locatia {} are pretul maxim {}".format(locatie,rezultat[locatie]))


def uiOrdonareDupaPret(list):
    lista= ordonareDupaPret(list)
    for obiect in lista:
        print(toString(obiect))


def uiSumaPretPerLocatie(list):
    rezultat=sumaPretPerLocatie(list)
    for locatie in rezultat:
        print("Locatia {} are suma preturilor egala cu {}".format(locatie,rezultat[locatie]))


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
        elif optiune=="5":
            uiConcatenareString(list)
        elif optiune=="6":
            uiCelMaiMarePretLocatii(list)
        elif optiune=="7":
            uiOrdonareDupaPret(list)
        elif optiune=="8":
            uiSumaPretPerLocatie(list)
        elif optiune=="a":
            showAll(list)
        elif optiune=="x":
            break
        else:
            print("Optiune gresita! Reincercati: ")