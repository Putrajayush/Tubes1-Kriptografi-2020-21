import string

message = ""
keycode = ""
enc_message = ""


def remove(string):
    return string.replace(" ", "")


def vigenere_encryption(plaintext, key):
    cipher = ""
    index = 0
    for c in plaintext:
        if c in string.ascii_lowercase:
            offset = ord(key[index]) - ord('a')

            encrypted_c = chr((ord(c) - ord('a') + offset) % 26 + ord('a'))
            cipher = cipher + encrypted_c

            index = (index + 1) % len(key)
        else:
            cipher = cipher + c

    return cipher


def vigenere_decryption(cipher, key):
    plaintext = ""
    index = 0
    for c in cipher:

        if c in string.ascii_lowercase:
            offset = ord(key[index]) - ord('a')
            decrypted_c_num = ord(c) - ord('a') - offset
            if decrypted_c_num < 0:
                decrypted_c_num = decrypted_c_num + 26

            decrypted_c = chr(decrypted_c_num + ord('a'))

            plaintext = plaintext + decrypted_c
            index = (index + 1) % len(key)

        else:
            plaintext = plaintext + c

    return plaintext


# def main():
#     plaintext = input("Masukkan Plaintext: ")
#     key = input("Masukan key: ")
#     encrypted = vigenere_encryption(plaintext, key)
#     print(encrypted)

#     decrypted = vigenere_decryption(encrypted, key)
#     print(decrypted)


# main()
