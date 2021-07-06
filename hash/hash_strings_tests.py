import pytest
from hash_strings import HashStrings


@pytest.fixture()
def new_hash() -> HashStrings:
    return HashStrings(5)


def test_hash_squads(new_hash):
    squads = [new_hash.get_squad_mod(x) for x in range(2)]
    assert squads == [1, 263]


def test_hash_squads_15(new_hash):
    refs = [263 ** x % 1000000007 for x in range(15)]
    squads = [new_hash.get_squad_mod(x) for x in range(15)]
    print(squads)
    assert squads == refs


def test_from_stepik_1(new_hash: HashStrings):
    results = []
    new_hash.add_string('world')
    new_hash.add_string('HellO')
    results.append(new_hash.check_bucket(4))
    results.append('yes' if new_hash.find_string('World') else 'no')
    results.append('yes' if new_hash.find_string('world') else 'no')
    new_hash.del_string('world')
    results.append(new_hash.check_bucket(4))
    new_hash.del_string('hellO')
    new_hash.add_string('luck')
    new_hash.add_string('GooD')
    results.append(new_hash.check_bucket(2))
    new_hash.del_string('good')
    assert results == ['HellO world', 'no', 'yes', 'HellO', 'GooD luck']


if __name__ == '__main__':
    size = int(input())
    h = HashStrings(size)
    coms = int(input())
    res = []
    for _ in range(coms):
        command = input().split()
        if command[0] == 'add':
            h.add_string(command[1])
        if command[0] == 'check':
            res.append(h.check_bucket(int(command[1])))
        if command[0] == 'del':
            h.del_string(command[1])
        if command[0] == 'find':
            res.append('yes' if new_hash.find_string(command[1]) else 'no')
    for l in res: print(l)



