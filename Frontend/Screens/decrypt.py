from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, BooleanProperty
import requests

BACKEND_URL = "http://127.0.0.1:5000"  #Flask Backend URL

class DecryptScreen(Screen):
    selected_file = StringProperty("No image selected")
    reuse_key = BooleanProperty(False)

    def open_file_chooser(self):
        """Opens a file chooser popup."""
        from Utils.file_chooser import FileChooserPopup
        popup = FileChooserPopup(self.set_selected_file)
        popup.open()

    def set_selected_file(self, file_path):
        """Sets the selected file from the popup."""
        self.selected_file = file_path

    def toggle_reuse_key(self):
        """Toggles the reuse key option and updates button text."""
        self.reuse_key = not self.reuse_key
        if "reuse_key_button" in self.ids:
            self.ids.reuse_key_button.text = "Do Not Reuse Key" if self.reuse_key else "Reuse Last Key"

    def decrypt_message(self):
        """Handles decryption by sending the image and key to backend."""
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
