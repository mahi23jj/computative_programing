
t=input()
j=0
z=list(map(str,input()))
for i in range(len(z)):
       if i != len(z)-1:
            if z[i]==z[i+1]:
              j+=1
print(j)






        
