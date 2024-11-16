tot=list(map(int, input().split()))
day=list(map(int, input().split()))

z=0
y=0
l=-1
for i in range(len(day)):
    if day[i]>=8:
        z+=8
        y=day[i]-8
        if z >= tot[1]:
            l=i+1
            break
    else:
        z=z+day[i]+y
        if z >= tot[1]:
            l=i+1
            break
print(l)  
