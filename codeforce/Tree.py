t = int(input())
l=[]
for i in range(t):
    ins=int(input())
    l.append(ins)

for j in range(len(l)):
    n=l[j]
    ans = 0
    while n > 0:
        ans += n
        n //= 2
    print(ans)

