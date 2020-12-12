#import statements here
f = open("input.txt", "r")

inpa = []
ans = 0
v = {}
for line in f:
    inpa.append(line)
    inst = line.split(" ")
    v[inst[-1][0:-1]]=inst[0:-2]

def getValue(s):
    value = v[s]
    if isinstance(value, int):
        return v[s]
    if "NOT" in value:
        try:
            r = int(value[1])
        except:
            r = getValue(value[1])
        v[s] = 65535-r
    elif "AND" in value:        
        try:
            r1 = int(value[0])
        except:
            r1 = getValue(value[0])
        try:
            r2 = int(value[2])
        except:
            r2 = getValue(value[2])
        v[s]= r1 & r2
    elif "OR" in value:
        try:
            r1 = int(value[0])
        except:
            r1 = getValue(value[0])
        try:
            r2 = int(value[2])
        except:
            r2 = getValue(value[2])
        v[s]= r1 | r2
    elif "RSHIFT" in value:
        try:
            r1 = int(value[0])
        except:
            r1 = getValue(value[0])
        try:
            r2 = int(value[2])
        except:
            r2 = getValue(value[2])
        v[s]= r1 >> r2
    elif "LSHIFT" in value: 
        try:
            r1 = int(value[0])
        except:
            r1 = getValue(value[0])
        try:
            r2 = int(value[2])
        except:
            r2 = getValue(value[2])
        v[s]= r1 << r2
    else:
        try:
            v[s]= int(value[0])
        except:
            v[s]= getValue(value[0])
    return v[s]
ans = getValue("a")
print(ans)
