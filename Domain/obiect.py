def  creeazaObiect(id,nume,descriere,pretachizitie,locatie):
    """
    creeaza un dictionar ce contine un obiect
    :param id: string
    :param nume: string
    :param descriere: string
    :param pretachizitie: float
    :param locatie: string
    :return: un dictionar ce contine un obiect
    """
    return {
        "id":id,
        "nume":nume,
        "descriere":descriere,
        "pretachizitie":pretachizitie,
        "locatie":locatie
    }

def getId(obiect):
    """
    da id-ul unui obiect
    :param obiect: dictionar de contine un obiect
    :return: id-ul obiectului
    """
    return obiect["id"]

def getNume(obiect):
    """
    da numele unui obiect
    :param obiect:dictionar ce contine un obiect
    :return: numele obiectului
    """
    return obiect["nume"]

def getDescriere(obiect):
    """
    da descrierea unui obiect
    :param obiect:dictionar ce contine un obiect
    :return: descrierea obiectului
    """
    return obiect["descriere"]

def getPretachizitie(obiect):
    """
    da pretul de achizitie al unui obiect
    :param obiect:dictionar ce contine un obiect
    :return: pretul de achizitie al obiectului
    """
    return obiect["pretachizitie"]

def getLocatie(obiect):
    """
    da locatia obiectului
    :param obiect:disctionar ce contine un obiect
    :return: locatia obiectului
    """
    return obiect["locatie"]

def toString(obiect):
    return "Id: {},Nume: {},Descriere: {}, Pretachizitie: {},Locatie: {}".format(
        getId(obiect),
        getNume(obiect),
        getDescriere(obiect),
        getPretachizitie(obiect),
        getLocatie(obiect)
    )
