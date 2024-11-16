# n,k=map(int, input().split())
# x=list(map(int, input().split()))
# y=list(map(int, input().split()))
# pf=[0]*len(x)
# pf[0]=x[0]
# l=0
# for i in range(1,len(x)):
#     pf[i]=pf[i-1]+x[i]


# for i in range(len(x)):
#     if i+k-1<len(x):
#         if y[i]==0:
#             l=pf[i+k-1]
#             break
# print(l)
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    a = [0] * n
    t = [0] * n
    cs = [0] * (n + 1)
    
    index = 2
    for i in range(n):
        a[i] = int(data[index])
        index += 1
    
    res = 0
    for i in range(n):
        t[i] = int(data[index])
        index += 1
        if t[i]:
            res += a[i]
            a[i] = 0
    
    cs[0] = 0
    for i in range(1, n + 1):
        cs[i] = a[i - 1] + cs[i - 1]
    
    tmp = 0
    for i in range(m, n + 1):
        tmp = max(tmp, cs[i] - cs[i - m])
    
    print(res + tmp)

if __name__ == "__main__":
    main()
