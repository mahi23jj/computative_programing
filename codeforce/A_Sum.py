t=input()
x=[]
for i in range(int(t)):
     x=[]
     x.extend(map(int, input().split()))
     if x[0]+x[1]==x[2]:
          print("YES")
     elif x[2]+x[1]==x[0]:
          print("YES")
     elif x[0]+x[2]==x[1]:
          print("YES")
     else:
          print("NO")
    


    


       


    

