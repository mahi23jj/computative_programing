n,m=map(int, input().split())
x=list(map(int, input().split()))
y=list(map(int, input().split()))
z=[]
i=0
j=0
while len(x)>i and len(y)>j: 
    # len(x)-5 so i don"t have to be greaterthen 5 .
    if x[i]<y[j]:
        z.append(x[i])
        i+=1
    else:
        z.append(y[j])
        j+=1  
z.extend(x[i:])  
# to add the remaining elements
z.extend(y[j:])      
print(*z)    
