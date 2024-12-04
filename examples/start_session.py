from PyChromeController import PyChromeController

def start_browser_and_minimize():
    # PyChromeController initialisieren
    controller = PyChromeController()

    controller.start_browser_session()

    # Browser starten und Tabs öffnen
    controller.open_url("https://www.example.com")
    controller.open_new_tab("https://www.google.com")
    controller.open_new_tab("https://www.github.com")
    controller.open_url("https://facebook.com")

    # Minimieren des Browserfensters
    controller.minimize_window()

    # Session ID speichern (automatisch von der Bibliothek verwaltet)
    session_id = controller.driver.session_id
    with open("session_id.txt", "w") as file:
        file.write(session_id)
    print(f"Session ID gespeichert: {session_id}")

start_browser_and_minimize()
