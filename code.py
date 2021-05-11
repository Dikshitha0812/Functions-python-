def countingnoofwords():
    filename=input("pls enter the full path of file along with file =")
    file=open(filename)
    filelines=file.readlines()
    print(filelines)
    noofwords=0
    for line in filelines:
        words=line.split()
        noofwords=noofwords+len(words)

    print("number of word in file are "+ str(noofwords))

countingnoofwords()