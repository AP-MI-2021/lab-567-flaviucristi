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

def getNume(obiect):
    """
    da numele unui obiect
    :param obiect:dictionar ce contine un obiect
    :return: numele obiectului
    """
    return obiect[1]

def getDescriere(obiect):
    """
    da descrierea unui obiect
    :param obiect:dictionar ce contine un obiect
    :return: descrierea obiectului
    """
    return obiect[2]

def getPretachizitie(obiect):
    """
    da pretul de achizitie al unui obiect
    :param obiect:dictionar ce contine un obiect
    :return: pretul de achizitie al obiectului
    """
    return obiect[3]

def getLocatie(obiect):
    """
    da locatia obiectului
    :param obiect:disctionar ce contine un obiect
    :return: locatia obiectului
    """
    return obiect[4]

def toString(obiect):
    return "Id: {},Nume: {},Descriere: {}, Pretachizitie: {},Locatie: {}".format(
        getId(obiect),
        getNume(obiect),
        getDescriere(obiect),
        getPretachizitie(obiect),
        getLocatie(obiect)
    )
