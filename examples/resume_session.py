from PyChromeController import PyChromeController

def connect_to_existing_browser_and_maximize():
    # Session ID aus der Datei laden
    with open("session_id.txt", "r") as file:
        session_id = file.read().strip()

    # Mit bestehendem Browser verbinden
    controller = PyChromeController()
    controller.attach_browser_session(session_id)

    # Fenster maximieren
    controller.maximize_window()

    # Schließe den ersten Tab
    controller.close_tab_by_index(0)

    print("Browser maximiert und erster Tab geschlossen.")

connect_to_existing_browser_and_maximize()
