from Tests.testCRUD import testAdaugaObiect, testStergeObiect, testModificaObiect
from Tests.testDomain import testObiect
from Tests.testFunctionalitati import testMutareaTuturorObiectelor


def runAllTests():
    testObiect()
    testAdaugaObiect()
    testStergeObiect()
    testModificaObiect()
    testMutareaTuturorObiectelor()