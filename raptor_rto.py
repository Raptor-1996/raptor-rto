import tkinter as tk
from tkinter import ttk
import threading
import keyboard
import easyocr
import numpy as np
from PIL import ImageGrab, ImageTk, Image
from googletrans import Translator
import sys
import os

# ========== تنظیمات اولیه ==========
reader = easyocr.Reader(['ru', 'en'], gpu=False)
translator = Translator()

# ========== پنجره شناور Raptor ==========
root = tk.Tk()
root.title("Raptor RTO (Wild Land) - Raptor")
root.attributes('-topmost', True)
root.attributes('-alpha', 0.85)
root.overrideredirect(True)
root.configure(bg='black')
root.iconbitmap('assets/icon.ico')

BG_COLOR = "#0a0a0a"
TEXT_COLOR_RU = "#ffcc00"
TEXT_COLOR_EN = "#00ffcc"
FONT_RU = ("Consolas", 11, "bold")
FONT_EN = ("Segoe UI", 10)

frame = tk.Frame(root, bg=BG_COLOR, bd=0)
frame.pack(padx=10, pady=8)

# هدر با دکمه بستن
header_frame = tk.Frame(frame, bg=BG_COLOR)
header_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0,5))

label_title = tk.Label(header_frame, text="🐺 RAPTOR RTO", fg="#ff4444", bg=BG_COLOR, 
                       font=("Arial", 8, "bold"))
label_title.pack(side="left")

# دکمه بستن
def close_app():
    root.destroy()
    os._exit(0)

close_btn = tk.Label(header_frame, text=" ✖ ", fg="#ff6666", bg=BG_COLOR, 
                     font=("Arial", 9, "bold"), cursor="hand2")
close_btn.pack(side="right")
close_btn.bind("<Button-1>", lambda e: close_app())

label_ru = tk.Label(frame, text="", fg=TEXT_COLOR_RU, bg=BG_COLOR, font=FONT_RU, 
                    wraplength=380, justify="left")
label_ru.grid(row=1, column=0, sticky="w", pady=2)

label_en = tk.Label(frame, text="", fg=TEXT_COLOR_EN, bg=BG_COLOR, font=FONT_EN, 
                    wraplength=380, justify="left")
label_en.grid(row=2, column=0, sticky="w", pady=2)

status_label = tk.Label(frame, text="🟢 Ready | Ctrl+Shift+L", fg="#888888", bg=BG_COLOR,
                        font=("Segoe UI", 7))
status_label.grid(row=3, column=0, sticky="w", pady=(5,0))

def start_move(event):
    root.x = event.x
    root.y = event.y

def on_move(event):
    deltax = event.x - root.x
    deltay = event.y - root.y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry(f"+{x}+{y}")

frame.bind("<Button-1>", start_move)
frame.bind("<B1-Motion>", on_move)
label_title.bind("<Button-1>", start_move)
label_title.bind("<B1-Motion>", on_move)

def capture_and_translate():
    status_label.config(text="🟡 Capturing screen...", fg="#ffaa00")
    root.update()
    
    screenshot = ImageGrab.grab(all_screens=True)
    img_np = np.array(screenshot)
    
    status_label.config(text="🔍 OCR reading Russian...", fg="#ffaa00")
    root.update()
    
    results = reader.readtext(img_np, paragraph=False)
    
    russian_texts = []
    for (bbox, text, confidence) in results:
        if any('\u0400' <= ch <= '\u04FF' for ch in text) and confidence > 0.4:
            russian_texts.append(text)
    
    if not russian_texts:
        label_ru.config(text="❌ No Russian text detected")
        label_en.config(text="Try adjusting camera angle")
        status_label.config(text="🔴 No text | Ready", fg="#888888")
        return
    
    full_ru = " ".join(russian_texts)
    highlighted_ru = f"🇷🇺 {full_ru}"
    label_ru.config(text=highlighted_ru)
    
    status_label.config(text="🌍 Translating to English...", fg="#ffaa00")
    root.update()
    
    try:
        translation = translator.translate(full_ru, src='ru', dest='en')
        translated_en = f"🇬🇧 {translation.text}"
        label_en.config(text=translated_en)
        status_label.config(text="✅ Ready | Ctrl+Shift+L", fg="#00ff88")
    except Exception as e:
        label_en.config(text=f"Translation error: {str(e)[:50]}")
        status_label.config(text="⚠️ API Error", fg="#ff4444")
    
    root.after(5000, lambda: root.geometry(""))

def on_hotkey():
    threading.Thread(target=capture_and_translate, daemon=True).start()

keyboard.add_hotkey('ctrl+shift+l', on_hotkey)

root.geometry("420x140")
root.mainloop()