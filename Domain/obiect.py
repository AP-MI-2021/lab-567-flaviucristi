def  creeazaObiect(id:str,nume:str,descriere:str,pretachizitie:float,locatie:str):
    """
    creeaza un dictionar ce contine un obiect
    :param id: string
    :param nume: string
    :param descriere: string
    :param pretachizitie: float
    :param locatie: string
    :return: un dictionar ce contine un obiect
    """

    list=[id,nume,descriere,pretachizitie,locatie]
    return list

def getId(list):
    """
    da id-ul unui obiect
    :param obiect: dictionar de contine un obiect
    :return: id-ul obiectului
    """
    return list[0]

def getNume(lista):
    """
    da numele unui obiect
    :param obiect:dictionar ce contine un obiect
    :return: numele obiectului
    """
    return lista[1]

def getDescriere(list):
    """
    da descrierea unui obiect
    :param obiect:dictionar ce contine un obiect
    :return: descrierea obiectului
    """
    return list[2]

def getPretachizitie(list):
    """
    da pretul de achizitie al unui obiect
    :param obiect:dictionar ce contine un obiect
    :return: pretul de achizitie al obiectului
    """
    return list[3]

def getLocatie(list):
    """
    da locatia obiectului
    :param obiect:disctionar ce contine un obiect
    :return: locatia obiectului
    """
    return list[4]

def toString(list):
    return "Id: {},Nume: {},Descriere: {}, Pretachizitie: {},Locatie: {}".format(
        getId(list),
        getNume(list),
        getDescriere(list),
        getPretachizitie(list),
        getLocatie(list)
    )
