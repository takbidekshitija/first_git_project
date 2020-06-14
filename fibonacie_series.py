def get_fibonacie(n):
    l = []
    i = 0
    j = 1
    l.extend([i,j])
    while len(l) != n:
        temp = j
        j = i + j
        i = temp
        l.append(j)
    return l
if __name__ =="__main__":
    n = int(input("Enter number:"))
    result = get_fibonacie(n)
    print("Fibonacie series ={}".format(result))
