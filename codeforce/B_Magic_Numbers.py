# x=list(map(int, input()))
# t='Yes'
# for i in range(len(x)):
#     if x[i]==1 and x[i]==4:
#         if x[i]==4:
#             if i-1 and i-2 >=0:
#                 if x[i-1]!=1 or x[i-1]!=4 and x[i-2]!=1:
#                     t='No'
#                     break
#     else:
#         t='No'
#         break
# print(t)
x = input()
s = str(x)

i = 0
t = "YES"

while i < len(s):

    if s[i : i + 3] == "144":
        i += 3

    elif s[i : i + 2] == "14":
        i += 2

    elif s[i] == "1":
        i += 1
    else:
        t = "NO"
        break

print(t)
