from PyChromeController import PyChromeController
import time

def test():
    # PyChromeController initialisieren
    controller = PyChromeController()

    controller.start_browser_session()

    # Browser starten und Tabs öffnen
    controller.open_url("https://www.example.com")
    controller.open_new_tab("https://www.google.com")
    controller.open_new_tab("https://www.github.com")
    controller.open_new_tab("https://facebook.com")

    time.sleep(3)

    controller.change_url_of_tab("https://www.instagram.com", 1)

    time.sleep(2)
  
    controller.change_url_of_tab_by_url("https://facebook.com", "https://www.youtube.com/")

    time.sleep(2)

    controller.change_url_of_tab_by_title("Domain", "https://web.whatsapp.com/")

test()
