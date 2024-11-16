a,b=map(int, input().split())
x=[]
y=[]
x.extend(map(int, input().split()))
y.extend(map(int, input().split()))
i=0


ans=[]
for sec in range(b):
    while i<a and x[i]<y[sec]:
        i+=1
    ans.append(i)    
print(*ans)    
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# a.sort()
# b.sort()

# i = 0
# results = []

# for item in b:
#     while i < n and a[i] < item:
#         i += 1
#     results.append(i)
# print(results)