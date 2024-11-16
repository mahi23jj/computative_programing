t=input()
x=[]
y=[]
net=0
x.extend(map(int, input()))
y.extend(map(int, input()))
for i in range(int(t)):
    sum=0
    tot=0
    a=x[i]
    b=y[i]
    while a!=b:
        if a<b:
            a+=1
            sum+=1
        elif a>b:
            a+=1
            sum+=1
            if a==10:
                a=0
    a=x[i]
    b=y[i]
    while a!=b:
        if a<b:
            a-=1
            tot+=1
            if a==-1:
                a=9
        elif a>b:
            a-=1
            tot+=1        
    if sum<tot:
        net+=sum
    else:
        net+=tot                          
print(net)
