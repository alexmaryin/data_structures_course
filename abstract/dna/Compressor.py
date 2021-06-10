import random


class CompressedGene:
    def __init__(self, gene: str):
        self.compressed = 0
        self.compress(gene)

    def compress(self, gene):
        self.compressed = 1
        for nucleotide in gene.upper():
            self.compressed <<= 2
            self.compressed |= {"A": 0b00, "C": 0b01, "G": 0b10, "T": 0b11}[nucleotide]

    def decompress(self):
        gene = ""
        for i in range(0, self.compressed.bit_length() - 1, 2):
            bits = self.compressed >> i & 0b11
            gene += {0b00: "A", 0b01: "C", 0b10: "G", 0b11: "T"}[bits]
        return gene[::-1]

    def __str__(self):
        return self.decompress()


if __name__ == '__main__':
    from sys import getsizeof
    origin = ''.join([random.choice("ACGT") for _ in range(0, 100000)])
    print(f'Origin string in {getsizeof(origin)} bytes')
    compressed = CompressedGene(origin)
    print(f'Compressed gene in {getsizeof(compressed.compressed)} bytes')
    assert origin == compressed.decompress()

