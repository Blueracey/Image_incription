import cv2
import numpy as np
import os
import random
import string

def generate_key(length=16):
    """Generates a random encryption key."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def encrypt_image(image_path, message):
    """Encrypts the given message into an image and returns the encrypted image path and key."""
    img = cv2.imread(image_path)
    if img is None:
        return None, None

    key = generate_key()
    encoded_message = [ord(char) for char in message]  #Convert message to ASCII

    rows, cols, _ = img.shape
    msg_index = 0

    for row in range(rows):
        for col in range(cols):
            if msg_index < len(encoded_message):
                img[row, col, 0] = encoded_message[msg_index]  #Encode in blue channel
                msg_index += 1
            else:
                break
        if msg_index >= len(encoded_message):
            break

    encrypted_path = f"{os.path.splitext(image_path)[0]}_encrypted.png"
    cv2.imwrite(encrypted_path, img)

    return encrypted_path, key
