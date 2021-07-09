from random import choice
import pytest
from param_types import linear_search, binary_search
from gene_types import *


@pytest.fixture()
def gene_setup() -> str:
    return ''.join([choice("ACGT") for _ in range(1000000)])


def test_simple_search():
    assert linear_search([1, 5, 15, 3, 2, 15, 3, 9], 3) == 3
    assert binary_search(sorted([1, 2, 3, 3, 3, 5, 15]), 3) == 2
    assert binary_search(sorted(['John', 'Alex', 'Sheila', 'Zorg']), 'Shelia') == -1


def test_speed_search_at_start(gene_setup):
    gene = sorted(str_to_gene(gene_setup))
    assert linear_search(gene, gene[0]) == 0
    assert binary_search(gene, gene[0]) == 0


def test_speed_search_at_end(gene_setup):
    gene = sorted(str_to_gene(gene_setup))
    last = len(gene) - 1
    while gene[last] == gene[last - 1]: last -= 1
    assert linear_search(gene, gene[last]) == last
    assert binary_search(gene, gene[last]) == last

