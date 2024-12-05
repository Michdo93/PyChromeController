from PyChromeController import PyChromeController
import time

def test():
    # PyChromeController initialisieren
    controller = PyChromeController()

    controller.start_browser_session()

    # Browser starten und Tabs öffnen
    controller.open_url("https://www.example.com")
  
    # Minimieren des Browserfensters
    controller.minimize_window()

    time.sleep(5)

    controller.maximize_window()

test()
