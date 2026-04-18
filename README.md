# Ascii_art
# 🎥 ASCII Webcam Renderer (Skull Style)

Convert your webcam feed into **clean, high-contrast ASCII art** in real-time — inspired by the classic black-and-white “skull-style” ASCII visuals.

---

## ✨ Features

* 🧠 Real-time webcam to ASCII conversion
* ⚫ Black background with white/gray character shading
* 🎯 High contrast for sharp visual structure
* ⚡ Smooth rendering using OpenCV
* 🖥️ Single output window (no raw camera feed)

---

## 🖼️ Output Preview

*Add your screenshots here 👇*

![Output 1]<img width="1002" height="654" alt="Screenshot 2026-04-19 034201" src="https://github.com/user-attachments/assets/9e2a92bf-352e-4623-8eff-e84e191b3946" />

---

## ⚙️ How It Works

1. Capture webcam frames using OpenCV
2. Convert frames to grayscale
3. Resize image to match ASCII proportions
4. Map pixel intensity → ASCII characters
5. Render ASCII characters back into an image
6. Display output in real-time

---

## 🧪 Tech Stack

* Python
* OpenCV
* NumPy

---

## 📦 Installation

```bash
git clone https://github.com/your-username/ascii-webcam.git
cd ascii-webcam
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python ascii_camera.py
```

Press **`q`** to exit.

---

## 🔧 Customization

### Change ASCII Density

```python
ASCII_CHARS = " .:-=+*#%@"
```

### Increase Detail

```python
new_width = 140
```

### Improve Contrast

Add:

```python
gray = cv2.equalizeHist(gray)
```

---

## 🚀 Future Improvements

* Edge-detection based ASCII (sharper output)
* Colored ASCII rendering
* Face detection + focused ASCII
* Web-based version (JavaScript + Canvas)

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgment

Inspired by classic ASCII art techniques and real-time image processing concepts.
