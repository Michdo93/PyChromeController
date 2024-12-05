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
    controller.open_url("https://facebook.com")

    time.sleep(2)

    print(controller.get_all_urls())
    print(controller.get_all_titles())

test()
