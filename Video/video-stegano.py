#!/usr/bin/env python
# coding: utf-8

# In[79]:


#vigenere Extended
from textwrap import wrap

def generateKey(string, key): 
	key = list(key) 
	if len(string) == len(key): 
		return(key) 
	else: 
		for i in range(len(string) - len(key)): 
			key.append(key[i % len(key)]) 
	return("" . join(key)) 

def encryptByteExtendedVigenere(bytePlainText, key):
    result = [[0] for i in range(len(bytePlainText))]
    key = key.strip().upper()
    keyIndex = 0
    keylength = len(key)
    for i in range(len(bytePlainText)):
        keyIndex = keyIndex % keylength
        shift = ord(key[keyIndex]) - 65
        result[i] = bytes([(ord(bytePlainText[i]) + shift) % 256])
        keyIndex+=1
    return result

def decryptByteExtendedVigenere(byteCipherText, key):
    result = [[0] for i in range(len(byteCipherText))]
    key = key.strip().upper()
    keyIndex = 0
    keylength = len(key)
    for i in range(len(byteCipherText)):
        keyIndex = keyIndex % keylength
        shift = ord(key[keyIndex]) - 65
        result[i] = bytes([(ord(byteCipherText[i]) + 256 - shift) % 256])
        keyIndex+=1
    return result

def encryptTextExtendedVigenere(plaintext, key):
    result = [[0] for i in range(len(plaintext))]
    key = key.strip().upper()
    keyIndex = 0
    keylength = len(key)
    for i in range(len(plaintext)):
        keyIndex = keyIndex % keylength
        shift = ord(key[keyIndex]) - 65
        result[i] = chr((ord(plaintext[i]) + shift) % 256)
        keyIndex+=1
    return ''.join(i for i in result)

def decryptTextExtendedVigenere(cipherText, key):
    result = [[0] for i in range(len(cipherText))]
    key = key.strip().upper()
    keyIndex = 0
    keylength = len(key)
    for i in range(len(cipherText)):
        keyIndex = keyIndex % keylength
        shift = ord(key[keyIndex]) - 65
        result[i] = chr((ord(cipherText[i]) + 256 - shift) % 256)
        keyIndex+=1
    return ''.join(i for i in result)

def wrapFiveCharacters(message):
    messageWrapFive = wrap(message,5)
    return ' '.join(messageWrapFive)

def write_to_file(path, text):
    file1 = open(path,"w+") 
    file1.write(text) 
    file1.close()

def readTextFromFile(path):
    file1 = open(path, "r")
    data = file1.read()
    file1.close()
    return data


# In[80]:


def get_bytes_from_file(filename):  
    return open(filename, "rb").read()


# In[81]:





# In[82]:


bytes = get_bytes_from_file("Tubes1-Kripto-2020.pdf")
print(type(bytes))


# In[83]:





# In[84]:


print(encryptTextExtendedVigenere("Saya makan nasi", "STEGANO"))


# In[85]:


print(decryptTextExtendedVigenere("et}g zo}tr&nn{", "STEGANO"))


# In[86]:


import cv2
import os
import random
import numpy as np
import types

def frame_extraction(video):
    if not os.path.exists("./temp_folder"):
        os.makedirs("temp_folder")
    vidcap = cv2.VideoCapture(video)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    #print("fps: ", end="")
    #print(fps)
    vidcap.set(cv2.CAP_PROP_FPS, fps) 
    success, image = vidcap.read()

    count=0
    temp_folder="temp_folder"
    while True:
        success, image = vidcap.read()
        if not success:
            break
        cv2.imwrite(os.path.join(temp_folder, "{:d}.png".format(count)), image)
        count += 1
    return count


# In[87]:


import cv2
import os
import random
import numpy as np
import types
from subprocess import call,STDOUT
call(["ffmpeg", "-i","video/sample-avi-file.avi" , "-q:a", "0", "-map", "a", "tmp/audio.mp3", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)


# In[88]:





# In[89]:


key="STEGANO"
sd=0
print(len(key))
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(key)):
    sd+=int(alphabet.index(key[i].lower()))
random.seed(sd)


# In[90]:


def messageToBinary(message):
  if type(message) == str:
    return ''.join([ format(ord(i), "08b") for i in message ])
  elif type(message) == bytes or type(message) == np.ndarray:
    return [ format(i, "08b") for i in message ]
  elif type(message) == int or type(message) == np.uint8:
    return format(message, "08b")
  else:
    raise TypeError("Input type not supported")


# In[91]:





# In[92]:


def prod_seed(key):
    sd=0
    #print(len(key))
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(key)):
        sd+=int(alphabet.index(key[i].lower()))
    random.seed(sd)
    return sd


# In[93]:


print(prod_seed("STEGANO"))


# In[94]:


def randomized_pixels_frames(sd, count, jum_frame):
    random.seed(sd)
    jum_frame_max=count
    #jum_frame = 0
    image = cv2.imread("temp_folder/0.png")
    
    
    jum_pixel=image.shape[0]*image.shape[1]*image.shape[2]
    
    print(jum_frame)

    frame_randomized=[]
    for i in range(jum_frame):
        frame_randomized.append(random.randint(1, count))
    return frame_randomized


