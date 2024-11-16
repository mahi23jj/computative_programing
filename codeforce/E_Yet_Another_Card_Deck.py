n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
t={}
z=[]
for i in  range(n):
    if x[i] not in t:
        t[x[i]]=i
for i in  range(m):
    z.append(t[y[i]]+1)
    for v in t:
        if t[v]<t[y[i]]:
            t[v]+=1
        elif t[v]==t[y[i]]:
            t[v]=0      
print(*z)
# t = []
# for val in y:
#     for i in range(len(x)):
#         if x[i] == val:
#             t.append(i + 1)
#             k = x[i]
#             x.pop(i)
#             x.insert(0, k)

#             break
#     #print(x)    
# print(*t)


# n, q = map(int, input().split())
# x = list(map(int, input().split()))
# y = list(map(int, input().split()))
# index = [float('inf')] * 55

# for i in range(n):
#        color = int(input())
#         # Find the minimum index for each distinct color
#        index[x[i]] = min(index[x[i]], i + 1)

# for _ in range(q):
#         color = int(input())
#         print(index[color], end=" ")

#         # For each color, if its minimum index is less than the current minimum index,
#         # increase its index by 1
# for i in range(1, 51):
#             if index[i] < index[x[i]]:
#                 index[i] += 1

#         # Current color is at the top of the stack
# index[x[i]] = 1
# print(x)
        



