from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

import time
import os
import pickle


class changeRole():
    def cookies_save(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)

        # cookies in job taker
        cookies_file = "../cookiesJobtaker.pkl"

        if os.path.exists(cookies_file):
            print("Memuat cookies...")
            cookies = pickle.load(open(cookies_file, "rb"))
            for cookie in cookies:
                driver.add_cookie(cookie)

            # Reload halaman agar cookies aktif
            driver.get("http://127.0.0.1:8000/job-taker/beranda")
        else:
            print("Login manual karena belum ada cookies...")

            driver.find_element(By.LINK_TEXT, "Tawarkan Kerja").click()

            email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
            email_input.send_keys("sonwt34@gmail.com")

            password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
            password_input.send_keys("@Kerjain17")

            driver.find_element(By.XPATH, "//button[contains(text(),'Masuk')]").click()

            time.sleep(2)

            # 1. Klik dropdown profil
            profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
            profile_dropdown.click()

            # 2. Klik "Ganti Peran"
            ganti_peran = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Ganti Peran']")))
            ganti_peran.click()

            # # first
            # driver.find_element(By.XPATH, "//input[@id='nama_depan']").send_keys("Wilsonff")
            # driver.find_element(By.XPATH, "//input[@id='nama_belakang']").send_keys("Tjoendddg")
            # driver.find_element(By.XPATH, "//input[@id='tanggal_lahir']").send_keys("10/05/2003")
            #
            # dropdown = Select(driver.find_element(By.XPATH, "//select[@id='jenis_kelamin']"))
            # dropdown.select_by_visible_text("Laki-laki")
            #
            # driver.find_element(By.XPATH, "//input[@id='nomor_telepon']").send_keys("085239202058")
            # driver.find_element(By.XPATH, "//input[@id='nomor_ktp']").send_keys("3578101510200900")
            # driver.find_element(By.XPATH, "//input[@id='alamat']").send_keys("jalan pakuan no 3")
            # time.sleep(2)
            #
            # driver.find_element(By.XPATH, "//button[normalize-space()='Lanjut']").click()
            # time.sleep(5)
            #
            # # second
            # driver.find_element(By.XPATH, "//input[@id='agree_terms']").click()
            # driver.find_element(By.XPATH, "//input[@id='agree_data_usage']").click()
            # driver.find_element(By.XPATH, "//button[@id='submitButton']").click()
            # time.sleep(5)
            #
            # # third
            # driver.find_element(By.XPATH, "//input[@id='selfie_photo']").send_keys("biskuitbayi.jpg")
            # time.sleep(2)
            # driver.find_element(By.XPATH, "//input[@id='id_card_photo']").send_keys("biskuitbayi.jpg")
            # time.sleep(2)
            # driver.find_element(By.XPATH, "//input[@id='selfie_with_id_card_photo']").send_keys("biskuitbayi.jpg")
            # time.sleep(2)
            #
            # driver.find_element(By.XPATH, "//input[@id='account_name']").send_keys("Budi Santoso")
            # driver.find_element(By.XPATH, "//input[@id='account_number']").send_keys("123456789")
            #
            # # confirmation message
            # driver.find_element(By.XPATH, "//button[contains(text(),'Simpan dan')]").click()
            # time.sleep(5)
            #
            # driver.find_element(By.XPATH, "//a[normalize-space()='Kembali ke Beranda']").click()
            # time.sleep(5)
            #
            # # 1. Klik tombol dropdown profil
            # profile_dropdown = driver.find_element(By.ID, "dropdownProfile")
            # profile_dropdown.click()
            # time.sleep(1)
            #
            # # 2. Klik pilihan "Menjadi Mitra" dari menu dropdown
            # driver.find_element(By.XPATH, "//a[normalize-space()='Ganti Peran']").click()
            # time.sleep(2)

            # Setelah login, simpan cookies
            print("Menyimpan cookies...")
            pickle.dump(driver.get_cookies(), open(cookies_file, "wb"))

            driver.get("http://127.0.0.1:8000/job-taker/beranda")  # reload untuk pastikan session aktif

        # Tunggu 30 detik agar kamu bisa lihat hasilnya
        time.sleep(15)
        driver.quit()

    def jobRequestertoJobTaker(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)
        driver.find_element(By.LINK_TEXT, "Tawarkan Kerja").click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("sonwt34@gmail.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Kerjain17")

        driver.find_element(By.XPATH, "//button[contains(text(),'Masuk')]").click()
        time.sleep(5)

        # 1. Klik tombol dropdown profil
        profile_dropdown = driver.find_element(By.ID, "dropdownProfile")
        profile_dropdown.click()
        time.sleep(1)

        # 2. Klik pilihan "Menjadi Mitra" dari menu dropdown
        driver.find_element(By.XPATH, "//a[normalize-space()='Ganti Peran']").click()

        time.sleep(15)
        driver.quit()

    def jobTakertoJobRequester(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)

        cookies_file = "../cookiesJobtaker.pkl"

        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Reload halaman agar cookies aktif
        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        # 1. Klik tombol dropdown profil
        profile_dropdown = driver.find_element(By.ID, "dropdownProfile")
        profile_dropdown.click()
        time.sleep(1)

        # 2. Klik pilihan "Menjadi Mitra" dari menu dropdown
        driver.find_element(By.XPATH, "//a[normalize-space()='Ganti Peran']").click()
        time.sleep(2)

        # Tunggu 30 detik agar kamu bisa lihat hasilnya
        time.sleep(15)
        driver.quit()

# saving cookies in Job Taker, so i dont need to doing same code anymore
saving = changeRole()
saving.cookies_save()

# Job Requester to Job Taker
# changeReqtoTaker = changeRole()
# changeReqtoTaker.jobRequestertoJobTaker()

# Job Taker to Job Requester
# changeTakertoReq = changeRole()
# changeTakertoReq.jobTakertoJobRequester()


