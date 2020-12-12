#import statements here
f = open("input.txt", "r")

inpa = []
ans = 0
la = []

for i in range(1000):
    la.append([False for x in range(1000)])

for line in f:
    inpa.append(line)
    inst = line.split(" ")
    if inst[0]=="turn":
        fc = inst[2].split(",")
        sc = inst[4].split(",")
        x1 = int(fc[0])
        x2 = int(sc[0])
        y1 = int(fc[1])
        y2 = int(sc[1])
        if inst[1]=="on":
            v = True
        elif inst[1]=="off":
            v = False
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                la[i][j]=v
    elif inst[0]=="toggle":
        fc = inst[1].split(",")
        sc = inst[3].split(",")
        x1 = int(fc[0])
        x2 = int(sc[0])
        y1 = int(fc[1])
        y2 = int(sc[1])
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                la[i][j]= not la[i][j]

for i in range(1000):
    for j in range(1000):
        if la[i][j]:
            ans += 1

print(ans)
