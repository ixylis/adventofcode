#import statements here
f = open("input.txt", "r")

inp = []
ans = 0
houses = set()
x = 0
y = 0

houses.add((x, y))
for line in f:
    inp.append(line)
    for c in line:
        if c=="^":
            y+=1
        elif c=="v":
            y-=1
        elif c==">":
            x+=1
        elif c=="<":
            x -=1
        houses.add((x, y))


ans = len(houses)
print(ans)
