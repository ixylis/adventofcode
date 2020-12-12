#import statements here
import hashlib
f = open("input.txt", "r")

inpa = []
ans = 0

for line in f:
    inpa.append(line)
inpa = inpa[0][0:-1]

n = 1
while True:
    ei = inpa+str(n)
    e = ei.encode('utf=8')
    m = hashlib.md5(e)
    mstr = m.hexdigest()
    if mstr[0:6]=="000000":
        break
    n +=1
ans = n
print(ans)
