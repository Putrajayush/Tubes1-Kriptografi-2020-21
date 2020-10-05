import wave
import os
from random import seed
from random import sample

def dec(binary):
    binary = int(binary)
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return(decimal)

def extractData(audio_path, dest):
    with wave.open (audio_path, "rb") as wav_file:
        # Read audio data.
        n_frames = wav_file.getnframes()
        stegano_frames = list(wav_file.readframes(n_frames))   # Read n_frames new frames.
    
    #Find isEncrypted and insertion order 
    temp = bin(stegano_frames[0])
    isEncrypted = temp[len(temp) - 1] == 1
    #Find message Length
    message_length = ''
    for i in range(1, 25):
        temp = bin(stegano_frames[i])
        lsb = temp[len(temp) - 1]
        message_length += lsb    
    message_length = dec(message_length)
    
    message = ''
    if (not(isEncrypted)):
        for i in range(25, message_length + 25):
            temp = bin(stegano_frames[i])
            lsb = temp[len(temp) - 1]
            message += lsb
    else:
        rand_i = sample(range(25, n_frames), message_length)
        for i in range(message_length):
            temp = bin(stegano_frames[rand_i[i]])
            lsb = temp[len(temp) - 1]
            message += lsb
    i=0
    message_content = []
    while (i < message_length):
        b = ''
        for j in range(8):
            b += message[i + j]
        message_content.append(dec(b))
        i += 8

    if (isEncrypted):
        chiper = ''
        for i in range(len(message_content)):
            chiper += chr(message_content[i])
        plain = (Decrypt(chiper, Key))
        message_content = []
        for i in range(len(plain)):
            message_content.append(ord(plain[i]))
    f = open(dest, 'w+b')
    binary_format = bytearray(message_content)
    f.write(binary_format)
    f.close()
    
audio_path = 'stegano_wav/' + input("Masukan nama file stegano wav:") + '.wav'
dest = 'extracted/' + input("Masukan nama file pesan yang diekstrak:") + '.txt'
# Key = input("Masukan key enkripsi:")

# generateSeed(Key)
extractData(audio_path, dest)