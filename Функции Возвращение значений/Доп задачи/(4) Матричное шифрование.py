def encrypt(text: str, size: int) -> str:
    text += (size - (len(text)) % size) * ' '
    encrypted_text = ''
    i1 = 0
    i2 = 0
    for i in range(len(text)):
        encrypted_text += text[i1]
        i1 += size
        if i1 >= len(text):
            i2 += 1
            i1 = i2

    return encrypted_text

def decrypt(encrypted_text: str, size: int) -> str:
    text = ''
    table_size = len(encrypted_text) // size
    i1 = 0
    i2 = 0
    for i in range(len(encrypted_text)):
        text += encrypted_text[i1]
        i1 += table_size
        if i1 >= len(encrypted_text):
            i2 += 1
            i1 = i2
    return text