# In[95]:





# In[96]:


randomized_pixels_frames


# In[97]:


def messageToBinary(message):
    if type(message) == str:
        return ''.join([ format(ord(i), "08b") for i in message ])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [ format(i, "08b") for i in message ]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "08b")
    else:
        #raise TypeError("Input type not supported")
        return [ format(i, "08b") for i in message ]


# In[98]:


print(messageToBinary("Saya"))
print(len(messageToBinary("Saya")))


# In[99]:


def message_length(message):
    return len(messageToBinary(message))


# In[100]:


print(message_length("Saya"))


# In[101]:


def num_of_pixels():
    image = cv2.imread("temp_folder/0.png")
    return image.shape[0]*image.shape[1]*image.shape[2]


# In[102]:


print(num_of_pixels())


# In[103]:


def num_of_frames(message):
    return message_length(message)//num_of_pixels()+1


# In[104]:


print(num_of_frames("Saya"))


# In[105]:


import math
def split_string(s_str,count=10):
    per_c=math.ceil(len(s_str)/count)
    c_cout=0
    out_str=''
    split_list=[]
    for s in s_str:
        out_str+=s
        c_cout+=1
        if c_cout == per_c:
            split_list.append(out_str)
            out_str=''
            c_cout=0
    if c_cout!=0:
        split_list.append(out_str)
    return split_list


# In[106]:


print(split_string("Saya makan nasi",1))


# In[107]:


def hideData(image, secret_message):

  
  n_bytes = image.shape[0] * image.shape[1] * 3 // 8
  print("Maximum bytes to encode:", n_bytes)

  
  if len(secret_message) > n_bytes:
      raise ValueError("Error encountered insufficient bytes, need bigger image or less data !!")
  
  secret_message += "#####" 

  data_index = 0
  
  binary_secret_msg = messageToBinary(secret_message)

  data_len = len(binary_secret_msg) 
  for values in image:
      for pixel in values:
          
          r, g, b = messageToBinary(pixel)
          
          if data_index < data_len:
              
              pixel[0] = int(r[:-1] + binary_secret_msg[data_index], 2)
              data_index += 1
          if data_index < data_len:
              
              pixel[1] = int(g[:-1] + binary_secret_msg[data_index], 2)
              data_index += 1
          if data_index < data_len:
              
              pixel[2] = int(b[:-1] + binary_secret_msg[data_index], 2)
              data_index += 1
          
          if data_index >= data_len:
              break

  return image


# In[108]:


def showData(image):

  binary_data = ""
  for values in image:
      for pixel in values:
          r, g, b = messageToBinary(pixel) 
          binary_data += r[-1] 
          binary_data += g[-1] 
          binary_data += b[-1] 
  
  all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8) ]
  
  decoded_data = ""
  for byte in all_bytes:
      decoded_data += chr(int(byte, 2))
      if decoded_data[-5:] == "#####": 
          break
  
  return decoded_data[:-5] 


# In[109]:


# Encode data into image 
def encode_text(image_name, data): 
  
  image = cv2.imread(image_name) 
  
  
  
  resized_image = cv2.resize(image, (500, 500)) 
  cv2.imshow('image', resized_image)
  
      
  #data = input("Enter data to be encoded : ") 
  if (len(data) == 0): 
    raise ValueError('Data is empty')
  
  
  encoded_image = hideData(image, data) 
  cv2.imwrite(image_name, encoded_image)


# In[ ]:





# In[110]:



def decode_text(image_name):
  
  
  image = cv2.imread(image_name) 

  
  resized_image = cv2.resize(image, (500, 500))  
  cv2.imshow('image', resized_image) 
    
  text = showData(image)
  return text


# In[113]:


