t=int(input())
l=[]
for i in range(t):
    n=int(input())
    y=list(map(int, input()))
    l.append([n,y])
for i in range(t):
    g=l[i][0]
    p=l[i][1]
    j=0
    k=g-1
    while k>j:
        if p[k]==0 and p[j]==1 or p[k]==1 and p[j]==0 :
            k-=1
            j+=1
        else:
            break    
    print(k-j+1)



