from Domain.obiect import getId, getNume, getDescriere, getPretachizitie, getLocatie
from Logic.CRUD import adaugaObiect
from Logic.functionalitati import mutareaTuturorObiectelor, concatenareString, celMaiMarePretLocatii, ordonareDupaPret, \
    sumaPretPerLocatie


def testMutareaTuturorObiectelor():
    list = []
    list = adaugaObiect("1", "telefon", "iphone", 4000, "Cluj", list)
    list = adaugaObiect("2", "carte", "programare", 50, "Arad", list)
    list = adaugaObiect("3", "carte", "desenat", 30, "Arad", list)
    list = adaugaObiect("4", "telefon", "samsung", 3500, "Iasi", list)

    list=mutareaTuturorObiectelor("Arad",list,"Cluj")

    assert getId(list[0]) == "1"
    assert getNume(list[0]) == "telefon"
    assert getDescriere(list[0]) == "iphone"
    assert getPretachizitie(list[0]) == 4000
    assert getLocatie(list[0]) == "Cluj"

    assert getId(list[1]) == "2"
    assert getNume(list[1]) == "carte"
    assert getDescriere(list[1]) == "programare"
    assert getPretachizitie(list[1]) == 50
    assert getLocatie(list[1]) == "Cluj"

    assert getId(list[2]) == "3"
    assert getNume(list[2]) == "carte"
    assert getDescriere(list[2]) == "desenat"
    assert getPretachizitie(list[2]) == 30
    assert getLocatie(list[2]) == "Cluj"

    assert getId(list[3]) == "4"
    assert getNume(list[3]) == "telefon"
    assert getDescriere(list[3]) == "samsung"
    assert getPretachizitie(list[3]) == 3500
    assert getLocatie(list[3]) == "Iasi"

def testConcatenareString():
    list = []
    list = adaugaObiect("1", "telefon", "iphone", 4000, "Cluj", list)
    list = adaugaObiect("2", "carte", "programare", 50, "Arad", list)
    list = adaugaObiect("3", "carte", "desenat", 30, "Arad", list)
    list = adaugaObiect("4", "telefon", "samsung", 3500, "Iasi", list)

    list = concatenareString("perfect",list,50)

    assert getId(list[0]) == "1"
    assert getNume(list[0]) == "telefon"
    assert getDescriere(list[0]) == "iphone perfect"
    assert getPretachizitie(list[0]) == 4000
    assert getLocatie(list[0]) == "Cluj"

    assert getId(list[1]) == "2"
    assert getNume(list[1]) == "carte"
    assert getDescriere(list[1]) == "programare"
    assert getPretachizitie(list[1]) == 50
    assert getLocatie(list[1]) == "Arad"

    assert getId(list[2]) == "3"
    assert getNume(list[2]) == "carte"
    assert getDescriere(list[2]) == "desenat"
    assert getPretachizitie(list[2]) == 30
    assert getLocatie(list[2]) == "Arad"

    assert getId(list[3]) == "4"
    assert getNume(list[3]) == "telefon"
    assert getDescriere(list[3]) == "samsung perfect"
    assert getPretachizitie(list[3]) == 3500
    assert getLocatie(list[3]) == "Iasi"

def testCelMaiMarePretLocatii():
    list = []
    list = adaugaObiect("1", "telefon", "iphone", 4000, "Cluj", list)
    list = adaugaObiect("2", "carte", "programare", 50, "Arad", list)
    list = adaugaObiect("3", "carte", "desenat", 30, "Arad", list)
    list = adaugaObiect("4", "telefon", "samsung", 3500, "Cluj", list)

    rezultat=celMaiMarePretLocatii(list)
    assert len(rezultat)==2
    assert rezultat["Cluj"]==4000
    assert rezultat["Arad"]==50

def testOrdonareDupaPret():
    list = []
    list = adaugaObiect("1", "telefon", "iphone", 4000, "Cluj", list)
    list = adaugaObiect("2", "carte", "programare", 50, "Arad", list)
    list = adaugaObiect("3", "carte", "desenat", 30, "Arad", list)
    list = adaugaObiect("4", "telefon", "samsung", 3500, "Cluj", list)

    rezultat=ordonareDupaPret(list)

    assert getId(rezultat[0]) == "3"
    assert getId(rezultat[1]) == "2"
    assert getId(rezultat[2]) == "4"
    assert getId(rezultat[3]) == "1"

def testSumaPretPerLocatie():
    list=[]

    list = adaugaObiect("1", "telefon", "iphone", 4000, "Cluj", list)
    list = adaugaObiect("2", "carte", "programare", 50, "Arad", list)
    list = adaugaObiect("3", "carte", "desenat", 30, "Arad", list)
    list = adaugaObiect("4", "telefon", "samsung", 3500, "Cluj", list)

    rezultat= sumaPretPerLocatie(list)

    assert len(rezultat)==2
    assert rezultat["Cluj"]==7500
    assert rezultat["Arad"]==80

