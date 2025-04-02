import streamlit as st
import re

# --- Fonction de détection d’émotion (simplifiée) ---
def detect_emotion(text):
    text = text.lower()
    if any(word in text for word in ["triste", "vide", "perdu", "manque"]):
        return "tristesse"
    elif any(word in text for word in ["joie", "heureux", "rire", "sourire"]):
        return "joie"
    elif any(word in text for word in ["colère", "énervé", "rage", "fâché"]):
        return "colère"
    elif any(word in text for word in ["solitude", "seul", "isolé", "abandonné"]):
        return "solitude"
    else:
        return "nostalgie"

# --- Dictionnaire de prompts associés ---
emotion_prompts = {
    "joie": "a colorful garden full of happy people, sunshine, vibrant flowers",
    "tristesse": "a rainy city street at night, a lone figure under an umbrella, melancholic mood",
    "colère": "a stormy sky above a broken landscape, raw dramatic atmosphere",
    "solitude": "a person sitting alone on a bench, foggy morning, peaceful yet lonely",
    "nostalgie": "a vintage room with faded photographs and sunlight through old curtains"
}

# --- Application Streamlit ---
st.set_page_config(page_title="Exprime & Illustre", layout="centered")

st.title("🖋️ Exprime ton histoire & 🎨 Illustre ton émotion")
st.markdown("""
Écris ton histoire ou ton problème ci-dessous (maximum 2000 mots).  
L'application détectera l’émotion dominante et générera une image associée.  
""")

# RGPD consentement
consent = st.checkbox("✅ J’accepte que mon texte soit analysé pour générer une image. Aucune donnée n’est conservée (RGPD)")

# Saisie du texte
story = st.text_area("✍️ Ton histoire ici :", height=300, max_chars=15000)

# Affichage du compteur de mots
word_count = len(re.findall(r'\b\w+\b', story))
st.write(f"**{word_count} / 2000 mots**")

# Bouton de génération
if st.button("🎨 Générer une image"):

    if not consent:
        st.error("Merci de cocher la case RGPD pour continuer.")
    elif word_count > 2000:
        st.warning("Le texte dépasse 2000 mots. Réduis un peu le contenu.")
    elif word_count < 10:
        st.warning("Le texte est trop court pour détecter une émotion.")
    else:
        emotion = detect_emotion(story)
        prompt = emotion_prompts.get(emotion, "an abstract emotional scene")

        # Simule une image avec DummyImage (tu peux ici brancher DALL·E ou autre API)
        dummy_image_url = f"https://dummyimage.com/600x400/cccccc/000000&text={emotion}"

        st.success(f"Émotion détectée : **{emotion.upper()}**")
        st.markdown(f"**Prompt utilisé :** _{prompt}_")
        st.image(dummy_image_url, caption=f"Illustration générée (émotion : {emotion})")

