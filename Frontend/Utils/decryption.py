import cv2

def decrypt_image(image_path, key):
    """Extracts the hidden message from an encrypted image."""
    img = cv2.imread(image_path)
    if img is None:
        return "Invalid image"

    rows, cols, _ = img.shape
    decoded_message = []

    for row in range(rows):
        for col in range(cols):
            char_value = img[row, col, 0]  #Read from blue channel
            if char_value == 0:
                break
            decoded_message.append(chr(char_value))

    return ''.join(decoded_message)
