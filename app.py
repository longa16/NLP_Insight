import streamlit as st
import pickle
import re

# --- CONFIGURATION ---
st.set_page_config(page_title="Analyse Avis Clients (NLP)", layout="centered")

# --- CHARGEMENT DES MODÈLES ---
try:
    tfidf = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))
    nmf = pickle.load(open('nmf_model.pkl', 'rb'))
except FileNotFoundError:
    st.error("Erreur : Les fichiers .pkl sont introuvables.")
    st.stop()


# --- FONCTION DE NETTOYAGE ---
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    return text


# --- INTERFACE ---
st.title(" Détecteur de Sujets (NLP)")
st.markdown("Colle un avis client pour comprendre automatiquement le problème.")

user_review = st.text_area("Avis du client (en Anglais) :", height=150,
                           placeholder="Example: The dress is beautiful but the size is way too small.")

if st.button("Analyser"):
    if not user_review:
        st.warning("Merci d'écrire un avis d'abord.")
    else:
        # 1. Nettoyage
        cleaned = clean_text(user_review)

        # 2. Transformation en chiffres (Vectorisation)
        vectorized = tfidf.transform([cleaned])

        # 3. Prédiction du Sujet (NMF)
        topic_scores = nmf.transform(vectorized)
        best_topic = topic_scores.argmax(axis=1)[0]
        confidence = topic_scores.max()

        # --- RÉSULTATS ---
        st.divider()

        topics_map = {
            0: "PROBLÈME DE TAILLE (Sizing)",
            1: "Qualité / Matière",
            2: "Style / Couleur",
            3: "Livraison / Service",
            4: "Autre"
        }

        predicted_label = topics_map.get(best_topic, "Sujet Inconnu")

        st.subheader(f"Sujet Détecté : {predicted_label}")

        # Logique Business spécifique
        if best_topic == 0:
            st.error(" **ALERTE BUSINESS :** Le client se plaint de la coupe. Risque de retour élevé.")
            st.write(" Action recommandée : Vérifier le guide des tailles pour ce produit.")
        else:
            st.success(" Ce sujet est généralement moins critique que les problèmes de taille.")
