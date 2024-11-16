t=input()
j=1
x=[]
for i in range(int(t)):
    x.extend(map(int,input()))
for i in range(len(x)):
    if i != len(x)-1:
        if x[i]==x[i+1]:
           j+=1
print(j)
#344A