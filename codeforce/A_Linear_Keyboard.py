test=int(input())
ask=[]
for i in range(test):
    words=list(input())
    let=list(input())
    ask.append([words,let]) 
val={}
i=1
for i in range(test):
    words=ask[i][0]
    let=ask[i][1]
    result=0
    for word in words:
        val[word]=i
        i+=1
    if len(let)==1:
        print(0) 
    else:
        x=val[let[0]]
        for i in range(1,len(let)):
            result+=abs(val[let[i]]-x)
            x=val[let[i]]
        print(result)


