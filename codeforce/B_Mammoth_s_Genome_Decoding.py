n = int(input())
s = list(input())

a = g = c = t = 0
# to check it is divisible by 4 (4,8,12,16...)
if n % 4 != 0:
    print("===")
# count all occurance
else:
    for char in s:
        if char == "A":
            a += 1
        elif char == "G":
            g += 1
        elif char == "C":
            c += 1
        elif char == "T":
            t += 1
    # how many each have to found
    n //= 4
# how many left
    if a <= n and g <= n and c <= n and t <= n:
        a = abs(a - n)
        g = abs(g - n)
        c = abs(c - n)
        t = abs(t - n)

        result = []
    # replace based on requirment
        for char in s:
            if char == "?":
                if a > 0:
                    result.append("A")
                    a -= 1
                elif g > 0:
                    result.append("G")
                    g -= 1
                elif c > 0:
                    result.append("C")
                    c -= 1
                elif t > 0:
                    result.append("T")
                    t -= 1
            else:
                result.append(char)

        print("".join(result))
    else:
        print("===")
