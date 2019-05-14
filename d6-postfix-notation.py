ops = {
    '+' : float.__add__,
    '-' : float.__sub__,
    '/' : float.__truediv__,
    '*' : float.__mul__,
    '^' : float.__pow__
}

def postfix(input):
    arr = input.split(' ')
    temp = []
    for item in arr:
        if item not in ops:
            ret = float(item)
        else:
            ret = ops[item](temp.pop(-2), temp.pop(-1))
            
        temp.append(ret)

    return temp.pop()

n = postfix('1 2 + 4 3 - + 10 5 / *')
print(n)
