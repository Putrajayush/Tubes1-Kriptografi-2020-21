import wave
import os
from random import seed
from random import sample

def decToBin(num): 
    return bin(num).replace("0b", "") 

def generateSeed(Key):
    seed_num = 0
    for i in range(len(Key)):
        seed_num += ord(Key[i])
    seed(seed_num)

def hideData(audio_path, message_path, dest, isEncrypted):
    with wave.open(audio_path, "rb") as wav_file:    # Open WAV file in read-only mode.
        # Get basic information.
        n_channels = wav_file.getnchannels()      # Number of channels. (1=Mono, 2=Stereo).
        sample_width = wav_file.getsampwidth()    # Sample width in bytes.
        framerate = wav_file.getframerate()       # Frame rate.
        n_frames = wav_file.getnframes()          # Number of frames.
        comp_type = wav_file.getcomptype()        # Compression type (only supports "NONE").
        comp_name = wav_file.getcompname()        # Compression name.

        # Read audio data.
        frames = list(wav_file.readframes(n_frames))   # Read n_frames new frames.
        temp = frames.copy()

    #Open message file and convert to bits
    filename, file_extension = os.path.splitext(message_path)
    with open(message_path, "rb") as f:
        message = f.read()
    if (file_extension == '.txt'):
        message = message.decode("utf-8")
        if (isEncrypted):
            message = Encrypt(message, Key)
        bin_message = ''.join('{0:b}'.format(ord(x)).zfill(8) for x in message)
    else:
        message = list(message)
        bin_message = ''
        for i in range(len(message)):
            bin_message += decToBin(message[i])

    l = '{0:b}'.format(len(bin_message))
    n = 8 * (len(l)//8 + 1)
    message_length = "{0:b}".format(len(bin_message)).zfill(24) #message <= 1MB
    
    #check if message length <= wav nframes
    if (len(bin_message) <= n_frames - 25):

        # Insert message in wav file
        # 1st byte for storing option : random->encrypt or sequential->not encrypt
        if ((temp[0] % 2 == 0) and (isEncrypted)):
            temp[0] += 1
        elif ((temp[0] % 2 == 1) and not(isEncrypted)):
            temp[0] -= 1
        # 2nd - 25th bytes for storing message length
        for i in range(1, 25):
            if ((temp[i] % 2 == 0) and (message_length[i-1] == '1')):
                temp[i] += 1
            elif ((temp[i] % 2 == 1) and (message_length[i-1] == '0')):
                temp[i] -= 1
        # Insert message content
        if (not(isEncrypted)):
            #sequential
            for i in range(25, len(bin_message) + 25):
                
                if ((temp[i] % 2 == 0) and (bin_message[i-25] == '1')):
                    temp[i] += 1
                elif ((temp[i] % 2 == 1) and (bin_message[i-25] == '0')):
                    temp[i] -= 1
        else:
            #random
            rand_i = sample(range(25, n_frames), len(bin_message))
            for i in range(len(bin_message)):
                if ((temp[rand_i[i]] % 2 == 0) and (bin_message[i] == '1')):
                    temp[rand_i[i]] += 1
                elif ((temp[rand_i[i]] % 2 == 1) and (bin_message[i] == '0')):
                    temp[rand_i[i]] -= 1

        stegano_frames = bytes(temp)
        # Duplicate to a new WAV file.
        with wave.open(dest, "wb") as wav_file2:    # Open WAV file in write-only mode.
            # Write audio data.
            params = (n_channels, sample_width, framerate, n_frames, comp_type, comp_name)
            wav_file2.setparams(params)
            wav_file2.writeframes(stegano_frames)
        

random = int(input(
    "1. Sequential\n2. Random\nPilih sequential atau random: "))
if(random == 1):
    isEncrypted = False
    audio_path = 'wav/' + input("Masukkan nama file wav:") + '.wav'
    message_path = 'message/' + input("Masukkan nama file berisi pesan:") + '.txt'
    dest = 'stegano_wav/' + input("Masukkan nama file wav stegano:") + '.wav'
elif(random == 2):
    isEncrypted = True
    audio_path = 'wav/' + input("Masukkan nama file wav:") + '.wav'
    message_path = 'message/' + input("Masukkan nama file berisi pesan:") + '.txt'
    dest = 'stegano_wav/' + input("Masukkan nama file wav stegano:") + '.wav'
    Key = input("Masukkan key enkripsi:")
    generateSeed(Key)
else:
    raise Exception("Enter correct input")


hideData(audio_path, message_path, dest, isEncrypted)