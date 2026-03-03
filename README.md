# ASCII GIF Converter

A desktop application that converts animated GIFs into animated ASCII art GIFs.

Built with **PySide6** for the GUI and **Pillow** for image processing.

---

## ✨ Features

* Convert animated GIFs to ASCII-art animated GIFs
* Adjustable scale percentage
* Adjustable font size
* Real-time progress bar
* Responsive UI (conversion runs in a background thread)
* Custom monospace font rendering (Ubuntu Mono)

---

## 🖥️ Built With

* Python 3
* PySide6 (Qt for Python)
* Pillow (PIL)
* PyInstaller (for building executables)

---

## 📂 Project Structure

```
ASCII-GIF-Converter/
│
├── main.py
├── converter.py
├── fonts/
│   └── UbuntuMono-R.ttf
├── requirements.txt
└── README.md
```

---

## 🚀 Installation (Development)

### 1. Clone the repository

```bash
git clone https://github.com/naseidl22/ASCII-Gif.git
cd ascii-gif-converter
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

---

## 📦 Building the Executable (Windows)

This project uses PyInstaller.

### Folder Build (Recommended – Faster Startup)

```bash
pyinstaller --windowed --collect-all PySide6 --add-data "fonts;fonts" main.py
```

### One-File Build (Single EXE)

```bash
pyinstaller --onefile --windowed --collect-all PySide6 --add-data "fonts;fonts" main.py
```

The executable will be located in:

```
dist/
```

---

## ⚙️ How It Works

1. Each GIF frame is extracted using Pillow.
2. Frames are converted to grayscale.
3. Pixel brightness is mapped to ASCII characters.
4. ASCII strings are rendered to images using a monospace font.
5. Frames are reassembled into a new animated GIF.

---

## 📄 License

This project is open source. Feel free to use and modify.

---

## 👤 Author

Created by Nicholas Seidl.
