def countWordsFromFile():
    fileName = input("Enter the file name:")

    numOfWords=0
    file = open(fileName,'r')
    fileLines = file.readlines()
    for line in fileLines:
        numOfWords = numOfWords+len(line)
    print("Total Words:")
    print(numOfWords)

countWordsFromFile()