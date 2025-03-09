import subprocess
import json
import streamlit as st
from topic_classifier import classify_topic

# Get relevant study content from session state
selected_content = st.session_state.get("selected_content", "")
selected_topics = st.session_state.get("selected_topics", [])

if selected_content and selected_topics:
    topics_json = json.dumps([", ".join([word for word, _ in topic]) for topic in selected_topics])

    # Save text for audio generation
    with open("selected_content.txt", "w") as f:
        f.write(selected_content)

    # Detect topic category
    category = classify_topic(selected_topics[0][0][0])  # Use first topic for classification
    print(f"🔍 Detected Category: {category}")

    # Run the appropriate animation
    if "biology" in category:
        subprocess.run(["python", "generate_biology_animation.py", category])
    elif "physics" in category:
        subprocess.run(["python", "generate_physics_animation.py", category])
    else:
        subprocess.run(["python", "generate_animation.py", topics_json])  # Default text-based animation

    # Generate audio
    subprocess.run(["python", "generate_audio.py", "selected_content.txt"])

    # Merge video & audio
    subprocess.run(["python", "combine_video_audio.py"])

else:
    st.warning("No relevant topics found. Please upload files in the Upload section.")
