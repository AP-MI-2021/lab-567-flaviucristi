from Domain.obiect import creeazaObiect, getId


def adaugaObiect(id,nume,descriere,pretachizitie,locatie,list):
    """
    adauga un obiect intr-o lista
    :param id: string
    :param nume: string
    :param descriere: string
    :param pretachizitie: float
    :param loactie: string
    :param list: lista de obiecte
    :return: o lista care contine atat elementele vechi, cat si obiectul nou
    """
    obiect= creeazaObiect(id,nume,descriere,pretachizitie,locatie)
    return list + [obiect]

def getById(id,list):
    """
    gaseste un obiect cu id-ul dat intr-o lista
    :param id: string
    :param list: lista de obiecte
    :return: obiectul cu id-ul dat sau None daca nu exista
    """
    for obiect in list:
        if getId(obiect)==id:
            return obiect
    return None

def stergeObiect(id,list):
    """
    sterge un obiect cu id-ul dat din lista
    :param id: string
    :param list: o lista cu obiecte
    :return: o lista de obiecte fara obiectul cu id-ul dat
    """
    return [obiect for obiect in list if getId(obiect)!=id]

def modificaObiect(id,nume,descriere,pretachizitie,locatie, list):
    """
    modifica un obiect cu id-ul dat
    :param id: stirng
    :param nume: string
    :param descriere: string
    :param pretachizitie: float
    :param locatie: string
    :return: lista modificata
    """
    listNoua=[]
    for obiect in list:
        if getId(obiect)== id:
            obiectNou= creeazaObiect(id,nume,descriere,pretachizitie,locatie)
            listNoua.append(obiectNou)
        else:
            listNoua.append(obiect)
    return listNoua

