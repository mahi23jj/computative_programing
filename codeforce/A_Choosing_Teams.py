z=0
x=list(map(int, input().split()))
y=list(map(int, input().split()))
for i in range(len(y)):
    a=5-y[i]
    if a>=x[1]:
        z+=1
tot=z//3
print(tot)