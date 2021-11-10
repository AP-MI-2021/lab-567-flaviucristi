from Domain.obiect import getId, getNume, getDescriere, getPretachizitie, getLocatie
from Logic.CRUD import adaugaObiect, getById, stergeObiect, modificaObiect


def testAdaugaObiect():
    list=[]
    list = adaugaObiect("1","telefon","iphone",4000,"Cluj",list)
    list = adaugaObiect("2", "carte", "programare", 50, "Arad", list)

    assert getId(list[0]) == "1"
    assert getNume(list[0]) == "telefon"
    assert getDescriere(list[0]) == "iphone"
    assert getPretachizitie(list[0]) == 4000
    assert getLocatie(list[0]) == "Cluj"

    assert getId(getById("2",list)) == "2"
    assert getNume(getById("2",list)) == "carte"
    assert getDescriere(getById("2",list)) == "programare"
    assert getPretachizitie(getById("2",list)) == 50
    assert getLocatie(getById("2",list)) == "Arad"

def testStergeObiect():
    list=[]
    list = adaugaObiect("1", "telefon", "iphone", 4000, "Cluj", list)
    list = adaugaObiect("2", "carte", "programare", 50, "Arad", list)

    list= stergeObiect("1",list)
    assert len(list)==1
    assert getById("1",list) is None
    assert getById("2",list) is not None

def testModificaObiect():
    list = []
    list = adaugaObiect("1", "telefon", "iphone", 4000, "Cluj", list)
    list = adaugaObiect("2", "carte", "programare", 50, "Arad", list)

    list= modificaObiect("1","carte", "desenat",45,"Arad", list)

    assert getId(getById("1", list)) == "1"
    assert getNume(getById("1", list)) == "carte"
    assert getDescriere(getById("1", list)) == "desenat"
    assert getPretachizitie(getById("1", list)) == 45
    assert getLocatie(getById("1", list)) == "Arad"

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


def testStergereUndoRedo():
    list = [["1", "caiet", "matematica", 5, "cluj"],["2", "carte", "romana", 10, "aiud"],["3", "telefon", "iphone", 4000, "iasi"]]
    undoList = []
    redoList = []

    rezultat = stergeObiect("2",list)
    undoList.append(list)
    redoList.clear()
    list = rezultat
    assert len(list) == 2
    assert len(undoList) == 1
    assert len(redoList) == 0

    rezultat = stergeObiect("1", list)
    undoList.append(list)
    redoList.clear()
    list = rezultat
    assert len(list) == 1
    assert len(undoList) == 2
    assert len(redoList) == 0

    if len(undoList) > 0:
        redoList.append(list)
        list = undoList.pop()
    assert len(list) == 2
    assert len(undoList) == 1
    assert len(redoList) == 1

    if len(undoList) > 0:
        redoList.append(list)
        list = undoList.pop()
    assert len(list) == 3
    assert len(undoList) == 0
    assert len(redoList) == 2

    if len(redoList) > 0:
        undoList.append(list)
        list = redoList.pop()
    assert len(list) == 2
    assert len(undoList) == 1
    assert len(redoList) == 1

def testModificareUndoRedo():
    list = [["1", "caiet", "matematica", 5, "cluj"], ["2", "carte", "romana", 10, "aiud"],
            ["3", "telefon", "iphone", 4000, "iasi"]]
    undoList = []
    redoList = []

    rezultat = modificaObiect("2", "tableta", "sony", 1500, "cluj",list)
    undoList.append(list)
    redoList.clear()
    list = rezultat
    assert len(list) == 3
    assert len(undoList) == 1
    assert len(redoList) == 0

    rezultat = modificaObiect("1", "carte","muzica",12,"iasi",list)
    undoList.append(list)
    redoList.clear()
    list = rezultat
    assert len(list) == 3
    assert len(undoList) == 2
    assert len(redoList) == 0

    if len(undoList) > 0:
        redoList.append(list)
        list = undoList.pop()
    assert len(list) == 3
    assert len(undoList) == 1
    assert len(redoList) == 1

    if len(undoList) > 0:
        redoList.append(list)
        list = undoList.pop()
    assert len(list) == 3
    assert len(undoList) == 0
    assert len(redoList) == 2

    if len(redoList) > 0:
        undoList.append(list)
        list = redoList.pop()
    assert len(list) == 3
    assert len(undoList) == 1
    assert len(redoList) == 1
    assert  list == [["1", "caiet", "matematica", 5, "cluj"], ["2", "tableta", "sony", 1500, "cluj"],
            ["3", "telefon", "iphone", 4000, "iasi"]]




