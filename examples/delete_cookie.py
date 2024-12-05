from PyChromeController import PyChromeController

def test_delete_cookie():
    controller = PyChromeController()
    controller.start_browser_session()
    
    try:
        controller.open_url("https://example.com")
        time.sleep(2)
        
        # Cookie hinzufügen
        controller.add_cookie(name="test_cookie", value="test_value")
        
        # Cookie löschen
        cookie_deleted = controller.delete_cookie(name="test_cookie")
        assert cookie_deleted, "Das Löschen des Cookies ist fehlgeschlagen."
        
        # Überprüfen, ob das Cookie entfernt wurde
        cookies = controller.get_all_cookies()
        assert not any(cookie['name'] == "test_cookie" for cookie in cookies), "Cookie wurde nicht gelöscht."
        
        print("Test 'test_delete_cookie' erfolgreich.")
    except Exception as e:
        print(f"Ein Fehler ist im Test 'test_delete_cookie' aufgetreten: {e}")
    finally:
        controller.close_browser()

test_delete_cookie()
