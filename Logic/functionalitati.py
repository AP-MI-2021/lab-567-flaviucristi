from Domain.obiect import getLocatie, creeazaObiect, getId, getNume, getDescriere, getPretachizitie

def mutareaTuturorObiectelor(loc,list,loc1):
    """
    mutarea tuturor obiectelor intr-o locatie data
    :param loc: string
    :param list: o lista cu obiecte
    :return: lista dupa mutare
    """
    listNoua=[]
    for obiect in list:
        if getLocatie(obiect)==loc:
            obiectNou=creeazaObiect(
                getId(obiect),
                getNume(obiect),
                getDescriere(obiect),
                getPretachizitie(obiect),
                loc1
            )
            listNoua.append(obiectNou)
        else:
            listNoua.append(obiect)
    return listNoua

def concatenareString(string,list,valoare):
    """

    :param string:
    :param obiect:
    :param valoare:
    :return:
    """
    listaNoua=[]

    for obiect in list:
        pret=getPretachizitie(obiect)
        if pret>valoare:
            obiectNou = creeazaObiect(
                getId(obiect),
                getNume(obiect),
                getDescriere(obiect)+" "+string,
                getPretachizitie(obiect),
                getLocatie(obiect)
            )
            listaNoua.append(obiectNou)
        else:
            listaNoua.append(obiect)

    return listaNoua

def celMaiMarePretLocatii(list):
    """

    :param list:
    :return:
    """
    rezultat={}
    for obiect in list:
        pret=getPretachizitie(obiect)
        locatie=getLocatie(obiect)
        if locatie in rezultat:
            if pret > rezultat[locatie]:
                rezultat[locatie]=pret
        else:
            rezultat[locatie]=pret

    return rezultat

def ordonareDupaPret(list):
    """

    :param list:
    :return:
    """
    return sorted(list, key= lambda obiect: getPretachizitie(obiect))

def sumaPretPerLocatie(list):
    """

    :param list:
    :return:
    """
    rezultat={}

    for obiect in list:
        locatie=getLocatie(obiect)
        pret=getPretachizitie(obiect)
        if locatie in rezultat:
            rezultat[locatie]=rezultat[locatie]+pret
        else:
            rezultat[locatie]=pret
    return rezultat


