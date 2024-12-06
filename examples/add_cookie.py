from PyChromeController import PyChromeController
import time

def test_add_cookie():
    controller = PyChromeController()
    controller.start_browser_session()
    
    try:
        # Eine Test-Website öffnen
        controller.open_url("https://example.com")
        time.sleep(2)
        
        # Cookie hinzufügen
        cookie_added = controller.add_cookie(name="test_cookie", value="test_value")
        assert cookie_added, "Das Hinzufügen des Cookies ist fehlgeschlagen."
        
        # Überprüfen, ob das Cookie existiert
        cookies = controller.get_all_cookies()
        assert any(cookie['name'] == "test_cookie" for cookie in cookies), "Cookie nicht gefunden."
        
        print("Test 'test_add_cookie' erfolgreich.")
    except Exception as e:
        print(f"Ein Fehler ist im Test 'test_add_cookie' aufgetreten: {e}")
    finally:
        controller.close_browser()

test_add_cookie()
