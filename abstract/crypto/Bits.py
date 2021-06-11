class Bits:
    def __init__(self):
        self.item: int = 1

    def __getitem__(self, item):
        return self.item >> item & 0b11

    def next_bits(self):
        for idx in range(0, self.item.bit_length() - 1, 2):
            yield self.__getitem__(idx)

    def __iadd__(self, other):
        self.item <<= 2
        self.item |= other
        return self

    def __repr__(self):
        return ''.join(str(s) for s in self.next_bits())


class CompressedGene2:
    def __init__(self, gene: str):
        self.compressed = Bits()
        for nucleotide in gene.upper():
            self.compressed += {"A": 0b00, "C": 0b01, "G": 0b10, "T": 0b11}[nucleotide]

    def decompress(self):
        gene = ''.join({0b00: "A", 0b01: "C", 0b10: "G", 0b11: "T"}[bits] for bits in self.compressed.next_bits())
        return gene[::-1]

    def __str__(self):
        return self.compressed.__str__()
