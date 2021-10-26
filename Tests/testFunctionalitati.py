from Domain.obiect import getId, getNume, getDescriere, getPretachizitie, getLocatie
from Logic.CRUD import adaugaObiect
from Logic.functionalitati import mutareaTuturorObiectelor


def testMutareaTuturorObiectelor():
    list = []
    list = adaugaObiect("1", "telefon", "iphone", 4000, "Cluj", list)
    list = adaugaObiect("2", "carte", "programare", 50, "Arad", list)
    list = adaugaObiect("3", "carte", "desenat", 30, "Aiud", list)
    list = adaugaObiect("4", "telefon", "samsung", 3500, "Iasi", list)

    list=mutareaTuturorObiectelor("Cluj",list)

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
    assert getLocatie(list[3]) == "Cluj"