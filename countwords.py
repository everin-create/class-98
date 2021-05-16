def countwords():
    filename=input("enter the file name : ")
    numofwords=0
    file=open(filename,'r')
    for line in file:
        words=line.split()
        numofwords=numofwords+len(words)
    print("number of words")
    print(numofwords)

countwords()