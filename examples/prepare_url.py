from PyChromeController import PyChromeController
from urllib.parse import urlparse
import os

def test():
    # PyChromeController initialisieren
    controller = PyChromeController()

    controller.start_browser_session()

    # Browser starten und Tabs öffnen
    controller.open_url(prepare_url("html.html"))  # Lokale Datei -> file://[absoluter Pfad]
    controller.open_new_tab(prepare_url("file:///home/ubuntu/html.html"))  # Schon korrekt
    controller.open_new_tab(prepare_url("http://example.com"))  # URL bleibt unverändert
    controller.open_new_tab(prepare_url("www.example.com"))  # URL bleibt unverändert
    controller.open_new_tab(prepare_url("192.168.1.1"))  # IP-Adresse bleibt unverändert

def is_valid_ip_address(ip):
    """
    Überprüft, ob die Eingabe eine valide IP-Adresse ist.
    """
    parts = ip.split('.')
    if len(parts) != 4:  # IP-Adresse muss aus genau 4 Teilen bestehen
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

def prepare_url(input_path_or_url):
    """
    Überprüft eine Eingabe, ob sie eine URL oder ein lokaler Dateipfad ist,
    und fügt falls notwendig 'file://' für lokale Pfade hinzu.

    :param input_path_or_url: Die URL oder der lokale Pfad
    :return: Eine gültige URL oder ein Dateipfad mit 'file://'
    """
    if not isinstance(input_path_or_url, str):
        raise ValueError("Die Eingabe muss ein String sein.")
    
    # Parse die Eingabe
    parsed = urlparse(input_path_or_url)
    
    # Prüfen, ob es bereits eine vollständige URL ist
    if parsed.scheme in ('http', 'https', 'file'):
        return input_path_or_url  # Bereits eine gültige URL oder Datei-URL
    
    # Prüfen, ob es sich um eine Webadresse ohne Schema handelt
    if "." in input_path_or_url and not os.path.exists(input_path_or_url):
        return f"http://{input_path_or_url}"  # Standardmäßig 'http://' hinzufügen
    
    # Prüfen, ob es eine gültige IP-Adresse ist
    if is_valid_ip_address(input_path_or_url):
        return f"http://{input_path_or_url}"  # Standardmäßig 'http://' hinzufügen
    
    # Wenn keine der obigen Bedingungen zutrifft, ist es vermutlich ein lokaler Pfad
    absolute_path = os.path.abspath(input_path_or_url)  # Absoluten Pfad ermitteln
    return f"file://{absolute_path}"  # file:// hinzufügen

test()
