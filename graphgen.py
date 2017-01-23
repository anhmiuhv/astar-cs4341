import random
f = open("sample1.txt", "w+")
st = ""
start = False
goal = False
for i in range(1000):
    for j in range(1000):
        nu = random.randint(0, 70)
        if nu == 0 and not start:
            start = True
            st += "S\t"
            continue
        if nu == 0 and not goal:
            goal = True
            st += "G\t"
            continue

        if nu < 20:
            st += "#\t"
        else:
            c = random.randint(0,9)
            st += str(c) + "\t"
            
    st +="\n"


f.write(st)
f.close()
