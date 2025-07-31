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

            def find_scroll_and_edit_send_keys(locator, text_to_send):
                element = wait.until(EC.presence_of_element_located(locator))
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(0.5)  # Beri jeda singkat setelah scroll
                element.clear()
                element.send_keys(text_to_send)
                print(f"Berhasil mengisi '{text_to_send}' ke elemen: {locator}")

            wait.until(EC.element_to_be_clickable((By.ID, 'dropdownProfile'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Masuk')]"))).click()
            wait.until(EC.element_to_be_clickable((By.NAME, 'email'))).send_keys('buditabutitesting@gmail.com')
            wait.until(EC.element_to_be_clickable((By.ID, 'password-login'))).send_keys('*Buditabuti123')
            wait.until(EC.element_to_be_clickable((By.ID, 'remember_me'))).click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='login-form'] button[type='submit']"))).click()

            find_scroll_and_click((By.XPATH, "//div[@class='container-fluid pembatas-x pembatas-b d-flex flex-column gap-4']//div[3]//div[1]//a[1]"))
            find_scroll_and_click((By.XPATH, "//a[normalize-space()='Sunting']//a[@id='button-action-1']"))
            find_scroll_and_edit_send_keys((By.ID, 'work-title-text'), 'Edited Title TC008')
            find_scroll_and_edit_send_keys((By.ID, 'work-detail-text'), 'Edited Sample Job Details TC008')
            find_scroll_and_edit_send_keys((By.ID, 'work-address-text'), 'Jl. Contoh No. 456, Bogor')
            find_scroll_and_edit_send_keys((By.ID, 'work-start-date-text'), '19/08/2025')
            find_scroll_and_edit_send_keys((By.ID, 'work-start-time-text1'), '13:00')
            find_scroll_and_edit_send_keys((By.ID, 'work-end-date-text'), '20/08/2025')
            find_scroll_and_edit_send_keys((By.ID, 'work-end-time-text1'), '21:00')
            find_scroll_and_edit_send_keys((By.ID, 'work-price-text'), '430000')

            find_scroll_and_click((By.XPATH, "//button[normalize-space()='Selesai Edit']"))

            time.sleep(10)

        except Exception as e:
            print(f"Terjadi error: {e}")
            driver.save_screenshot("error_automasi.png")
            print("Screenshot disimpan sebagai error_automasi.png")

        finally:
            driver.quit()


findbyid = DemoFindElementByIDandName()
findbyid.locate_by_ID_demo()