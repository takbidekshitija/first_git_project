def writetofile():
    with open("demo.txt", "w") as f:
        f.write("Hello World!! how are you \n")
        l = ["Kshitija\n", "Takbie\n", "28\n"]
        print(dir(f))
        f.writelines(l)

def readtofile():
    with open("demo.txt", "r") as f:
        #read as string
        print("####read as string##")
        print(f.read())   # if you want to load whole content(HTML)
        f.seek(0)
        print("####read line by line ###")
        # read line by line
        for line in f:
            print(line)
        f.seek(0)
        print("#### read as list of string ##")
        #read as list of string
        for c,line in enumerate(f):
            print(c)
            print(line)



def appendtofile():
    with open("demo.txt","a+") as f:
        f.write("Hello Vinod")

def findkeyword(word):
    with open("demo.txt", "r")as f:
        l = l.readlines()
        print(l)
        # print "enumerate op", enumerate (l)
        found = False
        for i v in enumerate(l):
            lower_string =



if __name__=="__main__":
    writetofile()
    readtofile()
    appendtofile()



