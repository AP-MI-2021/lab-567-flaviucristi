from Logic.CRUD import adaugaObiect, stergeObiect, modificaObiect
from UI.console import showAll


def comenzi(list):
    while True:
        try:
            print("comenzi: help, add, delete, update, showall, stop")
            comanda=input("Dati comanda: ")
            if comanda=="help":
                print("introduceti comanda add -> pentru a adauga un nou obiect, iar dupa comanda add introduceti datele separate prin virgula")
                print("Exemplu: add,id,nume,descriere,pret achizitie,locatie")
                print("introduceti comanda delete -> pentru a sterge un obiect, iar dupa comanda delete id-ul obiectului de sters separat prin virgula")
                print("Exemplu: delet,id")
                print("introduceti comanda update -> pentru a modifica un obiect existent, iar dupa comanda update introduceti id-ul obiectului de modificat si noile date separate prin virgua")
                print("Exemplu: update,id obiect de modificat,noul nume,noua descriere,noul pret, noua locatie")
                print("introduceti comanda showall -> pentru a vedea obiectele")
                print("Exemplu: showall")
                print("introduceti cocmanda stop pentru a iesi")
                print("Se pot introduce mai multe comenzi separand-le prin ;")
                print("Exemplu: delete,id;showall")
            elif comanda == "stop":
                break
            else:
                comenzi=comanda.split(";")
                for i in range(len(comenzi)):
                    comanda_adaugata= comenzi[i].split(",")
                    if comanda_adaugata[0]=="add":
                        id=comanda_adaugata[1]
                        nume=comanda_adaugata[2]
                        descriere=comanda_adaugata[3]
                        pretachizitie=float(comanda_adaugata[4])
                        locatie=comanda_adaugata[5]

                        list= adaugaObiect(id,nume,descriere,pretachizitie,locatie,list)
                    elif comanda_adaugata[0]=="delete":
                        id=comanda_adaugata[1]
                        list=stergeObiect(id,list)
                    elif comanda_adaugata[0]=="update":
                        id = comanda_adaugata[1]
                        nume = comanda_adaugata[2]
                        descriere = comanda_adaugata[3]
                        pretachizitie = float(comanda_adaugata[4])
                        locatie = comanda_adaugata[5]

                        list=modificaObiect(id,nume,descriere,pretachizitie,locatie,list)
                    elif comanda_adaugata[0]=="showall":
                        showAll(list)
                    else:
                        print("Comanda gresita! Reincearca.")
        except ValueError as ve:
            print("Eroare: {}".format(ve))


