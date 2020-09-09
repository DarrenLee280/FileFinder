import os

def countLines():
    file = open("Sorted File List.txt", "w")
    count = 0

    content = file.read()
    coList = Content.split("\n")

    for i in coList:
        if i:
            count +=1

def createFile():
    file = open("Sorted File List.txt", "w+")

    #start to sort
    for root, dirs, files in os.walk(r"C:\Users\dlee\Desktop\Test Folder"):
        new_file = files[::-1]
        for name in new_file:
            file.write(name + "\n")

    file.close()


def main():
    createFile()



main()
