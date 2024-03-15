def anagramm(s1:str, s2:str):
     # Hier kommt dein Code hin
     pass






#-------------------
#    Tests:
#-------------------
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import testing

print("TESTS:")
testNum = 1
testNum = testing.testFunction(anagramm, testNum, False, "", "")
testNum = testing.testFunction(anagramm, testNum, True, "a", "a")
testNum = testing.testFunction(anagramm, testNum, False, "ab", "b")
testNum = testing.testFunction(anagramm, testNum, True, "A", "a")
testNum = testing.testFunction(anagramm, testNum, True, "Auu", "UAu")
testNum = testing.testFunction(anagramm, testNum, True, "Mehl", "Lehm")
testNum = testing.testFunction(anagramm, testNum, True, "Aberglaube", "Regelabbau")
testNum = testing.testFunction(anagramm, testNum, True, "bauschutt", "Staubtuch")