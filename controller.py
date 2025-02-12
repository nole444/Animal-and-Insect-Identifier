from view import AppView
from model import classify_image, get_details_from_gemini

class Controller:
    def __init__(self, root):
        self.view = AppView(root)
        self.view.set_upload_callback(self.handle_upload)

    def handle_upload(self):
        file_path = self.view.open_file_dialog()
        if file_path:
            self.view.display_image(file_path)
            label = classify_image(file_path)
            if label.startswith("Classification error:"):
                self.view.display_result(label)
                return
            details = get_details_from_gemini(label)
            # Show the label (without extra codes) and the AI details directly.
            result_text = f"Identified: {label}\n\n{details}"
            self.view.display_result(result_text)
