# 🛠 Installation Guide

Follow these steps to set up Easy Learning on your local machine.

## 🔹 1. Clone the Repository

```sh
git clone https://github.com/yourusername/easy-learning.git
cd easy-learning
```

## 🔹 2.Install Dependencies

pip install -r requirements.txt

## 🔹 3. Run the application

streamlit run main/main.py

## 🔹4.(Optional) Run an Animation Manually

manim -pql main/generate_biology_animation.py DigestiveSystemAnimation
manim -pql main/generate_physics_animation.py ElectricityAnimation

## 🔹trouble shooting

if manim is not found
pip install manim
if streamlit does not start check python environment is active

---

## **3️⃣ `USAGE.md` - How to Use**

```md
# 📖 User Guide - Easy Learning

This guide explains how to use the Easy Learning web app.

---

## 📂 1. Upload Study Materials

1️⃣ Click on the **Upload Files** tab.  
2️⃣ Upload your **text files or PDFs** containing notes or exam materials.  
3️⃣ Click **Analyze** to extract key topics.

---

## 🎥 2. Animated Summaries

- If your notes contain Biology topics (e.g., "Digestive System"), a **human body animation** will be generated.
- If the notes contain Physics topics (e.g., "Electric Current"), a **physics animation** will be generated.
- If no specific subject is found, a **text-based animation** is created.

---

## 🔊 3. Listen to Audio Summaries

- The app will generate **spoken explanations** using text-to-speech (TTS).
- You can **download the audio** or **watch the combined video summary**.

---

## 🎬 4. Watch the Final Video

- The system **combines animations and audio** into a single **study video**.
- Click **Download Video** to save it for offline study.
```
