from Tests.testCRUD import testAdaugaObiect, testStergeObiect, testModificaObiect
from Tests.testDomain import testObiect
from Tests.testFunctionalitati import testMutareaTuturorObiectelor, testConcatenareString, testCelMaiMarePretLocatii, \
    testOrdonareDupaPret, testSumaPretPerLocatie, testUndoRedo


def runAllTests():
    testObiect()
    testAdaugaObiect()
    testStergeObiect()
    testModificaObiect()
    testMutareaTuturorObiectelor()
    testConcatenareString()
    testCelMaiMarePretLocatii()
    testOrdonareDupaPret()
    testSumaPretPerLocatie()
    testUndoRedo()