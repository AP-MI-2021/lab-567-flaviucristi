from Tests.testCRUD import testAdaugaObiect, testStergeObiect, testModificaObiect, testUndoRedo, testStergereUndoRedo, \
    testModificareUndoRedo
from Tests.testDomain import testObiect
from Tests.testFunctionalitati import testMutareaTuturorObiectelor, testConcatenareString, testCelMaiMarePretLocatii, \
    testOrdonareDupaPret, testSumaPretPerLocatie, testMutareaTuturorObiectelorUndoRedo, testConcatenareStringUndoRedo


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
    testStergereUndoRedo()
    testModificareUndoRedo()
    testMutareaTuturorObiectelorUndoRedo()
    testConcatenareStringUndoRedo()