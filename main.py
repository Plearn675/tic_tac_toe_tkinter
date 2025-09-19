import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageFont

class TicTacToeGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe Game")
        self.geometry("620x620")
        self.resizable(width=False, height=False)

        # --- UI   -----
        tk.Label(self, text="Watermark Text:").pack(pady=(12,0))
        self.watermark_text = tk.StringVar(value="© Your Name")
        tk.Entry(self, textvariable=self.watermark_text, width=34).pack(pady=(0, 10))

        tk.Button(self, text="Upload Image").pack(pady=6)
        self.preview_btn = tk.Button(self, text="Show Preview", width=22, state="disabled")
        self.preview_btn.pack(pady=6)
        self.save_btn = tk.Button(self, text="Save Image", state="disabled")
        self.save_btn.pack(pady=6)

        tk.Label(self, text="Tip: After uploading, preview opens in a new window.").pack(pady=(6, 0))



if __name__ == "__main__":
    app = TicTacToeGame()
    app.mainloop()
