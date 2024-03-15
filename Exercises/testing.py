def printResultOfFailedTest(testNum, expectedOutput, recievedOutput, concatinatedInputs):
    print(f"Test {testNum} failed\n Input: {concatinatedInputs}\n Expected Ouput:{expectedOutput}\n Recieved Output:{recievedOutput}")

def testFunction(function, testNum, expectedOutput, *inputs):
    returnTestNum = testNum + 1
    concatinatedInputs = ""
    for i in inputs:
        concatinatedInputs += (str)(i) + ", "
    concatinatedInputs = concatinatedInputs[:len(concatinatedInputs)-2:]
    try:
        recievedOutput = function(*inputs)
    except Exception as e:
        print(f"Test {testNum} failed Input :{concatinatedInputs} \n Error message: \n{e}")
        return returnTestNum
    try:
        if(recievedOutput == expectedOutput):
            print(f"Test {testNum} passed")
            return returnTestNum
    except:
        pass     
    printResultOfFailedTest(testNum, expectedOutput, recievedOutput, inputs)
    return testNum+1