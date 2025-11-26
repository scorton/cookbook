# Challenge 2 — AppSleuth

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

## Analyse Comportementale d’Applications

### Contexte
Vous jouez le rôle d’un analyste cybersécurité chargé d’évaluer le comportement d’une application mobile.  
Objectif : comprendre ce qu’elle fait en arrière-plan (permissions, serveurs contactés, comportements suspects).

### Objectif du Challenge
- Recevoir des traces comportementales  
- Analyser les permissions, appels réseau, événements  
- Détecter signaux faibles, dérives, comportements anormaux  
- Construire une API de détection  
- Proposer une amélioration (règle, feature, signal)

### Types de Données Manipulées
1. **Permissions** : caméra, GPS, contacts, micro, stockage  
2. **Appels réseau** : endpoints, fréquence, volume, domaine  
3. **Événements** : ouverture app, capture photo, navigation  
4. **Métadonnées APK** : version, taille, SDK

### Ce qu’un analyste doit comprendre
- Permissions incohérentes  
- Envoi GPS après photo → signal faible  
- Appels réseau vers domaine inconnu → signal fort  

### Livrables
- API fonctionnelle d’analyse comportementale  
- Dataset minimal  
- Page d’audit claire  
