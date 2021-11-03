from Logic.CRUD import adaugaObiect
from Tests.testAll import runAllTests
from UI.comenzi import comenzi
from UI.console import runMenu


def main():
    runAllTests()
    list=[]
    list = adaugaObiect("1", "telefon", "iphone", 5000, "Cluj", list)
    list = adaugaObiect("2", "carte", "programare", 50, "Arad", list)
    list = adaugaObiect("3", "carte", "desenat", 30, "Aiud", list)
    list = adaugaObiect("4", "telefon", "samsung", 3500, "Iasi", list)
    comenzi(list)
if __name__ == '__main__':
    main()


