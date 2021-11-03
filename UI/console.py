from Domain.obiect import toString, getNume, getDescriere, getPretachizitie, getLocatie
from Logic.CRUD import adaugaObiect, stergeObiect, modificaObiect, getById
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
    print("u. Undo")
    print("a. Afisare obiecte")
    print("x. Iesire")


def uiAdaugaObiect(list,undoOperations):
    try:
        id= input("Dati id-ul: ")
        nume = input("Dati numele obiectului: ")
        descriere= input("Dati descrierea obiectului: ")
        pretachizitie=float(input("Dati pretul de achizitie: "))
        locatie= input("Dati locatia obiectului: ")

        rezultat = adaugaObiect(id,nume,descriere,pretachizitie,locatie,list)
        undoOperations.append(lambda : stergeObiect(id,rezultat))
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return list

def uiStergeObiect(list,undoOperations):
    try:
        id= input("Dati id-ul obiectului de sters: ")
        rezultat = stergeObiect(id,list)
        obiectNou=getById(id,list)
        undoOperations.append(lambda : adaugaObiect(
            id,
            getNume(obiectNou),
            getDescriere(obiectNou),
            getPretachizitie(obiectNou),
            getLocatie(obiectNou),
            rezultat
        ))
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return list


def uiModificaObiect(list,undoOperations):
    try:
        id = input("Dati id-ul obiectului de modificat: ")
        nume = input("Dati noul nume al obiectului: ")
        descriere = input("Dati noua descriere a obiectului: ")
        pretachizitie = float(input("Dati noul pret de achizitie: "))
        locatie = input("Dati noua locati a obiectului: ")

        rezultat = modificaObiect(id,nume,descriere,pretachizitie,locatie,list)
        obiectVechi=getById(id,list)
        undoOperations.append(lambda :modificaObiect(
            id,
            getNume(obiectVechi),
            getDescriere(obiectVechi),
            getPretachizitie(obiectVechi),
            getLocatie(obiectVechi),
            rezultat
        ))
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return list


def showAll(list):
    for obiect in list:
        print(toString(obiect))


def uiMutareObiecte(list):
    try:
        loc=input("Dati locatia din care vreti sa fie mutate toate obiectele: ")
        if len(loc) < 4 or len(loc) > 4:
            raise ValueError("Locatia trebuia sa aiba exact 4 litere.")
        loc1=input("Dati locatia in care vreti sa fie mutate toate obiectele din locatia data anterior: ")
        if len(loc1) < 4 or len(loc1) > 4:
            raise ValueError("Locatia trebuia sa aiba exact 4 litere.")

        return mutareaTuturorObiectelor(loc,list,loc1)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return list


def uiConcatenareString(list):
    try:
        string=input("Dati stringul pe care doriti sa il concatenati la descriere la obiectele cu pretul mai mare decat un pret dat: ")
        valoare=float(input("Dati pretul: "))

        return concatenareString(string,list,valoare)

    except ValueError as ve:
        print("Eroare {}".format(ve))
        return list



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
    undoOperations=[]
    while True:
        printMenu()
        optiune=input("Dati optiunea: ")

        if optiune=="1":
            list=uiAdaugaObiect(list,undoOperations)
        elif optiune=="2":
            list=uiStergeObiect(list,undoOperations)
        elif optiune=="3":
            list=uiModificaObiect(list,undoOperations)
        elif optiune=="4":
            list=uiMutareObiecte(list)
        elif optiune=="5":
            list=uiConcatenareString(list)
        elif optiune=="6":
            uiCelMaiMarePretLocatii(list)
        elif optiune=="7":
            uiOrdonareDupaPret(list)
        elif optiune=="8":
            uiSumaPretPerLocatie(list)
        elif optiune=="u":
            if len(undoOperations)>0:
                list= undoOperations.pop()()
        elif optiune=="a":
            showAll(list)
        elif optiune=="x":
            break
        else:
            print("Optiune gresita! Reincercati: ")