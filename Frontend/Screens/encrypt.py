from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, BooleanProperty
import requests
import os
import shutil
from tkinter import Tk, filedialog

BACKEND_URL = "http://127.0.0.1:5000"  # Flask Backend URL

class EncryptScreen(Screen):
    selected_file = StringProperty("No image selected")
    reuse_key = BooleanProperty(False)
    encrypted_image_path = StringProperty("")  # Stores path of encrypted image

    def open_file_chooser(self):
        """Opens native Windows file chooser (restricted to images)."""
        from Utils.file_chooser import FileChooserPopup
        popup = FileChooserPopup(self.set_selected_file)
        popup.open()

    def set_selected_file(self, file_path):
        """Sets the selected file from the native file dialog."""
        self.selected_file = file_path

    def toggle_reuse_key(self, state):
        self.reuse_key = True if state == "down" else False

    def encrypt_message(self):
        """Handles encryption by sending the image and message to backend."""
        if not self.selected_file or self.selected_file == "No image selected":
            print("Please select an image first.")
            return

        message = self.ids.message_input.text
        if not message:
            print("Please enter a message to encrypt.")
            return

        files = {'image': open(self.selected_file, 'rb')}
        data = {'message': message, 'reuse_key': self.reuse_key}
        try:
            response = requests.post(f"{BACKEND_URL}/encrypt", files=files, data=data)
            if response.status_code == 200:
                response_data = response.json()
                self.ids.key_output.text = f"Generated Key: {response_data.get('key', 'N/A')}"
                self.encrypted_image_path = response_data.get("encrypted_image_path", "")
                print("Encryption successful!")
            else:
                print("Encryption failed:", response.text)
        except Exception as e:
            print("Error contacting backend:", e)

    def download_encrypted_image(self):
        """Opens a 'Save As' dialog to let the user download the encrypted image."""
        if not self.encrypted_image_path or not os.path.exists(self.encrypted_image_path):
            print("No encrypted image to download.")
            return

        try:
            root = Tk()
            root.withdraw()
            root.wm_attributes('-topmost', 1)
            save_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg;*.jpeg")],
                title="Save Encrypted Image As"
            )
            root.destroy()

            if save_path:
                shutil.copy(self.encrypted_image_path, save_path)
                print(f"Image saved to {save_path}")
        except Exception as e:
            print("Error saving file:", e)
