t=int(input())
x=list(map(int, input().split()))
z=[]
d=0
for i in range(int(len(x)/2)):
    z=[]
    for j in range(len(x)):
        if j>i:
            c=x[j]-x[i]
            if c<0:
                c=c*-1
            z.append(c)
    d+=min(z)        
print(d)

n=int(input())
a=list(map(int,input().split()))
a.sort()
sum=0
for i in range(1,n,2):
    sum+=a[i]-a[i-1]
print(sum)

