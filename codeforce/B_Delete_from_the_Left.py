s = input()  # First String
t = input()  # Second String
x=[]
re=0
res = 0
while len(s)!=len(t):
     if len(s)>len(t):
          s=s[1:]
          re+=1
     elif len(t)>len(s):
          t=t[1:]
          re+=1

for i in range(len(s) - 1, -1, -1):
        if s[i] == t[i]:
            res += 1
        else:
            break
v=(len(s) - res) + (len(t) - res)
print(v+re)