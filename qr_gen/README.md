### 📄 `qr_generator/README.md`

```markdown
# QR Code Generator 📱

A simple utility to generate QR codes from any string, URL or text.

## ✨ Features

- Generate QR code from text
- Save to PNG file
- Optional: display inline in Jupyter/Colab
- Modular function for reuse

## 🚀 Usage

### 1. Python Script

```python
from qr_generator import generate_qr

generate_qr(
    data="https://github.com/your_username",
    filename="my_qr.png",
    show=True,
    save=True
)
