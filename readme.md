# 🗣️  NLP & Insights 

## Contexte Business
Les avis clients sont une mine d'or d'informations souvent inexploité car non structurée. Une simple analyse de sentiment (Positif/Négatif) ne suffit pas à comprendre les **causes racines** de l'insatisfaction.
Ce projet vise à automatiser l'extraction d'insights à partir de milliers d'avis textuels pour identifier les points de friction spécifiques sans lecture manuelle.

## Stack Technique
* **Langage :** Python 3.x
* **Bibliothèques :** Pandas, Scikit-learn (NMF, TF-IDF), Seaborn.
* **NLP :** Nettoyage de texte (Regex), Stopwords, Lemmatization.
* **Algorithme :** Non-Negative Matrix Factorization (NMF) pour le Topic Modeling.

## Méthodologie

### 1. Prétraitement du Texte 
* Nettoyage des caractères spéciaux et normalisation (minuscules).
* Vectorisation **TF-IDF**  pour transformer le texte en matrice numérique, en filtrant les termes trop fréquents ou trop rares.

### 2. Modélisation des Sujets 
Utilisation de l'algorithme **NMF** pour extraire 5 thèmes latents dans le corpus d'avis.
* **Identification des thèmes :** Analyse des mots-clés les plus pondérés pour chaque topic.
* **Topic 0 identifié :** Problèmes de Taille/Coupe ("Size", "Fit", "Small", "Large").

### 3. Analyse Croisée 
Corrélation entre le sujet dominant d'un avis et la note attribuée par le client.

## Résultats Clés

L'analyse a révélé une disparité critique dans la satisfaction client selon le sujet abordé :

| Sujet (Topic) | Thème Identifié | Impact sur la Satisfaction |
| :--- | :--- | :--- |
| **Topic 0** | **Taille & Coupe (Sizing)** | 🔴 **Impact Négatif Majeur** (Note la plus basse) |
| **Topic X** | Qualité/Matière | 🟢 Neutre / Positif |
| **Topic Y** | Style/Esthétique | 🟢 Positif |

## Recommandation Stratégique
Les données montrent que le **"Sizing"** est le principal vecteur d'insatisfaction (Pain Point).
**Action recommandée :** Audit immédiat du guide des tailles sur le site e-commerce et implémentation d'un outil d'aide au choix de la taille pour réduire le taux de retours.