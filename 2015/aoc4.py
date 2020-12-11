import hashlib
inp="bgvyzdsv"
found=False
i=1
while not found:
    print(i)
    einp=inp+str(i)
    m = hashlib.md5(einp.encode())
    mstr = m.hexdigest()
    if mstr[0:6]=="000000":
        found=True
        print(mstr)
    else:
        i+=1

