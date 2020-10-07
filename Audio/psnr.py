import librosa
import numpy as np
import math

def PSNR(amp_original, amp_stegano):
    ssd = 0
    for i in range(len(amp_original)): #len(amp_original) == len(amp_stegano)
        ssd += np.square(amp_original[i] - amp_stegano[i])
    rms = np.sqrt(ssd/(len(amp_original * amp_stegano)))
    return (20 * math.log10(255/rms))

ori = 'wav/' + input("Audio Asli:") + '.wav'
steg = 'stegano_wav/' + input("Audio Stegano:") + '.wav'
amp_original, sr = librosa.load(ori)
amp_stegano, sr2 = librosa.load(steg)

if (len(amp_original) == len(amp_stegano)):
	print("\nHasil = " , PSNR(amp_original, amp_stegano) , "dB")
else:
	print("\nError : Banyak frames kedua audio tidak sama")


print("\n")