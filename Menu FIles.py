def fileread():
    try:
        filename = input("Enter filename: ")
        f = open(filename, 'r')
        s = f.read()
        print(s)
        f.close()
    except:
        print("File Not Found")
def filewrite():
    try:
        filename = input("Enter filename: ")
        f = open(filename, "w")
        s = input("Enter the Content: ")
        f.write(s)
        f.close()
    except:
        print("File Not Found")
def fileappend():
    try:
        filename = input("Enter filename: ")
        f = open(filename, "a")
        s = input("Enter the Content: ")
        f.write(s)
        f.close()
    except:
        print("File Not Found")
def filesearch():
    try:
        filename = input("Enter filename: ")
        f = open(filename, "r")
        c = input("Enter the Content to Search: ")
        s = f.read()
        if c in s:
            print("Content Found", c)
        else:
            print("Not Found")
        f.close()
    except:
        print("File Not Found")
def filedelete():
    try:
        filename = input("Enter filename: ")
        import os
        os.remove(filename)
        print("File is Deleted")
    except:
        print("File Not Found")
while True:
    print("\nMenu Driven-File Operations")
    print("1.File Read")
    print("2.File Write")
    print("3.File Append")
    print("4.File Search")
    print("5.File Delete")
    print("6.Exit")
    try:
        ch = int(input("Enter the choice: "))
        if ch == 1:
            fileread()
        elif ch == 2:
            filewrite()
        elif ch == 3:
            fileappend()
        elif ch == 4:
            filesearch()
        elif ch == 5:
            filedelete()
        elif ch == 6:
            exit()
        else:
            print("Invalid Choice")
    except:
        print("Invalid Input")