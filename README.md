<div align="center">
  
  <img src="assets/logo.png" alt="Raptor RTO Logo" width="200">
  
  # 🐺 Raptor RTO (CIS Helper)
  
  **Real-time Russian to English translator overlay for Ghost Recon Wildlands**
  
  [![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
  [![Python](https://img.shields.io/badge/Python-3.12+-green.svg)](https://python.org)
  [![Platform](https://img.shields.io/badge/Platform-Windows-blue.svg)](https://microsoft.com/windows)
  [![GitHub release](https://img.shields.io/badge/release-v1.0-orange.svg)](https://github.com/yourusername/raptor-rto/releases)
  
</div>

---

## 📖 About

**Raptor RTO** is a lightweight, non-lagging overlay tool that helps you play **Ghost Recon Wildlands** or **WatchDogs** or Any other CIS Games in Russian language by providing real-time English translations.

No more guessing mission objectives or dialogue meanings! Just press `Ctrl+Shift+L` and the translation appears instantly.

### ✨ Features

- 🎯 **Real-time OCR** - Reads Russian text directly from your screen
- 🌍 **Instant Translation** - Uses Google Translate API
- 🪟 **Floating Overlay** - Transparent, always-on-top window that doesn't cause lag
- ⌨️ **Hotkey Support** - `Ctrl+Shift+L` to translate
- 🎮 **Single Player Focused** - No ban risk (offline only)
- ✖️ **Easy Close** - Click the X button to exit


## 🚀 Installation

### Prerequisites
- Windows 10/11
- Python 3.12 or higher
- Ghost Recon Wildlands (Russian version) or Any Other CIS Games
- Single Player Use >>> If You got banned in MP it's on your own :)

### Step-by-Step Guide

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/raptor-rto.git
   cd raptor-rto
Install dependencies
```

```bash
pip install -r requirements.txt
```

### ⚠️ First time only: EasyOCR will download ~500MB of language models. This takes 5-10 minutes.

Run the launcher

```bash
python raptor_launcher.py
```
Or double-click run_launcher.bat

##🎮 How to Use
Launch Ghost Recon Wildlands

Start Raptor RTO (the overlay window appears)
```
Press Ctrl+Shift+L whenever you see Russian text
```

The English translation will appear in the overlay

## 🎮 Hotkeys

| Key | Action |
|-----|--------|
| `Ctrl+Shift+L` | Translate current screen |
| Click + Drag | Move overlay window |
| ✖ (red X) | Close application |


##📁 Project Structure
text
raptor-rto/
├── raptor_rto.py          # Main translator engine
├── raptor_launcher.py     # GUI launcher
├── run_launcher.bat       # Batch launcher
├── requirements.txt       # Dependencies
├── assets/               # Icons and screenshots
└── docs/                 # Documentation


##🤝 Contributing
Contributions are welcome! Please read CONTRIBUTING.md first.

Fork the repository

Create your feature branch (git checkout -b feature/amazing)

Commit your changes (git commit -m 'feat: add amazing feature')

Push to the branch (git push origin feature/amazing)

Open a Pull Request


## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| `pip not recognized` | Reinstall Python with "Add to PATH" option |
| EasyOCR download slow | Check internet connection, first time is ~500MB |
| No text detected | Make sure Russian text is clear and readable |
| Translation not showing | Check if overlay window is on top of game |


## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.


## ⚠️ Disclaimer
This tool is intended for single-player use only The developer is not responsible for any issues arising from multiplayer use Use at your own risk

### 🙏 Acknowledgments
EasyOCR for text detection
Google Translate API


<div align="center"> Made with 🐺 by **Raptor** </div> ```