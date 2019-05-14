print("Start Hanoi tower")

def doHNTower(height, left='left', middle='middle', right='right'):
    if height:
        doHNTower(height - 1, left, right, middle)
        print(left, ' => ', right)
        doHNTower(height - 1, middle, left, right)

doHNTower(4)