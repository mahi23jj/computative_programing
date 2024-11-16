n = int(input())
x = list(map(int, input().split()))

math = []
prog = []
eu = []

for i in range( n ):
    if x[i] == 1:
        prog.append(i)
    elif x[i] == 2:
        math.append(i)
    elif x[i] == 3:
        eu.append(i)

ans = min(len(math), len(prog), len(eu))
print(ans)

for i in range(ans):
    print(math[i]+1, prog[i]+1, eu[i]+1)
