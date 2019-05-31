def binary_search(list, item):
    n = len(list)
    left, right = 0, n-1
    count = 0
    while left < right:
        count += 1
        print(count)
        middle = (right + left) // 2
        if list[middle] == item:
            return middle
        elif list[middle] < item:
            left = middle + 1
        else:
            right = middle
    return -1

print(binary_search(list(i for i in range(0, 16)), 254))