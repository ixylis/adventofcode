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
        print(line)
        line2 = ast.literal_eval(line)
        print(line2)
        strliteral+=len(line2)
    except:
        pass


#get answer
ans = strliteral-memchar
print(ans)
