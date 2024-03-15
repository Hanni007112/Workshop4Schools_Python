def taschenrechner(zahl1, zahl2, operation):
     # Hier kommt dein Code hin
     pass



#-------------------
#    Tests:
#-------------------
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(0, parentdir)
import testing

print("TESTS:")
testNum = 1
testNum = testing.testFunction(taschenrechner, testNum, 0, 0, 0, "+")
testNum = testing.testFunction(taschenrechner, testNum, 0, 0, 0, '*')
testNum = testing.testFunction(taschenrechner, testNum, -1, 1, -2, "+")
testNum = testing.testFunction(taschenrechner, testNum, None, 0, 0, "#")
testNum = testing.testFunction(taschenrechner, testNum, None, 100, 0,  "/")
testNum = testing.testFunction(taschenrechner, testNum, 100, 10, 10, "*")
testNum = testing.testFunction(taschenrechner, testNum, 15, 10, 5, "+")
testNum = testing.testFunction(taschenrechner, testNum, 100, 150, 50, "-")