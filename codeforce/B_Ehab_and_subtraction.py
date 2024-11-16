# n,v = list(map(int,input().split()))
# arr = list(map(int,input().split()))
# Bismillahir Rahmanir Rahim
import sys
input = sys.stdin.read

def main():
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    s = set()
    s.add(0)
    
    for i in range(2, 2 + n):
        a = int(data[i])
        s.add(a)
    
    s = sorted(s)
    it = 0
    
    for i in range(k):
        if it + 1 == len(s):
            print(0)
        else:
            print(s[it + 1] - s[it])
            it += 1

if __name__ == "__main__":
    main()


