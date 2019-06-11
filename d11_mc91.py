def mc91(n):
    if n > 100:
        return n - 10
    else:
        return mc91(mc91(n + 11))

def mc91_no_recursive(n):
    loop = 1
    while loop:
        if n > 100:
            n -= 10
            loop -= 1
        else:
            n += 11
            loop += 1
    return n

for i in range(80, 120):
    print(i, mc91(i), mc91_no_recursive(i))