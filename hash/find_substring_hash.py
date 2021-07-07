class HashSearch:
    def __init__(self):
        self.P = 1000000007
        self.X = 263
        self.squads = {0: 1}
        self.memo = []

    def get_squad_mod(self, x):
        if x not in self.squads:
            self.squads[x] = self.get_squad_mod(x - 1) * self.X % self.P
        return self.squads[x]

    def get_full_hash(self, string, length=-1):
        hash_code = 0
        for idx, sym in enumerate(string):
            hash_code += ord(sym) * self.get_squad_mod(idx)
            if length > 0:
                self.memo.append(ord(sym) * self.get_squad_mod(length - 1))
        print(f'hash for {string} is {hash_code % self.P}')
        return hash_code % self.P

    def slide_hash(self, text, left, right, previous):
        hash_code = ord(text[left]) + previous - self.memo[len(text) - right - 1]
        self.memo.append(ord(text[left]) * self.get_squad_mod(right - left))
        print(f'hash for slide {text[left:right + 1]} is {hash_code}')
        return hash_code


if __name__ == '__main__':
    pattern, text = input(), input()
    assert len(pattern) <= len(text)
    left = len(text) - len(pattern)
    search = HashSearch()
    hash_pattern, hash_str = search.get_full_hash(pattern), search.get_full_hash(text[left:], len(pattern))
    res = []
    for idx in range(left, 1, -1):
        if hash_str == hash_pattern and text[idx:idx + len(pattern)] == pattern:
            res.append(str(idx))
        hash_str = search.slide_hash(text, idx - 1, idx + len(pattern) - 2, hash_str)
    print(' '.join(res))
