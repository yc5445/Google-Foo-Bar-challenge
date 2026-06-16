def parent(h, node):
    root = (1 << h) - 1
    if node == root:
        return -1
    current = root
    height = h

    while height > 1:
        left_root = current - (1 << (height - 1))
        right_root = current - 1
        if node == left_root or node == right_root:
            return current
        if node < left_root:
            current = left_root
        else:
            current = right_root
        height -= 1
    return -1

def solution(h, q):
    return [parent(h, x) for x in q]

if __name__ == "__main__":
    print(solution(3, [7, 3, 5, 1]))
    print(solution(5, [19, 14, 28]))