def testUndoRedo():

    list = []
    undoList = []
    redoList = []

    rezultat = adaugaObiect("1", "caiet", "matematica", 5, "cluj", list)
    undoList.append(list)
    redoList.clear()
    list = rezultat
    assert len(list) == 1
    assert len(undoList)==1
    assert len(redoList)==0


    rezultat = adaugaObiect("2", "carte", "romana", 10, "aiud", list)
    undoList.append(list)
    redoList.clear()
    list = rezultat
    assert len(list) == 2
    assert len(undoList)==2
    assert len(redoList) == 0


    rezultat = adaugaObiect("3", "telefon", "iphone", 4000, "iasi", list)
    undoList.append(list)
    redoList.clear()
    list = rezultat
    assert len(list) == 3
    assert len(undoList)==3
    assert len(redoList) == 0
    assert list == [["1", "caiet", "matematica", 5, "cluj"], ["2", "carte", "romana", 10, "aiud"],["3", "telefon", "iphone", 4000, "iasi"]]


    if len(undoList) > 0:
        redoList.append(list)
        list = undoList.pop()
    assert undoList == [[], [["1", "caiet", "matematica", 5, "cluj"]]]
    assert len(list)==2
    assert len(undoList)==2
    assert len(redoList) == 1


    if len(undoList) > 0:
        redoList.append(list)
        list = undoList.pop()
    assert undoList == [[]]
    assert len(list)==1
    assert len(undoList)==1
    assert len(redoList) == 2


    if len(undoList) > 0:
        redoList.append(list)
        list = undoList.pop()
    assert undoList == []
    assert len(list)==0
    assert len(undoList)==0
    assert len(redoList) == 3


    if len(undoList) > 0:
        redoList.append(list)
        list = undoList.pop()
    assert undoList == []
    assert len(list) == 0
    assert len(undoList)==0
    assert len(redoList) == 3


    rezultat = adaugaObiect("1", "caiet", "matematica", 5, "cluj", list)
    undoList.append(list)
    redoList.clear()
    list = rezultat
    assert len(list) == 1
    assert len(undoList)==1
    assert len(redoList) == 0


    rezultat = adaugaObiect("2", "carte", "romana", 10, "aiud", list)
    undoList.append(list)
    redoList.clear()
    list = rezultat
    assert len(list) == 2
    assert len(undoList)==2
    assert len(redoList) == 0


    rezultat = adaugaObiect("3", "telefon", "iphone", 4000, "iasi", list)
    undoList.append(list)
    redoList.clear()
    list = rezultat
    assert len(list) == 3
    assert len(undoList)==3
    assert len(redoList) == 0
    assert list == [["1", "caiet", "matematica", 5, "cluj"], ["2", "carte", "romana", 10, "aiud"],["3", "telefon", "iphone", 4000, "iasi"]]



    if len(redoList) > 0:
        undoList.append(list)
        list = redoList.pop()
    assert len(list) == 3
    assert len(undoList)==3
    assert len(redoList) == 0


    if len(undoList) > 0:
        redoList.append(list)
        list = undoList.pop()
    assert undoList == [[], [["1", "caiet", "matematica", 5, "cluj"]]]
    assert len(list) == 2
    assert len(undoList)==2
    assert len(redoList) == 1


    if len(undoList) > 0:
        redoList.append(list)
        list = undoList.pop()
    assert undoList == [[]]
    assert len(list) == 1
    assert len(undoList)==1
    assert len(redoList) == 2


    if len(redoList) > 0:
        undoList.append(list)
        list = redoList.pop()
    assert len(list) == 2
    assert len(undoList)==2
    assert len(redoList) == 1


    if len(redoList) > 0:
        undoList.append(list)
    list = redoList.pop()
    assert len(list) == 3
    assert len(undoList)==3
    assert len(redoList) == 0


    if len(undoList) > 0:
        redoList.append(list)
    list = undoList.pop()
    assert undoList == [[], [["1", "caiet", "matematica", 5, "cluj"]]]
    assert len(list) == 2
    assert len(undoList)==2
    assert len(redoList) == 1


    if len(undoList) > 0:
        redoList.append(list)
    list = undoList.pop()
    assert undoList == [[]]
    assert len(list) == 1
    assert len(undoList)==1
    assert len(redoList) == 2


    rezultat = adaugaObiect("4", "telefon", "samsung", 3000, "iasi", list)
    undoList.append(list)
    redoList.clear()
    list = rezultat
    assert len(list) == 2
    assert len(undoList)==2
    assert len(redoList) == 0
    assert list == [["1", "caiet", "matematica", 5, "cluj"], ["4", "telefon", "samsung", 3000, "iasi"]]


    if len(redoList) > 0:
        undoList.append(list)
        list = redoList.pop()
    assert undoList == [[], [["1", "caiet", "matematica", 5, "cluj"]]]
    assert len(list) == 2
    assert len(undoList)==2
    assert len(redoList) == 0


    if len(undoList) > 0:
        redoList.append(list)
        list = undoList.pop()
    assert undoList == [[]]
    assert len(list) == 1
    assert len(undoList)==1
    assert len(redoList) == 1


    if len(undoList) > 0:
        redoList.append(list)
        list = undoList.pop()
    assert undoList == []
    assert len(list) == 0
    assert len(undoList)==0
    assert len(redoList) == 2


    if len(redoList) > 0:
        undoList.append(list)
        list = redoList.pop()
    assert len(list) == 1
    assert len(undoList)==1


    if len(redoList) > 0:
        undoList.append(list)
        list = redoList.pop()
    assert len(list) == 2
    assert len(undoList)==2
    assert len(redoList) == 0


    if len(redoList) > 0:
        undoList.append(list)
        list = redoList.pop()
    assert len(list) == 2
    assert len(undoList)==2
    assert len(redoList) == 0
    assert list == [["1", "caiet", "matematica", 5, "cluj"], ["4", "telefon", "samsung", 3000, "iasi"]]














