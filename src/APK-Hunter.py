import re
import os
from urllib.parse import urlparse

def extraire_urls_depuis_apk(chemin_apk):
    """
    Simule la commande : strings fichier.apk | grep -Eo "https?://..."
    """
    print(f"📦 Lecture du fichier APK : {chemin_apk}...")
    
    if not os.path.exists(chemin_apk):
        print("❌ Erreur : Le fichier APK n'existe pas.")
        return []

    urls_trouvees = set() # Utiliser un set pour éviter les doublons instantanément

    try:
        # On ouvre le fichier en mode BINAIRE ('rb')
        with open(chemin_apk, 'rb') as f:
            content = f.read()
            
            # Regex équivalente à : "https?://[^\"\'\s<>]+"
            # On utilise une regex de type 'bytes' (rb"...") car on lit du binaire
            pattern = rb"https?://[^\"\'\s<>]+"
            
            matches = re.findall(pattern, content)
            
            # On décode les octets trouvés en chaînes de caractères (utf-8)
            for m in matches:
                try:
                    url_str = m.decode('utf-8', errors='ignore')
                    # Filtrage basique pour éviter les faux positifs trop courts
                    if len(url_str) > 8:
                        urls_trouvees.add(url_str)
                except:
                    continue
                    
    except Exception as e:
        print(f"❌ Erreur lors de la lecture de l'APK : {e}")
        return []

    print(f"🔍 Extraction terminée : {len(urls_trouvees)} URLs uniques trouvées.\n")
    return list(urls_trouvees)

def analyser_menaces(liste_urls):
    """
    Analyse la liste des URLs extraites avec des règles heuristiques.
    """
    # 1. WHITELIST (Bruit technique à ignorer)
    whitelist_stems = [
        'google', 'android', 'apple', 'microsoft', 'facebook', 
        'unity3d', 'unrealengine', 'w3.org', 'purl.org', 
        'schema.org', 'xml.org', 'adobe', 'autodesk',
        'cloudfront', 'akamai' # CDNs
    ]

    # 2. EXTENSIONS À RISQUE
    risky_tlds = [
        # --- Géographiques à haut risque / Faibles régulations ---
        '.ru', '.cn', '.ir', '.kp', '.su', '.vn', '.ng', '.pk',
        
        # --- Extensions gratuites ou très bon marché (Souvent abusées) ---
        '.tk', '.ml', '.ga', '.cf', '.gq',  # Le "gang" Freenom (souvent bloqué)
        '.xyz', '.top', '.club', '.work', '.site', '.info',
        
        # --- Nouveaux gTLDs à très faible réputation (Spam/Malware) ---
        '.gdn', '.buzz', '.fit', '.rest', '.bar', '.surf', 
        '.cam', '.icu', '.best', '.loan', '.monster', '.live', 
        '.click', '.link', '.pro', '.win', '.vip', '.bid',
        
        # --- Risques techniques / Confusion ---
        '.onion',  # Réseau Tor
        '.zip', '.mov',  # Dangereux car identiques à des extensions de fichiers
        '.download', '.stream', '.review'
    ]
    # 3. MOTS-CLÉS SUSPECTS
    keywords_suspects = [
        # --- Gaming / Triche / Warez (Votre base) ---
        'mod', 'hack', 'cheat', 'crack', 'patch', 'bypass', 'keygen',
        'emulator', 'root', 'jailbreak', 'aimbot', 'wallhack', 'trainer',
        'spoofer', 'noclip', 'godmode',
        
        # --- Distribution illégale / Serveurs ---
        'null', 'private', 'server', 'mirror', 'repack', 'warez', 
        'torrent', 'leaked', 'activator', 'license-key', 'serial',
        
        # --- Arnaques / Appâts (Scams) ---
        'free', 'gem', 'coin', 'money', 'unlock', 'vip', 'bet', 'win', 
        'gift', 'promo', 'bonus', 'giveaway', 'prize', 'winner',
        'generator', 'unlimited', 'glitch',
        
        # --- Phishing & Ingénierie Sociale (Urgence/Compte) ---
        'verify', 'signin', 'login', 'secure', 'account', 'update', 
        'confirm', 'wallet', 'invoice', 'billing', 'suspended', 
        'locked', 'security-alert', 'recover', 'support',
        
        # --- Crypto-monnaies (Souvent liées aux arnaques) ---
        'crypto', 'bitcoin', 'btc', 'eth', 'invest', 'forex', 'profit',
        'doubler', 'airdrop', 'presale',
        
        # --- Vecteurs techniques (Malware) ---
        'loader', 'inject', 'payload', 'dll', 'exe', 'iso', 'installer',
        'driver', 'bios', 'firmware', 'setup', 'downloader'
    ]

    urls_suspectes = []

    print(f"--- Analyse de sécurité en cours ---\n")

    for url in liste_urls:
        try:
            parsed = urlparse(url)
            domain = parsed.netloc.lower()
            path = parsed.path.lower()
        except:
            continue

        # A. Whitelist check
        if any(stem in domain for stem in whitelist_stems):
            continue

        raisons = []

        # B. Check TLDs
        for tld in risky_tlds:
            if domain.endswith(tld):
                raisons.append(f"Extension à risque ({tld})")
                break

        # C. Check Keywords
        for word in keywords_suspects:
            if word in domain or word in path:
                raisons.append(f"Mot-clé suspect ('{word}')")
                break

        # D. Check IP brute
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", domain):
            if not domain.startswith("127.0.0.1"):
                raisons.append("Connexion directe à une IP")

        # E. Check "Bizarre" (ex: http://n ou http://error.null)
        if '.' not in domain and 'localhost' not in domain:
            raisons.append("Domaine invalide ou incomplet")

        if raisons:
            urls_suspectes.append((url, raisons))

    # Affichage
    if urls_suspectes:
        print(f"🚨 {len(urls_suspectes)} MENACES POTENTIELLES DÉTECTÉES :\n")
        for url, causes in urls_suspectes:
            print(f"URL: {url}")
            for c in causes:
                print(f"  ❌ {c}")
            print("-" * 40)
    else:
        print("✅ Aucune URL suspecte détectée dans cet APK.")

# --- UTILISATION ---
# Remplacez ceci par le chemin réel de votre APK
fichier_apk = "clash-royale-mod_12.169.3-an1.com.apk" 

# Lancer le programme
urls = extraire_urls_depuis_apk(fichier_apk)
if urls:
    analyser_menaces(urls)