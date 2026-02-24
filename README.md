# 🎨 MNST Project – Advanced Masked Neural Style Transfer Web App

A modular and extensible **Neural Style Transfer (NST)** web application built using **PyTorch** and **Streamlit**.

This project supports:

- 🎭 Full Image Style Transfer  
- 🧍 Subject-Only Style Transfer  
- 🌄 Background-Only Style Transfer  
- 🎨 Dual Style Transfer  

---

## 🚀 Features

- Modular architecture (clean separation of UI and core logic)
- Optimization-based NST using pretrained CNN
- Subject segmentation support
- Memory monitoring utilities
- Sample images included
- Streamlit interactive UI

---

## 🧠 Models Used

### 1️⃣ VGG19 – Feature Extractor

```python
torchvision.models.vgg19(pretrained=True)
```

**Why VGG19?**

- Pretrained on ImageNet
- Strong hierarchical feature extraction
- Lower layers → textures & edges
- Deeper layers → semantic content
- Standard backbone for NST research

Used only as a **feature extractor**, not for classification.

---

### 2️⃣ Gram Matrix for Style Representation

- Computes feature map correlations
- Captures texture, brush strokes, patterns
- Independent of spatial structure

---

### 3️⃣ Optimization-Based Neural Style Transfer

Instead of training a new network:

```
Total Loss = Content Loss + Style Loss
```

- Direct pixel optimization
- High-quality artistic results
- Adjustable style strength

---

### 4️⃣ Segmentation Model (Subject Mode)

Used for:
- Subject-only stylization
- Background-only stylization
- Dual-style blending

Enables selective artistic transfer.

---

## 🏗️ Project Structure

```
.
├── README.md
├── app
│   ├── streamlit_app.py        # Entry point
│   ├── components              # Reusable UI components
│   │   └── image_selector.py
│   └── views                   # Different NST modes
│       ├── home.py
│       ├── full_style.py
│       ├── subject_style.py
│       ├── background_style.py
│       └── dual_style.py
│
├── images                      # Sample images
│   ├── sampleContent
│   ├── sampleStyle
│   └── samples
│
├── main                        # Core NST logic
│   ├── model_init.py           # VGG initialization
│   ├── nst_model.py            # Core NST loss logic
│   ├── seg_model.py            # Segmentation model
│   ├── stylize.py              # Stylization pipeline
│   ├── memory_utils.py         # RAM monitoring
│   └── utils.py                # Helper functions
│
└── requirements.txt
```

---

## 🛠️ Setup Instructions

### 1️⃣ Create Virtual Environment (Python 3.12)

```bash
python3.12 -m venv venv
```

Activate:

**Mac/Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

---

### 2️⃣ Upgrade Core Packaging Tools

```bash
pip install --upgrade pip setuptools wheel
```

---

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```bash
python -m streamlit run app/streamlit_app.py
```

---

## 💻 Hardware Requirements

### Minimum:
- 8 GB RAM
- CPU support

### Recommended:
- 16 GB RAM
- NVIDIA GPU (CUDA)
- Apple Silicon (M1/M2/M3 with MPS)

> NST is memory-intensive due to VGG feature maps and segmentation masks.

---

## ⚡ Performance Notes

- Large input images significantly increase memory usage.
- Subject/Background modes require additional segmentation processing.
- Image resizing is applied internally for memory safety.

---

## 🔮 Future Improvements

- 🚀 Fast Style Transfer (Feed-forward transformer network)
- ⚡ Mixed precision inference (`float16`)
- 🎛️ Style intensity slider
- 🔄 Before/After comparison view
- 📦 Docker production deployment
- 📊 Real-time GPU/RAM monitoring panel
- 🧠 Model selection (VGG16 / VGG19 / custom encoder)

---

## 🐳 Docker (Optional)

```bash
docker build -t nst-app .
docker run -p 8501:8501 nst-app
```

---

## 📧 Contact

Harshal Khandave  
📩 harshalkhandave19@gmail.com  

---

## ⭐ Why This Project Matters

This project demonstrates:

- Deep understanding of CNN feature extraction
- Gram matrix style encoding
- Loss engineering
- Optimization-based image synthesis
- Clean modular software architecture
- Real-world deployment using Streamlit

If you found this useful, feel free to ⭐ the repository!
