from Domain.obiect import getLocatie, creeazaObiect, getId, getNume, getDescriere, getPretachizitie

def mutareaTuturorObiectelor(loc,list):
    """
    mutarea tuturor obiectelor intr-o locatie data
    :param loc: string
    :param list: o lista cu obiecte
    :return: lista dupa mutare
    """
    listNoua=[]
    for obiect in list:
        if getLocatie(obiect)!=loc:
            obiectNou=creeazaObiect(
                getId(obiect),
                getNume(obiect),
                getDescriere(obiect),
                getPretachizitie(obiect),
                loc
            )
            listNoua.append(obiectNou)
        else:
            listNoua.append(obiect)
    return listNoua
