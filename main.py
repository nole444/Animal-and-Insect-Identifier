import tkinter as tk
from controller import Controller

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Animal/Insect Identifier App")
    root.geometry("700x600")  # Set a normal window size
    app = Controller(root)
    root.mainloop()
