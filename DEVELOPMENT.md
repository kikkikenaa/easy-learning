# 👨‍💻 Developer Guide

This guide explains the **code structure** and how to modify or contribute to the project.

---

## 📂 Project Structure

easy_learning2/ │── main/ │ │── main.py # Core script to classify topics & trigger animations │ │── topic_classifier.py # Classifies topics into Biology, Physics, or General │ │── generate_biology_animation.py # Manim animations for Biology topics │ │── generate_physics_animation.py # Manim animations for Physics topics │ │── generate_animation.py # Default text-based animations │ │── generate_audio.py # Converts study notes to speech │ │── combine_video_audio.py # Merges animations with TTS audio │── pages/ │ │── 1_Upload_Files.py # Upload page in Streamlit │ │── 2_Analyze_Files.py # Analysis page in Streamlit │── assets/ # Contains SVGs for animations │── requirements.txt # Dependencies

---

## 📝 Code Overview

### 1️⃣ **Topic Classification (`topic_classifier.py`)**

- Checks study material for keywords like `"heart"`, `"voltage"`, etc.
- Categorizes the content as **Biology, Physics, or General**.

### 2️⃣ **Generating Animations**

- **Biology topics** → `generate_biology_animation.py`
- **Physics topics** → `generate_physics_animation.py`
- **General text-based animations** → `generate_animation.py`

### 3️⃣ **Text-to-Speech & Video Processing**

- **TTS Audio** → `generate_audio.py`
- **Merge video & audio** → `combine_video_audio.py`

---

## 🛠 How to Add a New Animation

1. Create a new **Manim animation class** inside `generate_biology_animation.py` or `generate_physics_animation.py`.
2. Update `topic_classifier.py` to recognize new keywords.
3. Test the new animation using:
   ```sh
   manim -pql main/generate_biology_animation.py NewAnimationClass
   ```

---

## **5️⃣ `API_REFERENCE.md` (Only if needed)**

If you decide to add an API in the future, this document will describe the API endpoints.

Example:

````md
# 📡 API Reference

## 🔹 1. Upload Files

**Endpoint:** `POST /upload`  
Uploads a study material file.

**Request:**

```json
{
  "file": "study_notes.pdf"
}
```
````

response:
{
"message": "File uploaded successfully",
"file_id": "123abc"
}

---

## **Next Steps**

Now that you have a well-structured documentation plan, you can:

- **Create these files** in your project folder.
- **Fill in missing details** (like author name, repo link, etc.).
- **Push everything to GitHub** so that others can read the docs easily.

Would you like help in writing GitHub **badges** (e.g., version, Python version, license) or setting up a **wiki**? 🚀
