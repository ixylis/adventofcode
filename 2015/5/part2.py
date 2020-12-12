#import statements here
f = open("input.txt", "r")

inpa = []
ans = 0

for line in f:
    inpa.append(line)
    c1 = False
    c2 = False
    for ci in range(len(line)-1):
        c = line[ci]
        if line[ci:ci+2] in line[ci+2::]:
            c1 = True
    for ci in range(len(line)-2):
        c = line[ci]
        if line[ci]==line[ci+2]:
            c2 = True
    if c1 and c2:
        ans += 1


print(ans)
