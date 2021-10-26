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




