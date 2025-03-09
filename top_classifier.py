def classify_topic(topic):
    """Classifies the detected topic into relevant categories."""
    biology_keywords = {
        "digestive": ["digestion", "stomach", "intestines", "esophagus"],
        "circulatory": ["heart", "blood", "veins", "arteries"],
        "nervous": ["neurons", "brain", "nervous system", "spinal cord"],
        "excretory": ["kidney", "urine", "filtration"],
    }

    physics_keywords = {
        "electricity": ["current", "voltage", "resistance", "circuit"],
        "magnetism": ["magnetic field", "electromagnet", "induction"],
    }

    for category, keywords in biology_keywords.items():
        if any(word in topic.lower() for word in keywords):
            return f"biology_{category}"  # e.g., "biology_digestive"

    for category, keywords in physics_keywords.items():
        if any(word in topic.lower() for word in keywords):
            return f"physics_{category}"  # e.g., "physics_electricity"

    return "general"  # Default to general text analysis
