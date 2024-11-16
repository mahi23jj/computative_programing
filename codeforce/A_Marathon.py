t=input()
for i in range(int(t)):
    count=0
    x=[]
    j=1
    x.extend(map(int,input().split()))
    while j<4:
        if x[j]>x[0]:
            count +=1
        j+=1
    print(count)



