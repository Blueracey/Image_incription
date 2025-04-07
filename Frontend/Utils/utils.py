import cv2
import random

def is_even(value):
    return value % 2 == 0

def to_binary(char):
    return format(ord(char), '08b')

def to_char(bits):
    return chr(int(bits, 2))

def get_message_bits(message):
    split = message.strip().split()
    final_bits = []

    for word in split:
        for char in word:
            for bit in to_binary(char):
                final_bits.append(int(bit))
        final_bits.extend([0, 0, 1, 0, 0, 0, 0, 0])  # space delimiter

    return final_bits

def get_image(image_path):
    img = cv2.imread(image_path,cv2.IMREAD_UNCHANGED)
    assert img is not None, f"Image file '{image_path}' not found or unreadable."
    return img

def get_message_length(img):
    hidden_pixel = img[0][0]
    red_digit = str(hidden_pixel[0])[-1]
    green_digit = str(hidden_pixel[1])[-1]
    blue_digit = str(hidden_pixel[2])[-1]

    total = int(red_digit + green_digit + blue_digit)
    return total * 8

def generate_random_pattern():
    return {
        "red": random.randint(3, 40),
        "green": random.randint(3, 40),
        "blue": random.randint(3, 40),
    }
