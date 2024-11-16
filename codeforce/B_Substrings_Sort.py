t=int(input())
x=[]
for i in range(int(t)):
    l=input()
    x.append(l)
x.sort(key=len)
b='YES'
for i in range(1,len(x)):
        if x[i] not in x[-1]:
                b='NO'
print(b) 
if b=='YES':               
    for i in range(int(t)):
        print(x[i])

