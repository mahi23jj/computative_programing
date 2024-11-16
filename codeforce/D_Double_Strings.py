def solve():
    n = int(input())
    s = []
    mp = {}
    
    for _ in range(n):
        word = input()
        s.append(word)
        mp[word] = True

    for word in s:
        ok = False
        for j in range(1, len(word)):
            pref = word[:j]
            suff = word[j:]
            if mp.get(pref) and mp.get(suff):
                ok = True
                break
        print(1 if ok else 0, end='')
    print()

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
