from Domain.obiect import creeazaObiect, getNume, getId, getDescriere, getPretachizitie, getLocatie


def testObiect():
    obiect=creeazaObiect("1","telefon","iphone",4000,"Cluj")

    assert  getId(obiect)=="1"
    assert getNume(obiect)=="telefon"
    assert getDescriere(obiect)=="iphone"
    assert getPretachizitie(obiect)==4000
    assert getLocatie(obiect)=="Cluj"
