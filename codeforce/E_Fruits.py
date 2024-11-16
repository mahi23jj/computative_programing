y=list(map(int, input().split()))
x=list(map(int, input().split()))
a=input()
b=input()
c=input()
x.sort()
v=sorted(x,reverse=True)
f=0
l=0
for i in range(y[1]):
    f+=v[i]
for j in range(y[1]):
    l+=x[j]
print(str(l)+" "+str(f))    

