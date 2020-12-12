#import statements here
f = open("input.txt", "r")

inp = []
ans = 0
houses = set()
x = 0
y = 0
rx=0
ry=0
Robot = False

houses.add((x, y))
for line in f:
    inp.append(line)
    for c in line:
        if Robot:
            if c=="^":
                y+=1
            elif c=="v":
                y-=1
            elif c==">":
                x+=1
            elif c=="<":
                x -=1
        else:
            if c=="^":
                ry+=1
            elif c=="v":
                ry-=1
            elif c==">":
                rx+=1
            elif c=="<":
                rx -=1
        Robot = not Robot
        houses.add((x, y))
        houses.add((rx, ry))


ans = len(houses)
print(ans)
