from Logic.CRUD import adaugaObiect
from Tests.testAll import runAllTests
from UI.comenzi import comenzi
from UI.console import runMenu


def main():
    runAllTests()
    list=[]

    runMenu(list)
if __name__ == '__main__':
    main()


