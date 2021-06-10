from secrets import token_bytes
from typing import Tuple


def random_key(length):
    token = token_bytes(length)
    return int.from_bytes(token, "big")


def encrypt(original) -> Tuple[int, int]:
    original_bytes = str(original).encode()
    dummy = random_key(len(original_bytes))
    original_key = int.from_bytes(original_bytes, "big")
    encrypted = original_key ^ dummy
    return dummy, encrypted


def decrypt(key1, key2):
    decrypted: int = key1 ^ key2
    temp = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()


if __name__ == "__main__":
    key1, key2 = encrypt("This is my own string!")
    print(key1, key2)
    result = decrypt(key1, key2)
    print(result)
