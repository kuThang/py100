def permutation(values):
    n = len(values)

    for i in (reversed(range(n-1))):
        if values[i] < values[i+1]:
            break
    else:
        # values[:] = reversed(values[:])
        return (True, values)
    
    for j in reversed(range(i, n)):
        if values[i] < values[j]:
            # swap
            values[i], values[j] = values[j], values[i]
            values[i+1:] = reversed(values[i+1:])
            break
    return (False, values)

a = [3, 2, 6, 5, 4, 1]
finish = False

while not finish:
# for i in range(10):
    finish, a = permutation(a)
    print(a)
