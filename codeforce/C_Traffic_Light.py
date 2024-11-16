t=int(input())
l=[]
sum = 0
cnt = 0
    
for i in range(t):
    n=list(map(int, input()))
    y=list(map(int, input()))
    l.append([n,y])
for i in l:
    n=i[0]
    y=i[1]
    for j in range(n[0]):
        if sum != 0:
            if y[i] != 'g':
                sum += 1
            else:
                sum = 0
        else:
            if y[i] != 'g':
                sum += 1
        if sum > cnt:
            cnt = sum
    
    print(cnt)


# def solve():
#     n = int(input())
#     ch = input().strip()
#     s = input().strip()
#     s += s  # Concatenate the string with itself
#     sum = 0
#     cnt = 0
    
#     for i in range(len(s)):
#         if sum != 0:
#             if s[i] != 'g':
#                 sum += 1
#             else:
#                 sum = 0
#         else:
#             if s[i] == ch and s[i] != 'g':
#                 sum += 1
#         if sum > cnt:
#             cnt = sum
    
#     print(cnt)

# def main():
#     t = int(input())
#     for _ in range(t):
#         solve()

# if __name__ == "__main__":
#     main()
