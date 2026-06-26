def solution(l):
    count = [0] * len(l)
    triples = 0

    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                count[i] += 1
                triples += count[j]
    return triples

if __name__ == "__main__":
    print(solution([1, 1, 1]))
    print(solution([1, 2, 3, 4, 5, 6]))