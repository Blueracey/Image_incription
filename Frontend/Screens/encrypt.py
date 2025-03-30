from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.uix.image import Image as KivyImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
import requests

BACKEND_URL = "http://127.0.0.1:5000"  # Flask Backend URL

class EncryptScreen(Screen):
    selected_file = StringProperty("No image selected")
    encrypted_file = StringProperty("")
    reuse_key = BooleanProperty(False)

    def open_file_chooser(self):
        from Utils.file_chooser import FileChooserPopup
        popup = FileChooserPopup(self.set_selected_file)
        popup.open()

    def set_selected_file(self, file_path):
        self.selected_file = file_path
        self.ids.selected_image.source = file_path

    def toggle_reuse_key(self):
        self.reuse_key = not self.reuse_key
        self.ids.reuse_key_button.text = "Reusing Key" if self.reuse_key else "Not Reusing Key"

    def encrypt_message(self):
        if not self.selected_file or self.selected_file == "No image selected":
            print("Please select an image first.")
            return

        message = self.ids.message_input.text
        if not message:
            print("Please enter a message to encrypt.")
            return

        files = {'image': open(self.selected_file, 'rb')}
        data = {'message': message, 'reuse_key': self.reuse_key}
        response = requests.post(f"{BACKEND_URL}/encrypt", files=files, data=data)

        if response.status_code == 200:
            response_data = response.json()
            self.ids.key_output.text = f"Generated Key: {response_data.get('key', 'N/A')}"
            encrypted_path = response_data.get("encrypted_image_path", "")
            self.encrypted_file = encrypted_path
            self.ids.encrypted_image.source = encrypted_path
            print("Encryption successful!")
        else:
            print("Encryption failed:", response.json())

    def show_full_image(self, path):
        if not path:
            return
        image = KivyImage(source=path, allow_stretch=True)
        layout = BoxLayout()
        layout.add_widget(image)
        popup = Popup(title="Full Image Preview", content=layout,
                      size_hint=(0.9, 0.9), auto_dismiss=True)
        popup.open()
