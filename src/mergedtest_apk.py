import subprocess
import glob
import json
import os
import requests

# -----------------------------
# Entrée APK
# -----------------------------
APK = input("Entrez le nom du fichier APK à analyser : ")

# -----------------------------
# Commandes des outils
# -----------------------------
TOOLS = {
    "APKDeepLens": f"python3 ~/APKDeepLens/APKDeepLens.py -apk {APK} -report json -o deep_report.json",
    "MobSF": None,  # MobSF via API
    "Androguard": f"androguard apk {APK} -o androguard_output.json",
    "QARK": f"qark --apk {APK} --report-type json"
}

# -----------------------------
# Fonction pour lancer un outil
# -----------------------------
def run_tool(name, cmd):
    if not cmd:
        print(f"\n▶ {name} doit être exécuté via API ou manuellement.")
        return
    print(f"\n▶ Running {name}...")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

# -----------------------------
# Lancer tous les outils CLI
# -----------------------------
for name, cmd in TOOLS.items():
    run_tool(name, cmd)

# -----------------------------
# MobSF via API
# -----------------------------
# Si tu veux récupérer MobSF automatiquement
MOBSF_URL = "http://127.0.0.1:8000/api/v1/upload"
API_KEY = "your_api_key"  # Remplace par ta clé MobSF

if os.path.exists(APK):
    try:
        with open(APK, 'rb') as f:
            files = {'file': f}
            headers = {'Authorization': API_KEY}
            r = requests.post(MOBSF_URL, files=files, headers=headers)
            mobsf_data = r.json()
    except Exception as e:
        print(f"Erreur MobSF : {e}")
        mobsf_data = {}
else:
    mobsf_data = {}

# -----------------------------
# Fusionner les rapports JSON
# -----------------------------
consolidated = {
    "package_name": None,
    "permissions": set(),
    "dangerous_permissions": set(),
    "activities": set(),
    "exported_activities": set(),
    "receivers": set(),
    "exported_receivers": set(),
    "providers": set(),
    "insecure_connections": set(),
    "hardcoded_secrets": [],
    "tool_reports": {}
}

# Chemins des rapports générés
report_paths = {
    "APKDeepLens": glob.glob("deep_report.json/reports/*.json"),
    "Androguard": glob.glob("androguard_output.json"),
    "QARK": glob.glob("qark_report/*.json"),
    "MobSF": []  # MobSF via API
}

for tool, paths in report_paths.items():
    for path in paths:
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        consolidated["tool_reports"][tool] = data
        for key in ["permissions", "dangerous_permissions", "activities",
                    "exported_activities", "receivers", "exported_receivers", "providers"]:
            if key in data:
                consolidated[key].update(data[key])
        if "insecure_connections" in data and isinstance(data["insecure_connections"], list):
            consolidated["insecure_connections"].update(data["insecure_connections"])
        if "hardcoded_secrets" in data:
            consolidated["hardcoded_secrets"].extend(data["hardcoded_secrets"])
        if not consolidated["package_name"] and "package_name" in data:
            consolidated["package_name"] = data["package_name"]

# Ajouter MobSF si présent
if mobsf_data:
    consolidated["tool_reports"]["MobSF"] = mobsf_data
    for key in ["permissions", "dangerous_permissions", "activities",
                "exported_activities", "receivers", "exported_receivers", "providers"]:
        if key in mobsf_data:
            consolidated[key].update(mobsf_data[key])
    if "insecure_connections" in mobsf_data and isinstance(mobsf_data["insecure_connections"], list):
        consolidated["insecure_connections"].update(mobsf_data["insecure_connections"])
    if "hardcoded_secrets" in mobsf_data:
        consolidated["hardcoded_secrets"].extend(mobsf_data["hardcoded_secrets"])
    if not consolidated["package_name"] and "package_name" in mobsf_data:
        consolidated["package_name"] = mobsf_data["package_name"]

# -----------------------------
# Générer un rapport lisible
# -----------------------------
rapport = f"===============================\nRAPPORT CONSOLIDE APK : {APK}\n===============================\n"
rapport += f"Package : {consolidated['package_name']}\n\n"
rapport += "Permissions :\n" + "\n".join(" - " + p for p in consolidated["permissions"]) + "\n\n"
rapport += "Permissions dangereuses :\n" + ("\n".join(" - " + p for p in consolidated["dangerous_permissions"]) or "Aucune") + "\n\n"
rapport += "Activities :\n" + "\n".join(" - " + a for a in consolidated["activities"]) + "\n\n"
rapport += "Exported Activities :\n" + ("\n".join(" - " + a for a in consolidated["exported_activities"]) or "Aucune") + "\n\n"
rapport += "Receivers :\n" + "\n".join(" - " + r for r in consolidated["receivers"]) + "\n\n"
rapport += "Exported Receivers :\n" + ("\n".join(" - " + r for r in consolidated["exported_receivers"]) or "Aucun") + "\n\n"
rapport += "Providers :\n" + "\n".join(" - " + p for p in consolidated["providers"]) + "\n\n"
rapport += "Connexions non sécurisées :\n" + ("\n".join(" - " + c for c in consolidated["insecure_connections"]) or "Aucune") + "\n\n"

rapport += "Secrets hardcodés :\n"
for s in consolidated["hardcoded_secrets"]:
    file = s.get("file", "Unknown file")
    type_ = s.get("type", "Unknown type")
    value = s.get("value", "Unknown value")
    rapport += f" - {file} | {type_} | {value}\n"

with open("rapport_consolide.txt", "w", encoding="utf-8") as f:
    f.write(rapport)

print("✔ Rapport consolidé généré : rapport_consolide.txt")
