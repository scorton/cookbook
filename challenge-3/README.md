# Challenge 3 — DarkWatch

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

## Analyse de Menaces OSINT (Threat Intelligence)

### Description
Le participant fournit un **nom de domaine**.  
Votre mission : conduire une **analyse OSINT complète** pour identifier signaux de menace, fuites, expositions, discussions suspectes publiques — **sans Dark Web réel**, uniquement des sources légales.

### Objectifs
- Collecter des données publiques sur le domaine  
- Rechercher mentions dans :
  - anciennes fuites anonymisées  
  - posts publics (forums, pastebins)  
  - blogs cyber  
  - rapports chercheurs  
  - Twitter/X, Reddit  
- Extraire entités sensibles : emails, IP, sous-domaines, tokens  
- Évaluer le risque : faible → critique  
- Générer un rapport professionnel

### Sources OSINT
- CERT-FR, CISA, ENISA  
- Rapid7, Qualys, Tenable, CheckPoint  
- BleepingComputer  
- Pastebin public  
- Tweets / articles cyber  
- HIBP (emails publics uniquement)

### Recherches Recommandées
- "domaine.com leak"  
- "domaine.com breach"  
- "domaine.com password"  
- "domaine.com data leak"  
- filetype:txt + email patterns

### Analyse attendue (exemples)
- 2 emails trouvés dans vieilles fuites → risque faible/moyen  
- API Key trouvée dans repo public → risque élevé  
- Aucune mention APT → menace faible active

### Livrables
- `osint_collector.py`  
- `osint_analyzer.py`  
- `report.md`  
