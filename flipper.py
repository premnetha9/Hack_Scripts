import socket, os
import re
from binascii import unhexlify

def send_request(socket, data):
    print(f'...sending {data}...')
    if data is not None:
        socket.sendall(data)
    data = socket.recv(8092).decode().strip()
    return data


def extract_cipher(data):
    match = re.search(r'Leaked ciphertext:\s(.*)', data)
    return unhexlify(match[1])

def flip_bit(data, i):
    return (i).to_bytes(1, byteorder="big") + data[1:48]

if __name__ == "__main__":
    HOST = '161.35.174.55'
    PORT =  30493
    # HOST = '127.0.0.1'
    # PORT = 1337

    for i in range(0, 255):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            data = None
            # initial request
            data = send_request(s, None)
            #print(data)
            # submit username
            data = send_request(s, b'bdmin')
            # print(data)
            # submit password
            data = send_request(s, b'g0ld3n_b0y') # e must be replaced with 3 through bit flipping
            # print(data)
            data = send_request(s, None)
            # print(data)
            # extract cipher
            cipher = extract_cipher(data)
            # flip a bit
            flipped_cipher = flip_bit(cipher, i)
            data = send_request(s, flipped_cipher.hex().encode())
            print(data)
            if re.search(r'successfully', data):
                quit()
            # final request
            data = send_request(s, None)
            print(data) 