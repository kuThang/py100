from itertools import zip_longest

T = [(0,0), (1,0), (1,0), (0,1), 
     (1,0), (0,1), (0,1), (1,1)]

def add1(x,y):
    x = list(map(int, reversed(x)))
    y = list(map(int, reversed(y)))
    sum=[]
    print(x)
    print(y)
    v, t = T[0]
    for a, b in zip_longest(x, y, fillvalue=0):
        v, t = T[t * 4 + a * 2 + b]
        sum.append(v)
    sum.append(T[t * 4][0])
    print(sum)
    return ''.join(list(map(str, reversed(sum))))

print(add1('10100100100111', '100100011011'))

v0c0 = 0, {}
v1c0 = 1, {}
v0c1 = 0, {}
v1c1 = 1, {}

no_carry_update = {(0,0): v0c0, (0,1): v1c0, (1,0): v1c0, (1,1): v0c1}
carry_update = {(0,0): v1c0, (0,1): v0c1, (1,0): v0c1, (1,1): v1c1}

v0c0[1].update(no_carry_update)
v1c0[1].update(no_carry_update)
v0c1[1].update(carry_update)
v1c1[1].update(carry_update)

def add2(x, y):
    x = list(map(int, reversed(x)))
    y = list(map(int, reversed(y)))
    sum=[]
    print(x)
    print(y)
    value, transition = v0c0
    for a, b in zip_longest(x, y, fillvalue=0):
        value, transition = transition[a, b]
        sum.append(value)
    sum.append(transition[0, 0][0])

    print(sum)
    return ''.join(list(map(str, reversed(sum))))


print(add2('10100100100111', '100100011011'))