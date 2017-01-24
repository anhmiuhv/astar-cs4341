import random
f = open("test1.txt", "w+")
st = ""
start = False
goal = False
for i in range(1000):
    for j in range(100):
        nu = random.randint(0, 2000)
        if nu == 0 and not start:
            start = True
            st += "S\t"
            continue
        if nu == 2000 and not goal:
            goal = True
            st += "G\t"
            continue

        if nu < 700:
            st += "#\t"
        else:
            c = random.randint(0,9)
            st += str(c) + "\t"
            
    st +="\n"


f.write(st)
f.close()
