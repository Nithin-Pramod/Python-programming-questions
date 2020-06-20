a,b=[int(x) for x in input("enter the number and divident").split(",")]
c=[]
try:
    for i in range(1,a+1):
        if a%i==0:
            c.append(i)
    print(c[b])
except:
    print(1)
