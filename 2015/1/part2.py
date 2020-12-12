#import statements here
f = open("input.txt", "r")

inp=[]
ans = 0
floor = 0

for line in f:
    inp.append(line)
for li in range(len(inp)):
    line = inp[li]
    for ci in range(len(line)):
        c = line[ci]
        ans +=1
        if c=="(":
            floor +=1
        elif c==")":
            floor -=1
        if floor==-1:
            break

print(ans)

