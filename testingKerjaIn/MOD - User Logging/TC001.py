from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class DemoFindElementByIDandName():
    def locate_by_ID_demo(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")

        try:
            wait = WebDriverWait(driver, 10)

            def find_scroll_and_click(locator):
                element = wait.until(EC.presence_of_element_located(locator))
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(0.5)  # Beri jeda singkat setelah scroll
                driver.execute_script("arguments[0].click();", element)
                print(f"Berhasil mengklik elemen: {locator}")

            def find_scroll_and_send_keys(locator, text_to_send):
                element = wait.until(EC.presence_of_element_located(locator))
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(0.5)  # Beri jeda singkat setelah scroll
                element.send_keys(text_to_send)
                print(f"Berhasil mengisi '{text_to_send}' ke elemen: {locator}")

            find_scroll_and_click((By.ID, "dropdownProfile"))
            find_scroll_and_click((By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']"))
            find_scroll_and_send_keys((By.NAME, "email"),"admin@example.com")
            find_scroll_and_send_keys((By.ID, "password-login"), "@Super645!")
            find_scroll_and_click((By.ID, "remember_me"))
            find_scroll_and_click((By.CSS_SELECTOR, "form[id='login-form'] button[type='submit']"))
            find_scroll_and_click((By.XPATH, "//div[@class='container-fluid p-0']//a[1]"))

            find_scroll_and_click((By.ID, "users-link"))

            time.sleep(10)

        except Exception as e:
            print(f"Terjadi error: {e}")
            driver.save_screenshot("error_automasi.png")
            print("Screenshot disimpan sebagai error_automasi.png")

        finally:
            driver.quit()


findbyid = DemoFindElementByIDandName()
findbyid.locate_by_ID_demo()