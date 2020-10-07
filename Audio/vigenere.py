def Encrypt(input, key):
    output = ''
    for i in range (len(input)):
        c = ord(input[i])
        k = ord(key[mod(i,len(key))])
        output += chr(mod(c + k, 256))
    return output


def Decrypt(input, key):
    output = ''
    for i in range (len(input)):
        c = ord(input[i])
        k = ord(key[mod(i,len(key))])
        output += chr(mod(c - k, 256))
    return output

def mod(n, m):
    return (((n % m) + m) % m)