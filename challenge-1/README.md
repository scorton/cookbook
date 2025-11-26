# Challenge 1 — VibeStream

## 🔧 Test Scorton Extension & API

## 🌐 Tester l’Extension Scorton (Chrome & Firefox)
Pour accéder à l’API Scorton et créer votre compte, vous devez passer par l’extension :

- **Extension Chrome** : point d’entrée sécurisé pour l’authentification et l’analyse de sites.
[Accéder à l'extension Chrome](https://chromewebstore.google.com/detail/dcnejfdbdngpaiddpolodngobfddjmgh?utm_source=item-share-cb)

- **Extension Firefox** : mêmes fonctionnalités, compatible avec Gecko.
[Accéder à l'extension Firefox](https://addons.mozilla.org/fr/firefox/addon/cyberscor/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search)

> L’extension sert de point d’entrée sécurisé pour l’inscription et la gestion utilisateur.

## 🛠️ Accès à l’API Scorton
Une fois authentifié via l’extension, vous pouvez interagir directement avec l’API.

### **Endpoints principaux**
- [Accéder à la documentation OpenAPI](https://radar.scorton.tech)
- [Accéder à la documentation Swagger](https://radar.scorton.tech/docs)
- [Accéder à la Gradio UI](https://radar.scorton.tech/ui)


## 🧭 Workflow recommandé
1. Installer l’extension Chrome ou Firefox  
2. Créer un compte depuis l’extension  
4. Tester vos appels API via :  
   - `/ui`
   - `/docs`
   - vos scripts externes


## 📌 Notes
- L’API est sécurisée : l’extension vous permet de créer un compte et vous générez un token unique par utilisateur.
- Toute consommation API directe nécessite un token valide.

---

## Analyse Externe & Détection de Signaux Cyber

### Contexte
Dans le domaine de la cybersécurité moderne, la capacité à analyser rapidement un site web, identifier des signaux faibles et détecter des comportements anormaux est essentielle.  
Ce challenge simule une mission d’analyste cyber : comprendre un environnement externe, collecter les bons indicateurs et formuler des hypothèses pertinentes.

### Objectif du Challenge
Réaliser un scan externe complet d’un site web (sans accès interne, sans score) afin de :
- collecter les données techniques essentielles,
- identifier des signaux faibles et forts,
- formuler des hypothèses sur d’éventuels risques ou comportements atypiques.

### Tâches Attendues
#### 1. Collecte & Ingestion
- Récupération du HTML, headers, certificat TLS, redirections, SSL.
- Extraction WHOIS : dates clés, registrar, durée de vie du domaine.

#### 2. Analyse & Détection
- Certificat faible ou expirant  
- Redirection anormale  
- Taille HTML anormale  
- Absence de HTTPS  
- Technologies obsolètes  
- Détection de signaux faibles

#### 3. Hypothèses & Interprétation
- Explication simple : “Ce signal pourrait indiquer X”
- Analyse contextualisée : impact, sévérité, probabilité

#### Optionnel
- Envoi des résultats vers une API externe  
- Mini‑pipeline (fetch → parse → analyse → synthèse)

### Critères de Réussite
- Détection d’au moins une anomalie non triviale  
- Justification claire  
- Proposition d’une amélioration ou nouvelle feature  
- Rapport final professionnel

### Livrables
- API de collecte et analyse de données  
- Dataset minimal  
- Page d’audit claire

### Bonus
- Détection d’un signal faible avant qu’il ne devienne critique  
- Optimisations (cache WHOIS, perf)  
- Visualisation (timeline, tableau)
