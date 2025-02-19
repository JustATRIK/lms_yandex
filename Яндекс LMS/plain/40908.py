def to_code(alphabet: str, line: str) -> list[int]:
    line_codes = list(line)
    for i in range(len(line_codes)):
        line_codes[i] = alphabet.index(line_codes[i])
    return line_codes


def from_code(alphabet: str, code: list[int]) -> str:
    return ''.join([alphabet[i] for i in code])


def crypt(alphabet: str, line: str, key: str) -> str:
    line_codes = to_code(alphabet, line)
    key_codes = to_code(alphabet, key)
    encrypted_code = [0] * len(line_codes)
    for i in range(len(line_codes)):
        encrypted_code[i] = (line_codes[i] + key_codes[i % len(key_codes)]) % len(alphabet)
    return from_code(alphabet, encrypted_code)


def decrypt(alphabet: str, res: str, key: str) -> str:
    res_codes = to_code(alphabet, res)
    key_codes = to_code(alphabet, key)
    decrypted_code = [0] * len(res_codes)
    for i in range(len(res)):
        decrypted_code[i] = (res_codes[i] - key_codes[i % len(key_codes)])
        if decrypted_code[i] < 0:
            decrypted_code[i] += len(alphabet)
    return from_code(alphabet, decrypted_code)
