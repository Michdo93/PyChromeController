from PyChromeController import PyChromeController
import time

def test():
    # PyChromeController initialisieren
    controller = PyChromeController()

    controller.start_browser_session()

    # Browser starten und Tabs öffnen
    controller.open_url("https://www.example.com")

    time.sleep(3)

    print(controller.get_console_logs())
    print(controller.get_network_logs())

test()
