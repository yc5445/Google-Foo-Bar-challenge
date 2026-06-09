def solution(n):
    primes = [2]
    parts = ["2"]
    total_len = 1
    curr = 3
    while total_len < n + 5:
        is_prime = True
        for p in primes:
            if p * p > curr:
                break
            if curr % p == 0:
                is_prime = False
                break

        if is_prime:
            s = str(curr)
            parts.append(s)
            total_len += len(s)
            primes.append(curr)
        curr += 2
    return "".join(parts)[n:n+5]

if __name__ == "__main__":
    print(solution(0))
    print(solution(3))
