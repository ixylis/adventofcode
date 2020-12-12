#import statements here
f = open("input.txt", "r")
import ast

#variables
inp = f.read()
inpa = inp.split("\n")
memchar=0
strliteral=0
ans = 0
#code goes here
for line in inpa:
    try:
        memchar+=len(line)
        line2 = repr(line)
        strliteral+=len(line)+2+line.count('\\')+line.count('"')
    except:
        pass


#get answer
ans = strliteral-memchar
print(sum(2+s.count('\\')+s.count('"') for s in open('input.txt')))
print(ans)
