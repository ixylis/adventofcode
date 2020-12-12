#import statements here
f = open("input.txt", "r")

inp=[]
ans = 0
floor = 0


for line in f:
    inp.append(line)
    for c in line:
        if c=="(":
            floor +=1
        elif c==")":
            floor -=1
ans = floor

print(ans)

