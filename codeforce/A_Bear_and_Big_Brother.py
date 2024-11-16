
for i in range(1):
     x=[]
     x.extend(map(int, input().split()))
cou=0
while x[0]<=x[1]:
    x[0]*=3
    x[1]*=2
    cou+=1
print(cou)   