from selenium.webdriver.common.by import By
from PyChromeController import PyChromeController
import time

def test_formsite_form():
    # PyChromeController initialisieren
    controller = PyChromeController()

    # Browser-Session starten
    controller.start_browser_session()

    try:
        # URL öffnen
        controller.open_url("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
        time.sleep(2)  # Warten, bis die Seite geladen ist

        # Vorname eingeben
        controller.enter_text(By.NAME, "RESULT_TextField-1", "Max")
        time.sleep(1)

        # Nachname eingeben
        controller.enter_text(By.NAME, "RESULT_TextField-2", "Mustermann")
        time.sleep(1)

        # Telefonnummer eingeben
        controller.enter_text(By.NAME, "RESULT_TextField-3", "0123456789")
        time.sleep(1)

        # Land eingeben
        controller.enter_text(By.NAME, "RESULT_TextField-4", "Deutschland")
        time.sleep(1)

        # Stadt eingeben
        controller.enter_text(By.NAME, "RESULT_TextField-5", "Berlin")
        time.sleep(1)

        # E-Mail-Adresse eingeben
        controller.enter_text(By.NAME, "RESULT_TextField-6", "max.mustermann@example.com")
        time.sleep(1)

        # Geschlecht auswählen (Radio Button) - Hier den Label-Klick verwenden
        controller.click_button(By.XPATH, "//label[@for='RESULT_RadioButton-7_0']")  # Male auswählen
        time.sleep(1)

        # Wochentage (Checkboxen) auswählen
        #controller.toggle_checkbox(By.ID, "RESULT_CheckBox-8_0", True)  # Sunday
        #controller.toggle_checkbox(By.ID, "RESULT_CheckBox-8_1", True)  # Monday
        #controller.toggle_checkbox(By.ID, "RESULT_CheckBox-8_2", True)  # Tuesday
        controller.toggle_checkbox(By.XPATH, "//label[@for='RESULT_CheckBox-8_0']", True)  # Sunday
        controller.toggle_checkbox(By.XPATH, "//label[@for='RESULT_CheckBox-8_1']", True)  # Monday
        controller.toggle_checkbox(By.XPATH, "//label[@for='RESULT_CheckBox-8_2']", True)  # Tuesday
        time.sleep(1)

        # Beste Zeit zur Kontaktaufnahme (Dropdown)
        controller.select_dropdown(By.NAME, "RESULT_RadioButton-9", value=None, visible_text="Morning")
        time.sleep(1)

        # Datei hochladen (optional)
        # Hier könnte der Datei-Upload-Code hinzugefügt werden, falls erforderlich
        # controller.enter_text(By.NAME, "RESULT_FileUpload-10", "Pfad_zur_Datei")

        time.sleep(5)

        # Formular abschicken
        controller.click_button(By.ID, "FSsubmit")
        time.sleep(2)

        print("Formular erfolgreich abgeschickt.")

    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
    finally:
        # Browser-Session beenden
        controller.close_browser()

test_formsite_form()
