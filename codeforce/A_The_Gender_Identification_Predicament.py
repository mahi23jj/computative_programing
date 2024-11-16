x=input()
result="".join(set(x))
b=0
for a in result:
    b+=1 
if b%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')        