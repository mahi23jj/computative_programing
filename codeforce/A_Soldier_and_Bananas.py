z=0
x=list(map(int, input().split()))
for i in range(1,x[2]+1):
    z+=x[0]*i
if z < x[1]:
    y=0
else:    
    y=z-x[1]   
print(y)
