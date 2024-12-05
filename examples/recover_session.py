from PyChromeController import PyChromeController

def test_get_all_cookies():
    controller = PyChromeController()
    controller.start_browser_session()
    
    try:
        controller.open_url("https://example.com")
        time.sleep(2)
        
        # Zwei Cookies hinzufügen
        controller.add_cookie(name="cookie1", value="value1")
        controller.add_cookie(name="cookie2", value="value2")
        
        # Cookies abrufen
        cookies = controller.get_all_cookies()
        assert len(cookies) >= 2, "Nicht alle Cookies wurden abgerufen."
        
        print("Cookies in der Sitzung:", cookies)
        print("Test 'test_get_all_cookies' erfolgreich.")
    except Exception as e:
        print(f"Ein Fehler ist im Test 'test_get_all_cookies' aufgetreten: {e}")
    finally:
        controller.close_browser()

test_get_all_cookies()
