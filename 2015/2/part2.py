#import statements here
f = open("input.txt", "r")

inp = []
ans = 0

for line in f:
    inp.append(line)
    dim = line.split("x")
    l = int(dim[0])
    w = int(dim[1])
    h = int(dim[2])
    ans += l*w*h+2*min(l+w, l+h, w+h)

print(ans)
