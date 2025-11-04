"""
    author: feezyhendrix

    Configuration file
    NOTE: leave use_custom_proxy=False if you don't use proxies.
"""
import os
import logging

logging.basicConfig(level=logging.INFO)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSET_DIR = os.path.join(BASE_DIR, "Assets")

# Chemin simplifié pour le ChromeDriver (déplacé à la racine 'drivers')
# Si tu gardes l’ancien chemin long, remets-le ici.
CHROMEDRIVER_PATH = r"C:\Users\moura\OneDrive\Bureau\Insta-mass-account-creator\drivers\chromedriver.exe"

Config = {
    # 1 = Selenium, 2 = requests (selon le projet)
    "bot_type": 1,

    # Chemin vers chromedriver.exe (utilisé explicitement par le code Selenium)
    "chromedriver_path": r"C:\Users\moura\OneDrive\Bureau\Insta-mass-account-creator\drivers\chromedriver.exe",

    # Proxies: désactivés
    "use_custom_proxy": False,
    "use_local_ip_address": True,

    # Fichier de proxies (non utilisé si use_custom_proxy=False)
    "proxy_file_path": os.path.join(ASSET_DIR, "proxies.txt"),

    # Paramètres divers du projet (garde les valeurs d’origine si besoin)
    "amount_of_account": 1,
    "amount_per_proxy": 1,

    "email_domain": "gmail.com",
    "country": "it",

    # Remplacer par tes identifiants si le projet les utilise
    "activation_email_addr": "xxxxxxxxxxxxxxxx",
    "activation_email_pass": "xxxxxxxxxxxxxxxx",
    "activation_email_serv": "xxxxxxxxxxxxxxxx",
    "activation_email_spor": 993,
}
