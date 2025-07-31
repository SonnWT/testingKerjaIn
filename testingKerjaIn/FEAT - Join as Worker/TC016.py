from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
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
                time.sleep(1)  # Beri jeda singkat setelah scroll
                driver.execute_script("arguments[0].click();", element)
                print(f"Berhasil mengklik elemen: {locator}")

            def find_scroll_and_select_dropdown(select_locator, value_to_select):
                element = wait.until(EC.presence_of_element_located(select_locator))
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                select = Select(element)
                select.select_by_value(value_to_select)
                print(f"Dropdown: {value_to_select}")

            def find_scroll_and_send_keys(locator, text_to_send):
                element = wait.until(EC.presence_of_element_located(locator))
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(0.5)  # Beri jeda singkat setelah scroll
                element.send_keys(text_to_send)
                print(f"Berhasil mengisi '{text_to_send}' ke elemen: {locator}")

            wait.until(EC.element_to_be_clickable((By.ID, 'dropdownProfile'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Masuk')]"))).click()
            wait.until(EC.element_to_be_clickable((By.NAME, 'email'))).send_keys('buditabutitesting@gmail.com')
            wait.until(EC.element_to_be_clickable((By.ID, 'password-login'))).send_keys('*Buditabuti123')
            wait.until(EC.element_to_be_clickable((By.ID, 'remember_me'))).click()
            wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='login-form'] button[type='submit']"))).click()

            find_scroll_and_click((By.ID, "dropdownProfile"))
            find_scroll_and_click((By.XPATH, "//a[normalize-space()='Menjadi Mitra']"))
            find_scroll_and_send_keys((By.ID, 'nama_depan'), 'Budi')
            find_scroll_and_send_keys((By.ID, 'nama_belakang'), 'Tabuti')
            find_scroll_and_send_keys((By.ID, 'tanggal_lahir'), '08/08/2004')
            find_scroll_and_select_dropdown((By.ID, 'jenis_kelamin'), 'Male')
            find_scroll_and_send_keys((By.ID, 'nomor_telepon'), '081234567890')
            find_scroll_and_send_keys((By.ID, 'nomor_ktp'), '1234567890123456')
            find_scroll_and_send_keys((By.ID, 'alamat'), 'Jl. Contoh No. 1, Jakarta')
            find_scroll_and_click((By.XPATH, "//button[normalize-space()='Lanjut']"))

            find_scroll_and_click((By.ID, "agree_terms"))
            find_scroll_and_click((By.ID, "agree_data_usage"))
            find_scroll_and_click((By.ID, "submitButton"))

            find_scroll_and_send_keys((By.ID, 'selfie_photo'), 'C://Users//agust//Downloads//foto_diri.pdf')
            find_scroll_and_send_keys((By.ID, 'id_card_photo'), 'C://Users//agust//Downloads//foto_ktp.pdf')
            find_scroll_and_send_keys((By.ID, 'selfie_with_id_card_photo'),'C://Users//agust//Downloads//foto_diri_ktp.pdf')
            find_scroll_and_send_keys((By.ID, 'account_name'), 'Budi Tabuti')
            find_scroll_and_send_keys((By.ID, 'account_number'), '1234567890')
            find_scroll_and_click((By.XPATH, "//button[contains(text(),'Simpan dan')]"))

            time.sleep(10)

        except Exception as e:
            print(f"Terjadi error: {e}")
            driver.save_screenshot("error_automasi.png")
            print("Screenshot disimpan sebagai error_automasi.png")

        finally:
            driver.quit()


findbyid = DemoFindElementByIDandName()
findbyid.locate_by_ID_demo()
