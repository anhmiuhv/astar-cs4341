import random
f = open("test5.txt", "w+")
st = ""
start = False
goal = False
for i in range(100):
    for j in range(100):
        nu = random.randint(0, 1000)
        if nu == 0 and not start:
            start = True
            st += "S\t"
            continue
        if nu == 0 and not goal:
            goal = True
            st += "G\t"
            continue

        if nu < 100:
            st += "#\t"
        else:
            c = random.randint(0,9)
            st += str(c) + "\t"
            
    st +="\n"


f.write(st)
f.close()
