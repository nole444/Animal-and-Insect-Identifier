import tkinter as tk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import tkinter.ttk as ttk  # Use Ttk for modern styling
from PIL import Image, ImageTk

class AppView:
    def __init__(self, master):
        self.master = master
        # Use a modern theme (e.g., 'clam')
        style = ttk.Style()
        style.theme_use("clam")

        # Top frame for welcome message
        self.top_frame = ttk.Frame(master, padding=10)
        self.top_frame.pack(fill=tk.X)
        self.welcome_label = ttk.Label(self.top_frame, text="Hello! Welcome to the Animal/Insect Identifier App!",
                                       font=("Helvetica", 16, "bold"))
        self.welcome_label.pack(pady=10)

        # Main content frame
        self.content_frame = ttk.Frame(master, padding=10)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        # Upload button
        self.upload_button = ttk.Button(self.content_frame, text="Upload Image Here")
        self.upload_button.pack(pady=10)

        # Image display label
        self.image_label = ttk.Label(self.content_frame)
        self.image_label.pack(pady=10)

        # ScrolledText for results (modern styled box)
        self.result_text = ScrolledText(self.content_frame, wrap=tk.WORD, width=60, height=15, font=("Helvetica", 12))
        self.result_text.pack(pady=10, fill=tk.BOTH, expand=True)

    def set_upload_callback(self, callback):
        self.upload_button.config(command=callback)

    def open_file_dialog(self):
        return filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

    def display_image(self, image_path):
        try:
            img = Image.open(image_path)
            img.thumbnail((250, 250))
            self.photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.photo)
            self.image_label.image = self.photo  # keep a reference
        except Exception as e:
            self.display_result(f"Error loading image: {e}")

    def display_result(self, result_text):
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, result_text)
