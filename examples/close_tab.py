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

    time.sleep(3)

    controller.close_tab_by_index(2)
    controller.close_first_tab()
    controller.close_last_tab()

    time.sleep(3)

    controller.open_new_tab("https://www.example.com")
    controller.open_new_tab("https://www.google.com")
    controller.open_new_tab("https://www.github.com")
    controller.open_url("https://facebook.com")

    time.sleep(3)

    controller.close_tab_by_url("https://www.google.com")
    controller.close_tab_by_title("GitHub")

    time.sleep(3)

    controller.open_new_tab("https://www.example.com")
    controller.open_new_tab("https://www.google.com")
    controller.open_new_tab("https://www.github.com")
    controller.open_url("https://facebook.com")

    controller.close_all_other_tabs()

test()
