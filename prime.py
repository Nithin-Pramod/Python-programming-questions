a=int(input("Enter the limit:"))
b=[]
for i in range(1,a):
    count=0
    for j in range(1,i):
        if i%j==0:
            count=count+1
    if count==1:
        b.append(i)
    count=0    
num=0
su=0
for k in b:
    su=su+k
    for l in b[b.index(k)+1:]:
        if su==l:
            num=num+1
print("the continous sum is ",num)
