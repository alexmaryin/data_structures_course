from functools import reduce


def check_equal(first: str, second: str):
    for sym1, sym2 in zip(first, second):
        if sym1 != sym2:
            return False
    return True


def build_z_hash(string: str):
    n = len(string)
    z = [0] * n
    left, right = 0, 0
    for idx in range(1, n):
        if idx <= right:
            z[idx] = min(right - idx + 1, z[idx - 1])
        while idx + z[idx] < n and string[z[idx]] == string[idx + z[idx]]:
            z[idx] += 1
        if idx + z[idx] - 1 > right:
            left, right = right, idx + z[idx] - 1
    return z


def get_hash(string: str, length, pos=0, previous=None):
    if previous:
        h = previous - ord(string[pos - 1]) + ord(string[pos + length - 1])
    else:
        h = reduce(lambda acc, sym: acc + ord(sym), string[pos:pos + length], 0)
    # print(f'Hash for {string[pos:pos + length]} is {h}')
    return h


if __name__ == '__main__':
    pattern, text = input(), input()
    l = len(pattern)
    pattern_hash, text_hash = get_hash(pattern, l), None
    res = []
    for i in range(0, len(text) - l + 1):
        text_hash = get_hash(text, l, i, text_hash)
        if pattern_hash == text_hash and pattern == text[i: i + l]:
            res.append(str(i))
    print(' '.join(res))
