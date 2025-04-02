from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.image import Image as KivyImage
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from Utils.file_chooser import FileChooserPopup
from Utils.utils import get_image
from Utils.decryption import decript, remakemessage
import ast

class DecryptScreen(Screen):
    selected_file = StringProperty("No image selected")
    reuse_key = BooleanProperty(False)

    def open_file_chooser(self):
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

        key_str = self.ids.key_input.text.strip()
        if not key_str:
            print("Please enter a decryption key.")
            return

        try:
            # Safely parse string to dictionary
            pattern = ast.literal_eval(key_str)
            img = get_image(self.selected_file)

            # Run decryption using local logic
            bits = decript(img, pattern)
            message = remakemessage(bits)

            self.ids.decrypted_message.text = f"Decrypted: {message}"
            print("Decryption successful!")
        except Exception as e:
            print(f"Decryption failed: {e}")
            self.ids.decrypted_message.text = "Decryption failed. Check key and image."

    def show_full_image(self, path):
        if not path:
            return
        image = KivyImage(source=path, allow_stretch=True)
        layout = BoxLayout()
        layout.add_widget(image)
        popup = Popup(title="Full Image Preview", content=layout,
                      size_hint=(0.9, 0.9), auto_dismiss=True)
        popup.open()
