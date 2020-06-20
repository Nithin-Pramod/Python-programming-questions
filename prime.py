a, o=[int(x) for x in input("enter the nunber of samples and range : ").split()]
b=[int(x) for x in input("enter the samples").split()]
arra=[]
for y in range(o):
    count=[]
    c,d=[int(x) for x in input("{}-enter the upper and lower range : ".format(y+1)).split()]
    q=0
    for x in b:
        if x in range(c,d):
            count.append(q+1)
    arra.append(sum(count))    
print(*arra,sep=" ")  
