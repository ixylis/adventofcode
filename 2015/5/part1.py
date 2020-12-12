#import statements here
f = open("input.txt", "r")

inpa = []
ans = 0

for line in f:
    inpa.append(line)
    if line.count("a")+line.count("e")+line.count("i")+line.count("o")+line.count("u")>=3:
        t = False
        for i in range(1, len(line)):
            c = line[i]
            if c==line[i-1]:
                t = True
        if t:
            if "ab" in line or "cd" in line or "pq" in line or "xy" in line:
                pass
            else:
                ans += 1



print(ans)
