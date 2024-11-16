g=int(input())
x=list(map(int, input().split()))
y=list(set(x))
z=len(y)
m=[]
b={}
s=[]
for a in x:
    b[a]=x.count(a)
for c in b:    
    s.append(b[c])
val=max(s)  
print(str(val)+" "+str(z))  

   
    