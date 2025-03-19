from flask import Flask, request, jsonify
import cv2
import numpy as np
import os
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "Flask Backend for Image Encryption"

#Encrypt Route
@app.route("/encrypt", methods=["POST"])
def encrypt():
    print("Incoming Request to /encrypt")

    #Debug Print the request content
    print(f"Request files: {request.files}")
    print(f"Request form: {request.form}")

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    if "message" not in request.form:
        return jsonify({"error": "No message provided"}), 400

    image_file = request.files["image"]
    message = request.form["message"]

    #Debug
    print(f"Received file: {image_file.filename}")
    print(f"Received message: {message}")

    #Check if the file has actual name
    if image_file.filename == "":
        return jsonify({"error": "Empty file received"}), 400

    image_path = os.path.join(UPLOAD_FOLDER, "input.png")
    image_file.save(image_path)

    if not os.path.exists(image_path):
        return jsonify({"error": "Failed to save image"}), 500

    from PIL import Image
    try:
        img_pil = Image.open(image_path)
        img_pil = img_pil.convert("RGB")  #Convert to RGB in case it's grayscale
        img_pil.save(image_path)
    except Exception as e:
        return jsonify({"error": f"PIL could not open image: {str(e)}"}), 400

    img = cv2.imread(image_path)
    if img is None:
        return jsonify({"error": "OpenCV could not read image"}), 400

    from Editing_test_2 import encript
    encript(img)

    encrypted_path = os.path.join(UPLOAD_FOLDER, "encrypted.png")
    cv2.imwrite(encrypted_path, img)

    return jsonify({"message": "Encryption successful!", "image": encrypted_path})

#Decrypt Route
@app.route("/decrypt", methods=["POST"])
def decrypt():
    if "image" not in request.files:
        return jsonify({"error": "Missing image"}), 400

    image_file = request.files["image"]
    image_path = os.path.join(UPLOAD_FOLDER, "encrypted.png")
    image_file.save(image_path)

    #Opening the image using Pillow
    try:
        img_pil = Image.open(image_path)
        img_pil = img_pil.convert("RGB")  #Convert to RGB
        img_pil.save(image_path)
    except Exception as e:
        return jsonify({"error": f"PIL could not open image: {str(e)}"}), 400

    img = cv2.imread(image_path)
    if img is None:
        return jsonify({"error": "OpenCV could not read image"}), 400

    from output_to_textfile import extract_message  #Import decryption function
    hidden_message = extract_message(img)  #Extract hidden message

    return jsonify({"message": "Decryption successful!", "hidden_message": hidden_message})

if __name__ == "__main__":
    app.run(debug=True)
