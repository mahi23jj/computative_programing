y=int(input())
x=input()
z=''
for i in range(len(x)):
    if len(x)%2!=0:
        if i%2==0:
           z=z+x[i]
        else:
            z=x[i]+z  
    else:
        if i%2==0:
           z=x[i]+z
        else:
            z=z+x[i] 
print(z)        