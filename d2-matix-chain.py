def mult(chain):
    n = len(chain)
    cost = 0
    order = '()'
    rows = 0
    cols = 0
    if n is 2:
        cost = chain[-2][1] *  chain[-2][2] *  chain[-1][2]
        order = '(' + chain[-2][0] + chain[-1][0] + ')'
        rows =  chain[-2][1]
        cols =  chain[-1][2]
    else:
        (c1, o1, r1, col1) = mult(chain[1:])
        (s_cost, s_order, s_rows, s_cols) = mult([chain[0], (o1, r1, col1)])
        s_cost = s_cost + c1

        (c1, o1, r1, col1) = mult(chain[:-1])
        (e_cost, e_order, e_rows, e_cols) = mult([(o1, r1, col1), chain[-1]])
        e_cost = e_cost + c1


        if e_cost > s_cost:
            return (s_cost, s_order, s_rows, s_cols)
        else:
            return (e_cost, e_order, e_rows, e_cols)

    return (cost, order, rows, cols)

print(mult([('A', 10, 20), ('B', 20, 10), ('D', 10, 100), ('C', 100, 10), ('E', 10, 100), ('F', 100, 10)]))

def mult2(chain):
    n = len(chain)
    
    # single matrix chain has zero cost
    aux = {(i, i): (0,) + chain[i] for i in range(n)}
    # print(aux)
    # i: length of subchain
    for i in range(1, n):
        # j: starting index of subchain
        for j in range(0, n - i):
            best = float('inf')
            # k: splitting point of subchain
            for k in range(j, j + i):
                # multiply subchains at splitting point
                lcost, lname, lrow, lcol = aux[j, k]
                rcost, rname, rrow, rcol = aux[k + 1, j + i]
                cost = lcost + rcost + lrow * lcol * rcol
                var = '(%s%s)' % (lname, rname)
                # print(var)
                # pick the best one
                if cost < best:
                    best = cost
                    aux[j, j + i] = cost, var, lrow, rcol
    return dict(zip(['cost', 'order', 'rows', 'cols'], aux[0, n - 1]))
print(mult2([('A', 10, 20), ('B', 20, 10), ('C', 10, 100), ('D', 100, 10), ('E', 10, 100), ('F', 100, 10)]))