# Image Steganography         
def Steganography(): 
    a = input("Video Steganography \n 1. Penyisipan Pesan \n 2. Ekstraksi Pesan \n Your input is: ")
    userinput = int(a)
    if (userinput == 1):
        a = input("1. Tanpa Enkripsi \n 2. Dengan Enkripsi \n Your input is: ")
        userinput = int(a)
        if (userinput == 1):
            a = input("1. Frame sekuensial \n 2. Frame acak \n Your input is: ")
            userinput = int(a)
            if (userinput == 1):
                a = input("1. Pixel-pixel Sekuensial \n 2. Pixel-pixel acak \n Your input is: ")
                userinput = int(a)
                if (userinput == 1):
                    key = input("Masukkan kunci: ")
                    userinput = key
                    
                    video = input("Masukkan path video: ")
                    count=frame_extraction(video)
                    data = input("Enter data to be encoded : ")
                    
                    print(type(data))
                    n_fr = num_of_frames(data)
                    data_list = split_string(data,n_fr)
                    print(n_fr)
                    encode_text("temp_folder/0.png", str(n_fr))
                    category="11"
                    encode_text("temp_folder/1.png", category)
                    for i in range(n_fr):
                        encode_text("temp_folder/"+str(i+2)+".png", data_list[i])
                    call(["ffmpeg", "-i", "temp_folder/%d.png" , "-vcodec", "png", "tmp/video.avi", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
                    call(["ffmpeg", "-i", "-framerate 15" "tmp/video.avi", "-i", "tmp/audio.mp3", "-codec", "copy", "res/video.avi", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
                    print("\nEncoding....")
                    
                elif (userinput == 2):
                    pass
            elif (userinput == 2):
                a = input("1. Pixel-pixel Sekuensial \n 2. Pixel-pixel acak \n Your input is: ")
                userinput = int(a)
                if (userinput == 1):
                    """
                    key = input("Masukkan kunci: ")
                    userinput = key
                    pix_fr = randomized_pixels_frames(prod_seed(key))
                    print(pix_fr)
                    for el in pix_fr:
                        encode_text("temp_folder/"+str(el)+".png")
                    
                    print("\nEncoding....")
                    #encode_text()
                    """
                    key = input("Masukkan kunci: ")
                    userinput = key
                    #pix_fr = randomized_pixels_frames(prod_seed(key))
                    #print(pix_fr)
                    video = input("Masukkan path video: ")
                    count=frame_extraction(video)
                    data = input("Enter data to be encoded : ")
                    #msg_len = message_length(data)
                    n_fr = num_of_frames(data)
                    data_list = split_string(data,n_fr)
                    pix_fr = randomized_pixels_frames(prod_seed(key), count, n_fr)
                    print(n_fr)
                    print(pix_fr)
                    encode_text("temp_folder/0.png", str(n_fr))
                    category="21"
                    encode_text("temp_folder/1.png", category)
                    for i in range(n_fr):
                        encode_text("temp_folder/"+str(pix_fr[i])+".png", data_list[i])
                    call(["ffmpeg", "-i", "temp_folder/%d.png" , "-vcodec", "png", "-r", "15", "tmp/video.avi", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
                    call(["ffmpeg", "-i", "tmp/video.avi", "-i", "tmp/audio.mp3", "-codec", "copy", "res/video.avi", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
                    print("\nEncoding....")
                    #encode_text()
                elif (userinput == 2):
                    pass
        elif (userinput == 2):
            a = input("1. Frame sekuensial \n 2. Frame acak \n Your input is: ")
            userinput = int(a)
            if (userinput == 1):
                a = input("1. Pixel-pixel Sekuensial \n 2. Pixel-pixel acak \n Your input is: ")
                userinput = int(a)
                if (userinput == 1):
                    key = input("Masukkan kunci: ")
                    userinput = key
                    #pix_fr = randomized_pixels_frames(prod_seed(key))
                    #print(pix_fr)
                    video = input("Masukkan path video: ")
                    count=frame_extraction(video)
                    data = input("Enter data to be encoded : ")
                    data_enc = encryptTextExtendedVigenere(data, key)
                    #msg_len = message_length(data)
                    n_fr = num_of_frames(data)
                    data_list = split_string(data_enc,n_fr)
                    print(n_fr)
                    encode_text("temp_folder/0.png", str(n_fr))
                    category="11"
                    encode_text("temp_folder/1.png", category)
                    for i in range(n_fr):
                        encode_text("temp_folder/"+str(i+2)+".png", data_list[i])
                    call(["ffmpeg", "-i", "temp_folder/%d.png" , "-vcodec", "png", "tmp/video.avi", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
                    call(["ffmpeg", "-i", "-framerate 15" "tmp/video.avi", "-i", "tmp/audio.mp3", "-codec", "copy", "res/video.avi", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
                    print("Proses selesai")
                    #encode_text()
                elif (userinput == 2):
                    pass
            elif (userinput == 2):
                pass
          
    elif (userinput == 2):
        key = input("Masukkan kunci: ")
        video = input("Masukkan path video: ")
        count=frame_extraction(video)
        #print(count)
        DIR="temp_folder"
        count = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])-1
        #count=10000
        n_fr = int(decode_text("temp_folder/0.png"))
        category = decode_text("temp_folder/1.png")
        print(category)
        #data_list = split_string(data,n_fr)
        #pix_fr = randomized_pixels_frames(prod_seed(key), count, n_fr)
        #print(n_fr)
        #print(pix_fr)
        if (category=="11"):
            for i in range(n_fr):
                print(decode_text("temp_folder/"+str(i+2)+".png"), end="")
            print("\nDecoding....")
            #print("Decoded message is " + decode_text())
        elif (category=="21"):
            #data_list = split_string(data,n_fr)
            pix_fr = randomized_pixels_frames(prod_seed(key), count, n_fr)
            print(n_fr)
            print(pix_fr)
            for i in range(n_fr):
                print(decode_text("temp_folder/"+str(pix_fr[i])+".png"), end="")
            print("Proses selesai")
            #print("Decoded message is " + decode_text())
    else: 
        raise Exception("Enter correct input") 
          
Steganography() #encode image


# In[112]:


vidcap = cv2.VideoCapture("res/video.avi")
fps = vidcap.get(cv2.CAP_PROP_FPS)
print("fps: ", end="")
print(fps)


# In[100]:


count = frame_extraction("res/video.avi")


# In[58]:


stri = "akan"
print(type(stri))


# In[ ]:




