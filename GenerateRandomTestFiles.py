import random

numTestFiles = 10
numNodesPerFile = 10
maxCoordVal = 1000

for i in range(0, numTestFiles):
    if (i % 3 == 0):
        mode = "MST"
    elif (i % 3 == 1):
        mode = "FASTTSP"
    else:
        mode = "OPTTSP"

    testName = "test-" + str(i + 1) + "-" + mode + ".txt"
    f = open(testName, "w")
    
    f.write(str(numNodesPerFile) + "\n")
    for j in range(0, numNodesPerFile):
        #need at least 1 decontamination room for MST
        if (j == 0 and mode == "MST"):
            x = 0
            y = random.randint(maxCoordVal * -1, 0)
        else:
            x = random.randint(maxCoordVal * -1, maxCoordVal)
            y = random.randint(maxCoordVal * -1, maxCoordVal)
        f.write(str(x) + " " + str(y) + "\n")
    f.close()
    print("wrote " + str(numNodesPerFile) + " coordinates to " + testName)