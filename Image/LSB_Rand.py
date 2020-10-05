from cv2 import cv2
import numpy as np
import types
import math
import vigenere_cipher
import random


def psnr(img1, img2):
    rms = math.sqrt(np.sum((img1.astype('float') - img2.astype('float'))
                           ** 2) / (img1.shape[1] * img1.shape[0]))
    return 20 * math.log10(256 / rms)


def generate_seed(key):
    return sum([ord(a) for a in key])


def messageToBinary(message):
    if type(message) == str:
        return ''.join([format(ord(i), "08b") for i in message])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [format(i, "08b") for i in message]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "08b")
    else:
        raise TypeError("Input Invalid")


def hideData(image, secret_message, key):

    # Maximum bytes to encode
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8
    #print("Maximum bytes:", n_bytes)

    # Checking length of byte to encode
    if len(secret_message) > n_bytes:
        raise ValueError(
            "Input Invalid, Panjang pesan melebihi ukuran image")

    # Delimiter
    secret_message += "#####"

    data_index = 0
    binary_secret_msg = messageToBinary(secret_message)

    seed = generate_seed(key)
    data_len = len(binary_secret_msg)

    random.seed(seed)
    pixel_arr = random.sample(range(image.shape[1]), (data_len+5)//3)

    i = 0
    while i < (data_len+5):
        for i in pixel_arr:
            pixel = image[i, i]
            r, g, b = messageToBinary(pixel)

            # Modify the LSB
            if data_index < data_len:
                # red pixel
                pixel[0] = int(r[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # green pixel
                pixel[1] = int(g[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # blue pixel
                pixel[2] = int(b[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index >= data_len:
                break
        i += 3
    return image


def showData(image, key):

    seed = generate_seed(key)
    random.seed(seed)
    pixel_arr = random.sample(
        range(image.shape[1]), image.shape[0]*image.shape[1])

    binary_data = ""

    i = 0
    while i < (image.shape[0]*image.shape[1]):
        for i in pixel_arr:
            pixel = image[i, i]
            r, g, b = messageToBinary(pixel)
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]
        i += 3
    return image

    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
    decoded_data = ""

    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "#####":
            break

    return decoded_data[:-5]


def encode_text(key):
    image_name = input("Masukan nama file dan extensionnya: ")
    image = cv2.imread(image_name)

    print("Bentuk dari Image adalah: ", image.shape)

    data = input("Masukan file yang akan disisipkan: ")
    if (len(data) == 0):
        raise ValueError('File Kosong')

    filename = input(
        "Masukan nama image keluaran dan extensionnya: ")
    encoded_image = hideData(image, data, key)
    cv2.imwrite(filename, encoded_image)


def encode_text_vigenere(key):
    image_name = input("Masukan nama file dan extensionnya: ")
    image = cv2.imread(image_name)

    print("Bentuk dari Image adalah: ", image.shape)

    data = input("Masukan file yang akan disisipkan: ")
    if (len(data) == 0):
        raise ValueError('File Kosong')

    data = str(data)
    data = vigenere_cipher.vigenere_encryption(str(data), key)

    filename = input(
        "Masukan nama image keluaran dan extensionnya: ")
    encoded_image = hideData(image, data, key)
    cv2.imwrite(filename, encoded_image)


def decode_text(key):

    image_name = input(
        "Masukan nama file steganografi dan extensionnya: ")
    image = cv2.imread(image_name)

    msg = showData(image, key)
    return msg


def decode_text_vigenere(key):

    image_name = input(
        "Masukan nama file steganografi dan extensionnya: ")
    image = cv2.imread(image_name)

    msg = str(showData(image, key))
    msg = vigenere_cipher.vigenere_decryption(msg, key)
    return msg


def main():
    a = input(
        "LSB Image Steganography \n1. Penyisipan Pesan\n2. Ekstrasi Pesan\nMasukan Pilihan: ")

    userinput = int(a)

    if(userinput == 1):
        vigenere = int(input(
            "1. Memakai Enkripsi Vigenere Cipher\n2. Tidak memakai enkripsi\nMasukan Pilihan:"))
        if(vigenere == 1):
            key = input("Masukan key untuk enkripsi: ")
            encode_text_vigenere(key)
        elif(vigenere == 2):
            key = input("Masukan key untuk random: ")
            encode_text(key)
        else:
            raise Exception("Input Invalid")

    elif(userinput == 2):
        vigenere = int(input(
            "1. Memakai Enkripsi Vigenere Cipher\n2. Tidak memakai enkripsi\nMasukan Pilihan:"))
        if(vigenere == 1):
            key = input("Masukan key untuk dekripsi: ")
            print("Decoded message: " + decode_text_vigenere(key))
        elif(vigenere == 2):
            key = input("Masukan key untuk random: ")
            print("Decoded message: " + decode_text(key))
        else:
            raise Exception("Input Invalid")

    else:
        raise Exception("Input Invalid")


main()
