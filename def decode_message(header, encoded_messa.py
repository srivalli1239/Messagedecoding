def decode_message(header, encoded_message):
    key_to_char = {}
    keys = generate_keys()
    for i in range(len(header)):
        key_to_char[keys[i]] = header[i]
    decoded_message = ""
    key_length = int(encoded_message[:3], 2)
    i = 3
    while key_length != 0:
        while encoded_message[i:i+key_length] != "1"*key_length:
            key=encoded_message[i:i+key_length]
            decoded_message += key_to_char[key]
            i += key_length
        i += key_length
        key_length = int(encoded_message[i:i+3], 2)
        i+=3
    return decoded_message
def generate_keys():
    keys = [ ]
    for i in range(1,8):
        for j in range(2**i-1):
            if bin(j)[2:] != '1' * i :
                keys.append(bin(j)[2:].zfill(i))
    return keys
header="tnm aeiou"
enc = "0010101100011101000100111011001111000"
print(decode_message(header,enc))
header = "$#**/"
enc  = "0100000101101100011100101000"
print(decode_message(header,enc))
