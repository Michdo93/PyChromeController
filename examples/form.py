from PyChromeController import PyChromeController
import time

def test_techlistic_form():
    # PyChromeController initialisieren
    controller = PyChromeController()

    # Browser-Session starten
    controller.start_browser_session()

    try:
        # URL öffnen
        controller.open_url("https://www.techlistic.com/p/selenium-practice-form.html")
        time.sleep(2)  # Warten, bis die Seite geladen ist

        # Formular ausfüllen
        controller.enter_text("By.XPATH", "//input[@name='firstname']", "Max")
        controller.enter_text("By.XPATH", "//input[@name='lastname']", "Mustermann")
        time.sleep(1)

        # Geschlecht auswählen (Radio Button)
        controller.click_button("By.XPATH", "//input[@id='sex-0']")
        time.sleep(1)

        # Erfahrung auswählen (Radio Button)
        controller.click_button("By.XPATH", "//input[@id='exp-2']")
        time.sleep(1)

        # Datum eingeben
        controller.enter_text("By.XPATH", "//input[@id='datepicker']", "12/12/2024")
        time.sleep(1)

        # Profession auswählen (Checkbox)
        controller.toggle_checkbox("By.XPATH", "//input[@id='profession-1']", True)
        time.sleep(1)

        # Tools auswählen (Checkbox)
        controller.toggle_checkbox("By.XPATH", "//input[@id='tool-2']", True)
        time.sleep(1)

        # Kontinent auswählen (Dropdown)
        controller.select_dropdown("By.XPATH", "//select[@id='continents']", value=None, visible_text="Europe")
        time.sleep(1)

        # Selenium Command auswählen (Mehrfachauswahl)
        controller.select_dropdown("By.XPATH", "//select[@id='selenium_commands']", value=None, visible_text="Browser Commands")
        time.sleep(1)

        # Formular abschicken
        controller.click_button("By.XPATH", "//button[@id='submit']")
        time.sleep(2)

        print("Formular erfolgreich abgeschickt.")
    
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
    finally:
        # Browser-Session beenden
        controller.close_browser()

test_techlistic_form()
