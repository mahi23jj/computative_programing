a=list(map(int,input().rstrip().split()))
s=a[0]
n=a[1]
lst=[]
for i in range(n):
    b=list(map(int,input().rstrip().split()))
    lst.append(b)
lst.sort()

f=0
for j in lst:
    if s>j[0]:
        s+=j[1]
        f+=1
if f==len(lst):
    print("YES")
else:
    print("NO")