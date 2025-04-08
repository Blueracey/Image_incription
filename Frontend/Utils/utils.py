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



def generate_code():
    red = random.randint(4, 99)
    green = random.randint(4, 99)
    blue = random.randint(4, 99)
    code = {
        "red": hex(red * 12345600),
        "green": hex(green * 12345600),
        "blue": hex(blue * 12345600),
    }
    return code

def connver_to_key_string(code):
    return f'{code["red"]}|{code["green"]}|{code["blue"]}'

def convert_key_string_to_dict(key):
    split = key.split("|")
    return {
        "red": split[0],
        "green": split[1],
        "blue": split[2],
    }

def translate_code(key):
    code = convert_key_string_to_dict(key)
    pattern = {
        "red": int(int(code["red"], 16) / 12345600),
        "green": int(int(code["green"], 16) / 12345600),
        "blue": int(int(code["blue"], 16) / 12345600),
    }
    return pattern
