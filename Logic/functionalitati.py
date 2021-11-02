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
    Concateneaza un string citit la toate descrieriile cu pretul mai mare decat o valoare citita
    :param string: string
    :param list: o lista de obiecte
    :param valoare: float
    :return: lista dupa ce a fost modificata descrierea obiectelor la toate obiectele cu pretul mai mare dacat o valoare data
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
    cel mai mare pret pentru fiecare locatie
    :param list: o lista de obiecte
    :return: pretul maxim pentru fiecare locatie
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
    Ordonarea obiectelor crescator dupa pretul de achizitie
    :param list: o lista de obiecte
    :return: lista ordonata crescator dupa pretul de achizitie
    """
    return sorted(list, key= lambda obiect: getPretachizitie(obiect))

def sumaPretPerLocatie(list):
    """
    sumele preturilor pentru fiecare locatie
    :param list: o lista de obiecte
    :return: suma preturilor pentru fiecare locatie
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


