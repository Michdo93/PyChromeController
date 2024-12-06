from PyChromeController import PyChromeController
import time

def test():
    # PyChromeController initialisieren
    controller = PyChromeController()

    controller.start_browser_session()

    # Browser starten und Tabs öffnen
    controller.open_url("https://www.example.com")
    controller.check_and_open_tab_by_url("https://www.google.com")
    controller.check_and_open_tab_by_url("https://www.github.com")
    controller.check_and_open_tab_by_url("https://facebook.com")

    time.sleep(3)

    controller.check_and_open_tab_by_url("https://www.google.com")

    time.sleep(1)
  
    controller.check_and_open_tab_by_url("https://www.github.com")

    time.sleep(1)

    controller.check_and_open_tab_by_url("https://facebook.com")

    time.sleep(1)

    controller.check_and_open_tab_by_title("Domain", "https://www.example.com")

    time.sleep(1)

    controller.check_and_open_tab_by_title("YouTube", "https://www.youtube.com/")

test()
