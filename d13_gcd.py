def gcd1(x,y):
    if x < y : return gcd1(y, x)

    u = x // y
    v = x % y
    print(x, y, u, v)
    if u == 0 : return 1
    if v == 0 : return y
    else: return gcd1(y, v)

def gcd2(x, y):
    if x < y: return gcd2(y, x)
    u0 , v0 = 1, 0  # x = u0*x + v0*y
    u1, v1 = 0, 1   # y = u1*x + v1*y
    while y :
        q = x // y
        r = x % y
        u0, u1 = u1, u0 - q * u1    # y = u1 * x + v1 * y
        v0, v1 = v1, v0 - q * v1    # r = x - y * q = (u0 - q*u1)x - (v0 - q*v1)y

        x = y
        y = r
    return x, u0, v0

print(gcd1(198, 252))
print(gcd2(198, 252))