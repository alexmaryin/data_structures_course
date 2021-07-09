from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]


def str_to_gene(s: str) -> Gene:
    gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            return gene
        codon = (Nucleotide[s[i]], Nucleotide[s[i+1]], Nucleotide[s[i+2]])
        gene.append(codon)
    return gene


def gene_to_str(gene: Gene, separator='-') -> str:
    return separator.join([f'{c[0]}{c[1]}{c[2]}' for c in gene])


def codon_search(gene: Gene, key: Codon) -> int:
    low, high = 0, len(gene) - 1
    while low <= high:
        mid = (low + high) // 2
        if gene[mid] < key:
            low = mid + 1
        elif gene[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1

