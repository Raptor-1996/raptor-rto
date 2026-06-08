import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

class RaptorLauncher:
    def __init__(self):
        self.process = None
        self.root = tk.Tk()
        self.root.title("Raptor RTO Launcher")
        self.root.geometry("400x500")
        self.root.configure(bg="#1a1a1a")
        self.root.resizable(False, False)
        
        # لوگو و عنوان
        title_frame = tk.Frame(self.root, bg="#1a1a1a")
        title_frame.pack(pady=20)
        
        tk.Label(title_frame, text="🐺", font=("Arial", 48), bg="#1a1a1a", fg="#ff4444").pack()
        tk.Label(title_frame, text="RAPTOR RTO", font=("Arial", 24, "bold"), 
                bg="#1a1a1a", fg="#ff4444").pack()
        tk.Label(title_frame, text="Ghost Recon Wildlands Translator", 
                font=("Arial", 10), bg="#1a1a1a", fg="#888888").pack()
        
        # اطلاعات بازی
        info_frame = tk.Frame(self.root, bg="#2a2a2a", relief="ridge", bd=1)
        info_frame.pack(pady=20, padx=20, fill="x")
        
        tk.Label(info_frame, text="🎮 GAME INFO", font=("Arial", 10, "bold"),
                bg="#2a2a2a", fg="#ffcc00").pack(pady=5)
        tk.Label(info_frame, text="Game: Ghost Recon Wildlands", 
                bg="#2a2a2a", fg="#ffffff").pack()
        tk.Label(info_frame, text="Language: Russian → English", 
                bg="#2a2a2a", fg="#ffffff").pack()
        tk.Label(info_frame, text="Hotkey: Ctrl+Shift+L", 
                bg="#2a2a2a", fg="#00ffcc").pack()
        
        # دکمه‌ها
        btn_frame = tk.Frame(self.root, bg="#1a1a1a")
        btn_frame.pack(pady=20)
        
        self.start_btn = tk.Button(btn_frame, text="▶ START RAPTOR", command=self.start_raptor,
                                   bg="#00aa44", fg="white", font=("Arial", 12, "bold"),
                                   width=20, height=2, cursor="hand2")
        self.start_btn.pack(pady=5)
        
        self.stop_btn = tk.Button(btn_frame, text="⏹ STOP RAPTOR", command=self.stop_raptor,
                                  bg="#aa4444", fg="white", font=("Arial", 12, "bold"),
                                  width=20, height=2, cursor="hand2", state="disabled")
        self.stop_btn.pack(pady=5)
        
        # وضعیت
        self.status_label = tk.Label(self.root, text="⚫ Status: Stopped", 
                                     font=("Arial", 10), bg="#1a1a1a", fg="#888888")
        self.status_label.pack(pady=10)
        
        # راهنما
        help_frame = tk.Frame(self.root, bg="#2a2a2a", relief="ridge", bd=1)
        help_frame.pack(pady=20, padx=20, fill="x")
        
        tk.Label(help_frame, text="📖 HOW TO USE", font=("Arial", 10, "bold"),
                bg="#2a2a2a", fg="#ffcc00").pack(pady=5)
        tk.Label(help_frame, text="1. Click 'START RAPTOR'", 
                bg="#2a2a2a", fg="#cccccc", anchor="w").pack(fill="x", padx=10)
        tk.Label(help_frame, text="2. Launch Ghost Recon Wildlands", 
                bg="#2a2a2a", fg="#cccccc", anchor="w").pack(fill="x", padx=10)
        tk.Label(help_frame, text="3. Press Ctrl+Shift+L for translation", 
                bg="#2a2a2a", fg="#00ffcc", anchor="w").pack(fill="x", padx=10)
        tk.Label(help_frame, text="4. Click 'X' on translator window to close", 
                bg="#2a2a2a", fg="#cccccc", anchor="w").pack(fill="x", padx=10)
        
        # کپی رایت
        tk.Label(self.root, text="© Raptor | Wild Land Edition", 
                font=("Arial", 8), bg="#1a1a1a", fg="#555555").pack(side="bottom", pady=10)
        
    def start_raptor(self):
        try:
            os.chdir(r"C:\Users\orion\Documents\000 Development\raptor_rto")
            self.process = subprocess.Popen([sys.executable, "raptor_rto.py"])
            self.status_label.config(text="🟢 Status: Running - Ready for game", fg="#00ff00")
            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")
            messagebox.showinfo("Success", "Raptor is running!\n\nPress Ctrl+Shift+L in game for translation.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start: {str(e)}")
    
    def stop_raptor(self):
        if self.process:
            self.process.terminate()
            self.process = None
        self.status_label.config(text="⚫ Status: Stopped", fg="#888888")
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = RaptorLauncher()
    app.run()