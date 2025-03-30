from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.image import Image as KivyImage
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
import requests

BACKEND_URL = "http://127.0.0.1:5000"

class DecryptScreen(Screen):
    selected_file = StringProperty("No image selected")
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

    def decrypt_message(self):
        if not self.selected_file or self.selected_file == "No image selected":
            print("Please select an image first.")
            return

        key = self.ids.key_input.text
        if not key:
            print("Please enter a decryption key.")
            return

        files = {'image': open(self.selected_file, 'rb')}
        data = {'key': key, 'reuse_key': self.reuse_key}
        response = requests.post(f"{BACKEND_URL}/decrypt", files=files, data=data)

        if response.status_code == 200:
            response_data = response.json()
            self.ids.decrypted_message.text = f"Decrypted: {response_data.get('message', 'N/A')}"
            print("Decryption successful!")
        else:
            print("Decryption failed:", response.json())

    def show_full_image(self, path):
        if not path:
            return
        image = KivyImage(source=path, allow_stretch=True)
        layout = BoxLayout()
        layout.add_widget(image)
        popup = Popup(title="Full Image Preview", content=layout,
                      size_hint=(0.9, 0.9), auto_dismiss=True)
        popup.open()
