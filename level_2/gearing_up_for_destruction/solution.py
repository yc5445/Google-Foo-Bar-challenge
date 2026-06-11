def solution(pegs):
    r1 = [pegs[1] - pegs[0], 1]
    min_s_even = r1[0]
    max_s_odd = 0

    for i in range(2, len(pegs)):
        if i % 2 == 0:
            r1[0] += -pegs[i] + pegs[i-1]
            if r1[0] > max_s_odd:
                max_s_odd = r1[0]
        else:
            r1[0] += pegs[i] - pegs[i-1]
            if r1[0] < min_s_even:
                min_s_even = r1[0]
    r1[0] *= 2

    if len(pegs) % 2 == 0:
        if r1[0] % 3 == 0:
            r1[0] //= 3
        else:
            r1[1] = 3
    if (r1[0] < (max_s_odd + 1) * r1[1] or
        r1[0] > (min_s_even - 1) * r1[1]):
        r1[0] = -1
        r1[1] = -1

    return r1

if __name__ == "__main__":
    print(solution([4, 30, 50]))
    print(solution([4, 17, 50]))
    print(solution([1, 3]))
