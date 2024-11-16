x=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n=len(x)
len=int(input())
words=input()
z=[]
for word in words:
    if word.isupper():
        word=word.lower()
    z.append(word)    
c='YES'      
for y in x:
    if y not in z:
            c='NO'
            break
print(c)

