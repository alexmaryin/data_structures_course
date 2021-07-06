from typing import List


class HashStrings:
    def __init__(self, size):
        self.p = 1000000007
        self.x = 263
        self.squads = {0: 1}
        self.buckets: List[List[str]] = [[] for _ in range(size)]

    def get_squad_mod(self, x):
        if x not in self.squads:
            self.squads[x] = self.get_squad_mod(x - 1) * self.x % self.p
        return self.squads[x]

    def get_hash(self, string: str):
        hash_code = 0
        for idx, sym in enumerate(string):
            hash_code += ord(sym) * self.get_squad_mod(idx)
        hash_code = hash_code % self.p % len(string)
        print(f'hash for {string} is {hash_code}')
        return hash_code

    def add_string(self, string):
        hash_code = self.get_hash(string)
        if len(self.buckets[hash_code]) != 0 and string in self.buckets[hash_code]:
            return
        self.buckets[hash_code].append(string)

    def del_string(self, string):
        hash_code = self.get_hash(string)
        if len(self.buckets[hash_code]) != 0 and string in self.buckets[hash_code]:
            self.buckets[hash_code].remove(string)

    def find_string(self, string):
        hash_code = self.get_hash(string)
        return len(self.buckets[hash_code]) != 0 and string in self.buckets[hash_code]

    def check_bucket(self, bucket: int):
        if len(self.buckets[bucket]) != 0:
            return ' '.join(list(reversed(self.buckets[bucket])))
        else:
            return ''
