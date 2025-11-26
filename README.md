# Scorton Hackathon — Cybersecurity Challenges
Analyse Web • Comportements Applicatifs A.K.A Vibe Night• OSINT & Threat Intelligence

Bienvenue dans le **Scorton Cybersecurity Hackathon A.K.A VIBENight **, un ensemble de trois challenges techniques destinés à évaluer et développer vos compétences en analyse de sécurité, investigation, collecte de signaux, et compréhension des menaces modernes.

---

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

## 🚀 Structure du Dépôt
```
scorton-hackathon/
│
├── challenge-1/        → VibeStream : Analyse externe de site & signaux web
├── challenge-2/        → AppSleuth : Analyse comportementale d’applications
├── challenge-3/        → DarkWatch : Analyse OSINT d’un domaine
└── README.md           → (Vous êtes ici)
```

---

## 🎯 Objectifs Pédagogiques
- Analyse technique web (HTTP, TLS, WHOIS...)
- Analyse comportementale d’applications
- OSINT & Threat Intelligence
- Extraction d’entités et signaux faibles
- Rédaction d’un rapport professionnel

---

## 🧩 Aperçu des Challenges

### **Challenge 1 — VibeStream**
Analyse externe d’un site web :
- Scan technique  
- Extraction de signaux faibles et forts  
- Détection d’anomalies  
- Hypothèses de risques  

---

### **Challenge 2 — AppSleuth**
Analyse comportementale d’une application :
- Permissions  
- Appels réseau  
- Séquences d’événements  
- Indicateurs de risques  

---

### **Challenge 3 — DarkWatch**
Analyse OSINT d’un domaine fourni par le client :
- Recherche de mentions publiques  
- Analyse de fuites anciennes anonymisées  
- Extraction d’entités sensibles  
- Évaluation du risque  

---

## 🧪 Attentes Globales
- Analyse structurée et justifiée  
- Travail individuel ou en équipe  
- Code clair (si applicable)  
- Rapport lisible et concret  

---

## 📬 Modalités de Soumission
### Fork + Pull Request  

---

## 🛡️ Règles et Sécurité
- Aucune action illégale  
- Aucun accès réel au Dark Web  
- Usage exclusif de données publiques ou générées  
- Approche analytique uniquement  

---

## 🔧 Prérequis Techniques
- Python 3.9+  
- Notions HTTP / TLS / DNS  
- Bases OSINT  

---

## 🔥 Commencer
Consultez :
- `challenge-1/README.md`  
- `challenge-2/README.md`  
- `challenge-3/README.md`  
