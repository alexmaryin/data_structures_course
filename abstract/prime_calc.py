from utils.time_measuring import measured_time


@measured_time
def primes(n) -> list[int]:
    assert n > 2
    nxt = 2
    numbers = [True for _ in range(n)]
    while nxt * nxt <= n:
        if numbers[nxt]:
            for index in range(n - nxt):
                step = nxt * nxt + index * nxt
                if step < n:
                    numbers[step] = False
                else:
                    break
        nxt += 1
    return [idx for idx, is_prime in enumerate(numbers) if idx >= 2 and is_prime]


if __name__ == '__main__':
    print(primes(10000000)[-1])
