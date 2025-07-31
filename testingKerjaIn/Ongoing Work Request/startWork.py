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


class startWorkFunctionality():
    def cookies_save(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/beranda")
        driver.find_element(By.LINK_TEXT, "Cari Kerja").click()
        time.sleep(2)

        # Klik detail job pertama
        element = driver.find_element(By.XPATH,
                                      "//div[@class='container-fluid pembatas-x pembatas-y d-flex gap-4']//div[2]//ul[1]//button[1]")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()

        # Klik tombol "Terima"
        hubungiBtn = driver.find_element(By.XPATH,
                                         "//div[@class='detail-buttons-placeholder d-flex gap-2 justify-content-end mt-auto align-items-center']//button[@class='details-button-item btn-terima-modal'][normalize-space()='Terima']")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hubungiBtn)
        time.sleep(2)
        hubungiBtn.click()

        # Klik "Ya, Saya Yakin"
        sureBtn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='confirm-accept-job']")))
        sureBtn.click()
        time.sleep(5)

        driver.find_element(By.LINK_TEXT, "Beranda").click()
        time.sleep(2)

        element_card = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                              "//body/main[@class='main-content']/div[@class='container-fluid pembatas-x pembatas-b d-flex flex-column gap-4']/div[@class='d-flex']/div[@class='col-12 col-xl-8 d-flex flex-column gap-4 beranda-req-kiri']/div[1]")))
        element_card.click()
        time.sleep(2)

        # Scroll dan klik tombol "Mulai Kerja"
        start_button = driver.find_element(By.XPATH, "//button[@id='start-work-button']")
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", start_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", start_button)

        print("Menyimpan cookies...")
        pickle.dump(driver.get_cookies(), open(cookies_file, "wb"))

    def TC001(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        driver.find_element(By.LINK_TEXT, "Cari Kerja").click()
        time.sleep(2)

        # Click detail button in the first job that appear
        element = driver.find_element(By.XPATH, "//div[9]//ul[1]//button[1]")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)  # opsional: beri jeda
        element.click()

        # Temukan elemen terlebih dahulu
        hubungiBtn = driver.find_element(By.XPATH,
                                         "//div[@class='detail-buttons-placeholder d-flex gap-2 justify-content-end mt-auto align-items-center']//button[@class='details-button-item btn-terima-modal'][normalize-space()='Terima']")

        # Scroll agar terlihat di layar
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hubungiBtn)
        time.sleep(2)
        hubungiBtn.click()

        # tunggu sampai pop up confirmation muncul
        wait = WebDriverWait(driver, 5)
        time.sleep(3)

        # cari button Ya, Saya Yakin
        sureBtn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='confirm-accept-job']")))
        sureBtn.click()
        time.sleep(5)

        driver.find_element(By.LINK_TEXT, "Beranda").click()
        time.sleep(2)

        # Tunggu hingga elemen muncul dan bisa diklik
        element_card = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'beranda-req-kiri')]//div[1]")))
        element_card.click()
        time.sleep(2)

        print("Menyimpan cookies...")
        pickle.dump(driver.get_cookies(), open(cookies_file, "wb"))

        # Tunggu tombol muncul
        start_button = wait.until(EC.element_to_be_clickable((By.ID, "start-work-button")))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        start_button.click()
        time.sleep(2)

        time.sleep(15)
        driver.quit()

    def TC002(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/accepted-work-request/47")

        driver.find_element(By.XPATH, "//input[@placeholder='Tulis pesan...']").send_keys('Halo bang')
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[@class='btn rounded-5 d-flex align-items-center justify-content-center']").click()

        time.sleep(15)
        driver.quit()

    def TC003(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/accepted-work-request/35")

        # Tunggu dan scroll ke tombol "Batalkan Kerja"
        start_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Batalkan Kerja']")))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", start_button)
        time.sleep(1)  # tunggu agar scroll selesai

        # Klik pakai JavaScript agar tidak terblok oleh elemen lain
        driver.execute_script("arguments[0].click();", start_button)
        time.sleep(2)

        # Tunggu dan klik tombol "Ya, Tetap Batalin"
        lanjut_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Ya, Tetap Batalin']")))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", lanjut_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", lanjut_button)

        time.sleep(15)
        driver.quit()



    def TC004(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/accepted-work-request/29")

        # # Tunggu dan scroll ke tombol "Batalkan Kerja"
        start_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Batalkan Kerja']")))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", start_button)
        time.sleep(1)  # tunggu agar scroll selesai

        # Klik pakai JavaScript agar tidak terblok oleh elemen lain
        driver.execute_script("arguments[0].click();", start_button)
        time.sleep(2)

        # Tunggu dan klik tombol "Lanjut Kerja"
        lanjut_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Lanjut Kerja']")))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", lanjut_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", lanjut_button)
        #
        time.sleep(15)
        driver.quit()

    def TC005(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/accepted-work-request/34")

        # Klik tombol "Selesai Kerja"
        try:
            selesai_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Selesai Kerja']")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", selesai_button)
            time.sleep(1)
            selesai_button.click()
        except Exception as e:
            print("Gagal menemukan tombol 'Selesai Kerja':", e)
            driver.quit()
            return

        # Upload foto
        try:
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "photoInputReport")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_input)
            upload_input.send_keys("D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/baby_90.png")
            time.sleep(2)
        except Exception as e:
            print("Gagal upload foto:", e)

        # Isi catatan
        driver.find_element(By.ID, "note").send_keys("Sudah baik")
        time.sleep(2)

        # Klik tombol "Selesai Pekerjaan"
        driver.find_element(By.XPATH, "//button[normalize-space()='Selesai Pekerjaan']").click()
        time.sleep(2)

        # Klik bintang rating 5
        try:
            bintang_5 = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//i[contains(@class, 'star-rating') and @data-value='5']"
            )))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", bintang_5)
            time.sleep(1)
            bintang_5.click()
            time.sleep(1)
        except Exception as e:
            print("Gagal klik bintang rating:", e)
            driver.quit()
            return

        # Isi komentar dan kirim
        driver.find_element(By.ID, "comment").send_keys("Sudah baik")
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[normalize-space()='Kirim']").click()

        time.sleep(5)
        driver.quit()

    def TC006(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/accepted-work-request/29")

        start_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Selesai Kerja']")))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", start_button)
        time.sleep(1)  # tunggu agar scroll selesai
        start_button.click()

        start_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Selesai Pekerjaan']")))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", start_button)
        time.sleep(1)  # tunggu agar scroll selesai
        start_button.click()

        time.sleep(15)
        driver.quit()

    def TC007(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/accepted-work-request/29")

        # Klik tombol "Selesai Kerja"
        try:
            selesai_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Selesai Kerja']")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", selesai_button)
            time.sleep(1)
            selesai_button.click()
        except Exception as e:
            print("Gagal menemukan tombol 'Selesai Kerja':", e)
            driver.quit()
            return

        # Upload foto
        try:
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "photoInputReport")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_input)
            upload_input.send_keys("D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/baby_90.png")
            time.sleep(2)
        except Exception as e:
            print("Gagal upload foto:", e)

        # Isi catatan
        # driver.find_element(By.ID, "note").send_keys("Sudah baik")
        # time.sleep(2)

        # Klik tombol "Selesai Pekerjaan"
        driver.find_element(By.XPATH, "//button[normalize-space()='Selesai Pekerjaan']").click()
        time.sleep(2)

        # Klik bintang rating 5
        # try:
        #     bintang_5 = wait.until(EC.element_to_be_clickable((
        #         By.XPATH, "//i[contains(@class, 'star-rating') and @data-value='5']"
        #     )))
        #     driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", bintang_5)
        #     time.sleep(1)
        #     bintang_5.click()
        #     time.sleep(1)
        # except Exception as e:
        #     print("Gagal klik bintang rating:", e)
        #     driver.quit()
        #     return

        # Isi komentar dan kirim
        # driver.find_element(By.ID, "comment").send_keys("Sudah baik")
        # time.sleep(1)

        driver.find_element(By.XPATH, "//button[normalize-space()='Kirim']").click()

        time.sleep(5)
        driver.quit()

    def TC008(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/accepted-work-request/30")

        # Klik tombol "Selesai Kerja"
        try:
            selesai_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Selesai Kerja']")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", selesai_button)
            time.sleep(1)
            selesai_button.click()
        except Exception as e:
            print("Gagal menemukan tombol 'Selesai Kerja':", e)
            driver.quit()
            return

        # Upload foto
        try:
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "photoInputReport")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_input)
            upload_input.send_keys("D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/baby_90.png")
            time.sleep(2)
        except Exception as e:
            print("Gagal upload foto:", e)

        # Isi catatan
        driver.find_element(By.ID, "note").send_keys("Sudah baik")
        time.sleep(2)

        # Klik tombol "Selesai Pekerjaan"
        driver.find_element(By.XPATH, "//button[normalize-space()='Selesai Pekerjaan']").click()
        time.sleep(2)

        # Klik bintang rating 5
        try:
            bintang_5 = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//i[contains(@class, 'star-rating') and @data-value='5']"
            )))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", bintang_5)
            time.sleep(1)
            bintang_5.click()
            time.sleep(1)
        except Exception as e:
            print("Gagal klik bintang rating:", e)
            driver.quit()
            return

        # Isi komentar dan kirim
        # driver.find_element(By.ID, "comment").send_keys("Sudah baik")
        # time.sleep(1)

        driver.find_element(By.XPATH, "//button[normalize-space()='Kirim']").click()

        time.sleep(5)
        driver.quit()

    def TC010(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/accepted-work-request/31")

        # Klik tombol "Selesai Kerja"
        try:
            selesai_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Selesai Kerja']")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", selesai_button)
            time.sleep(1)
            selesai_button.click()
        except Exception as e:
            print("Gagal menemukan tombol 'Selesai Kerja':", e)
            driver.quit()
            return

        # Upload foto
        try:
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "photoInputReport")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_input)
            upload_input.send_keys("D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/baby_90.png")
            time.sleep(2)
        except Exception as e:
            print("Gagal upload foto:", e)

        # Isi catatan
        driver.find_element(By.ID, "note").send_keys("Sudah baik")
        time.sleep(2)

        # Klik tombol "Selesai Pekerjaan"
        driver.find_element(By.XPATH, "//button[normalize-space()='Selesai Pekerjaan']").click()
        time.sleep(2)

        # Klik bintang rating 5
        try:
            bintang_5 = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//i[contains(@class, 'star-rating') and @data-value='1']"
            )))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", bintang_5)
            time.sleep(1)
            bintang_5.click()
            time.sleep(1)
        except Exception as e:
            print("Gagal klik bintang rating:", e)
            driver.quit()
            return

        # Isi komentar dan kirim
        driver.find_element(By.ID, "comment").send_keys("Sudah baik")
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[normalize-space()='Kirim']").click()

        time.sleep(5)
        driver.quit()

    def TC011(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/accepted-work-request/32")

        # Klik tombol "Selesai Kerja"
        try:
            selesai_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Selesai Kerja']")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", selesai_button)
            time.sleep(1)
            selesai_button.click()
        except Exception as e:
            print("Gagal menemukan tombol 'Selesai Kerja':", e)
            driver.quit()
            return

        # Upload foto
        try:
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "photoInputReport")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_input)
            upload_input.send_keys("D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/baby_90.png")
            time.sleep(2)
        except Exception as e:
            print("Gagal upload foto:", e)

        # Isi catatan
        driver.find_element(By.ID, "note").send_keys("Sudah baik")
        time.sleep(2)

        # Klik tombol "Selesai Pekerjaan"
        driver.find_element(By.XPATH, "//button[normalize-space()='Selesai Pekerjaan']").click()
        time.sleep(2)

        # Klik bintang rating 5
        try:
            bintang_5 = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//i[contains(@class, 'star-rating') and @data-value='2']"
            )))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", bintang_5)
            time.sleep(1)
            bintang_5.click()
            time.sleep(1)
        except Exception as e:
            print("Gagal klik bintang rating:", e)
            driver.quit()
            return

        # Isi komentar dan kirim
        driver.find_element(By.ID, "comment").send_keys("Sudah baik")
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[normalize-space()='Kirim']").click()

        time.sleep(5)
        driver.quit()

    def TC012(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/accepted-work-request/33")

        # Klik tombol "Selesai Kerja"
        try:
            selesai_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Selesai Kerja']")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", selesai_button)
            time.sleep(1)
            selesai_button.click()
        except Exception as e:
            print("Gagal menemukan tombol 'Selesai Kerja':", e)
            driver.quit()
            return

        # Upload foto
        try:
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "photoInputReport")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_input)
            upload_input.send_keys("D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/baby_90.png")
            time.sleep(2)
        except Exception as e:
            print("Gagal upload foto:", e)

        # Isi catatan
        driver.find_element(By.ID, "note").send_keys("Sudah baik")
        time.sleep(2)

        # Klik tombol "Selesai Pekerjaan"
        driver.find_element(By.XPATH, "//button[normalize-space()='Selesai Pekerjaan']").click()
        time.sleep(2)

        # Klik bintang rating 5
        try:
            bintang_5 = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//i[contains(@class, 'star-rating') and @data-value='3']"
            )))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", bintang_5)
            time.sleep(1)
            bintang_5.click()
            time.sleep(1)
        except Exception as e:
            print("Gagal klik bintang rating:", e)
            driver.quit()
            return

        # Isi komentar dan kirim
        driver.find_element(By.ID, "comment").send_keys("Sudah baik")
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[normalize-space()='Kirim']").click()

        time.sleep(5)
        driver.quit()

    def TC013(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/accepted-work-request/34")

        # Klik tombol "Selesai Kerja"
        try:
            selesai_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Selesai Kerja']")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", selesai_button)
            time.sleep(1)
            selesai_button.click()
        except Exception as e:
            print("Gagal menemukan tombol 'Selesai Kerja':", e)
            driver.quit()
            return

        # Upload foto
        try:
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "photoInputReport")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_input)
            upload_input.send_keys("D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/baby_90.png")
            time.sleep(2)
        except Exception as e:
            print("Gagal upload foto:", e)

        # Isi catatan
        driver.find_element(By.ID, "note").send_keys("Sudah baik")
        time.sleep(2)

        # Klik tombol "Selesai Pekerjaan"
        driver.find_element(By.XPATH, "//button[normalize-space()='Selesai Pekerjaan']").click()
        time.sleep(2)

        # Klik bintang rating 5
        try:
            bintang_5 = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//i[contains(@class, 'star-rating') and @data-value='4']"
            )))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", bintang_5)
            time.sleep(1)
            bintang_5.click()
            time.sleep(1)
        except Exception as e:
            print("Gagal klik bintang rating:", e)
            driver.quit()
            return

        # Isi komentar dan kirim
        driver.find_element(By.ID, "comment").send_keys("Sudah baik")
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[normalize-space()='Kirim']").click()

        time.sleep(5)
        driver.quit()

    def TC014(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/accepted-work-request/35")

        # Klik tombol "Selesai Kerja"
        try:
            selesai_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Selesai Kerja']")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", selesai_button)
            time.sleep(1)
            selesai_button.click()
        except Exception as e:
            print("Gagal menemukan tombol 'Selesai Kerja':", e)
            driver.quit()
            return

        # Upload foto
        try:
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "photoInputReport")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_input)
            upload_input.send_keys("D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/baby_90.png")
            time.sleep(2)
        except Exception as e:
            print("Gagal upload foto:", e)

        # Isi catatan
        driver.find_element(By.ID, "note").send_keys("Sudah baik")
        time.sleep(2)

        # Klik tombol "Selesai Pekerjaan"
        driver.find_element(By.XPATH, "//button[normalize-space()='Selesai Pekerjaan']").click()
        time.sleep(2)

        # Klik bintang rating 5
        try:
            bintang_5 = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//i[contains(@class, 'star-rating') and @data-value='5']"
            )))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", bintang_5)
            time.sleep(1)
            bintang_5.click()
            time.sleep(1)
        except Exception as e:
            print("Gagal klik bintang rating:", e)
            driver.quit()
            return

        # Isi komentar dan kirim
        driver.find_element(By.ID, "comment").send_keys("Sudah baik")
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[normalize-space()='Kirim']").click()

        time.sleep(5)
        driver.quit()

    def TC015(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/accepted-work-request/25")

        # Klik tombol "Selesai Kerja"
        try:
            selesai_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Selesai Kerja']")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", selesai_button)
            time.sleep(1)
            selesai_button.click()
        except Exception as e:
            print("Gagal menemukan tombol 'Selesai Kerja':", e)
            driver.quit()
            return

        # Upload foto
        try:
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "photoInputReport")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_input)
            upload_input.send_keys("D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/baby_90.png")
            time.sleep(2)
        except Exception as e:
            print("Gagal upload foto:", e)

        # Isi catatan
        driver.find_element(By.ID, "note").send_keys("Sudah baik")
        time.sleep(2)

        # Klik tombol "Selesai Pekerjaan"
        driver.find_element(By.XPATH, "//button[normalize-space()='Selesai Pekerjaan']").click()
        time.sleep(2)

        # # Klik bintang rating 5
        # try:
        #     bintang_5 = wait.until(EC.element_to_be_clickable((
        #         By.XPATH, "//i[contains(@class, 'star-rating') and @data-value='1']"
        #     )))
        #     driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", bintang_5)
        #     time.sleep(1)
        #     bintang_5.click()
        #     time.sleep(1)
        # except Exception as e:
        #     print("Gagal klik bintang rating:", e)
        #     driver.quit()
        #     return

        # Isi komentar dan kirim
        driver.find_element(By.ID, "comment").send_keys("Sudah baik")
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[normalize-space()='Kirim']").click()

        time.sleep(5)
        driver.quit()

    def TC016(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/accepted-work-request/27")

        # Klik tombol "Selesai Kerja"
        try:
            selesai_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Selesai Kerja']")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", selesai_button)
            time.sleep(1)
            selesai_button.click()
        except Exception as e:
            print("Gagal menemukan tombol 'Selesai Kerja':", e)
            driver.quit()
            return

        # Upload foto
        try:
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "photoInputReport")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_input)
            upload_input.send_keys("D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/baby_90.png")
            time.sleep(2)
        except Exception as e:
            print("Gagal upload foto:", e)

        # Isi catatan
        driver.find_element(By.ID, "note").send_keys("Sudah baik")
        time.sleep(2)

        # Klik tombol "Selesai Pekerjaan"
        driver.find_element(By.XPATH, "//button[normalize-space()='Selesai Pekerjaan']").click()
        time.sleep(2)

        # Klik bintang rating 5
        try:
            bintang_5 = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//button[@class='btn-close']"
            )))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", bintang_5)
            time.sleep(1)
            bintang_5.click()
            time.sleep(1)
        except Exception as e:
            print("Gagal klik close", e)
            driver.quit()
            return

        # # Isi komentar dan kirim
        # driver.find_element(By.ID, "comment").send_keys("Sudah baik")
        # time.sleep(1)

        time.sleep(5)
        driver.quit()

    def TC017(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/accepted-work-request/27")

        # Klik tombol "Selesai Kerja"
        try:
            selesai_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Selesai Kerja']")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", selesai_button)
            time.sleep(1)
            selesai_button.click()
        except Exception as e:
            print("Gagal menemukan tombol 'Selesai Kerja':", e)
            driver.quit()
            return

        # Upload foto
        try:
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "photoInputProof")))
            # Hilangkan class 'd-none' supaya bisa upload
            driver.execute_script("arguments[0].classList.remove('d-none');", upload_input)

            # Scroll ke elemen & isi file
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_input)
            upload_input.send_keys("D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/baby_90.png")

            print("✅ Foto berhasil diupload")
            time.sleep(2)
        except Exception as e:
            print("❌ Gagal upload foto:", e)

        # Isi catatan
        driver.find_element(By.ID, "note").send_keys("Sudah baik")
        time.sleep(2)

        # Klik tombol "Selesai Pekerjaan"
        driver.find_element(By.XPATH, "//button[normalize-space()='Selesaikan Pekerjaan']").click()
        time.sleep(2)

        # Klik laporkan masalah
        try:
            bintang_5 = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//button[normalize-space()='Laporkan masalah']"
            )))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", bintang_5)
            time.sleep(1)
            bintang_5.click()
            time.sleep(1)
        except Exception as e:
            print("Gagal klik close", e)
            driver.quit()
            return

        time.sleep(5)
        driver.quit()

    def TC018(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/accepted-work-request/26")

        # Klik tombol "Selesai Kerja"
        try:
            selesai_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Selesai Kerja']")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", selesai_button)
            time.sleep(1)
            selesai_button.click()
        except Exception as e:
            print("Gagal menemukan tombol 'Selesai Kerja':", e)
            driver.quit()
            return

        # Upload foto
        try:
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "photoInputProof")))
            # Hilangkan class 'd-none' supaya bisa upload
            driver.execute_script("arguments[0].classList.remove('d-none');", upload_input)

            # Scroll ke elemen & isi file
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_input)
            upload_input.send_keys("D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/baby_90.png")

            print("✅ Foto berhasil diupload")
            time.sleep(2)
        except Exception as e:
            print("❌ Gagal upload foto:", e)

        # Isi catatan
        driver.find_element(By.ID, "note").send_keys("Sudah baik")
        time.sleep(2)

        # Klik tombol "Selesai Pekerjaan"
        driver.find_element(By.XPATH, "//button[normalize-space()='Selesaikan Pekerjaan']").click()
        time.sleep(2)

        # Klik bintang rating 5
        try:
            lapor = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//button[normalize-space()='Laporkan masalah']"
            )))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", lapor)
            time.sleep(1)
            lapor.click()
            time.sleep(2)
        except Exception as e:
            print("Gagal klik Laporkan masalah", e)
            driver.quit()
            return

        try:
            # Tunggu elemen muncul
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "photoInputReport")))

            # Pastikan benar <input type="file">
            input_type = upload_input.get_attribute("type")
            if input_type != "file":
                print("❌ Elemen bukan input file. type =", input_type)
            else:
                # Hilangkan 'd-none' agar bisa diakses
                driver.execute_script("arguments[0].classList.remove('d-none');", upload_input)
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                      upload_input)

                # Upload file
                file_path = "D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/test.docx"
                upload_input.send_keys(file_path)
                print("✅ File berhasil diupload:", file_path)

            time.sleep(2)

        except Exception as e:
            print("❌ Gagal upload file:", e)

        driver.find_element(By.XPATH, "//button[@type='submit'][contains(text(),'Kirim')]").click()

        time.sleep(5)
        driver.quit()


    def TC019(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/accepted-work-request/27")

        # Klik tombol "Selesai Kerja"
        try:
            selesai_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Selesai Kerja']")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", selesai_button)
            time.sleep(1)
            selesai_button.click()
        except Exception as e:
            print("Gagal menemukan tombol 'Selesai Kerja':", e)
            driver.quit()
            return

        # Upload foto
        try:
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "photoInputProof")))
            # Hilangkan class 'd-none' supaya bisa upload
            driver.execute_script("arguments[0].classList.remove('d-none');", upload_input)

            # Scroll ke elemen & isi file
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_input)
            upload_input.send_keys("D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/baby_90.png")

            print("✅ Foto berhasil diupload")
            time.sleep(2)
        except Exception as e:
            print("❌ Gagal upload foto:", e)

        # Isi catatan
        driver.find_element(By.ID, "note").send_keys("Sudah baik")
        time.sleep(2)

        # Klik tombol "Selesai Pekerjaan"
        driver.find_element(By.XPATH, "//button[normalize-space()='Selesaikan Pekerjaan']").click()
        time.sleep(2)

        # Klik bintang rating 5
        try:
            lapor = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//button[normalize-space()='Laporkan masalah']"
            )))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", lapor)
            time.sleep(1)
            lapor.click()
            time.sleep(2)
        except Exception as e:
            print("Gagal klik Laporkan masalah", e)
            driver.quit()
            return

        try:
            # Tunggu elemen muncul
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "photoInputReport")))

            # Pastikan benar <input type="file">
            input_type = upload_input.get_attribute("type")
            if input_type != "file":
                print("❌ Elemen bukan input file. type =", input_type)
            else:
                # Hilangkan 'd-none' agar bisa diakses
                driver.execute_script("arguments[0].classList.remove('d-none');", upload_input)
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                      upload_input)

                # Upload file
                file_path = "D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/baby_90.png"
                upload_input.send_keys(file_path)
                print("✅ File berhasil diupload:", file_path)

            time.sleep(2)

        except Exception as e:
            print("❌ Gagal upload file:", e)

        driver.find_element(By.XPATH, "//button[@type='submit'][contains(text(),'Kirim')]").click()


        time.sleep(5)
        driver.quit()

    def TC020(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/accepted-work-request/27")

        # Klik tombol "Selesai Kerja"
        try:
            selesai_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Selesai Kerja']")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", selesai_button)
            time.sleep(1)
            selesai_button.click()
        except Exception as e:
            print("Gagal menemukan tombol 'Selesai Kerja':", e)
            driver.quit()
            return

        # Upload foto
        try:
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "photoInputProof")))
            # Hilangkan class 'd-none' supaya bisa upload
            driver.execute_script("arguments[0].classList.remove('d-none');", upload_input)

            # Scroll ke elemen & isi file
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_input)
            upload_input.send_keys("D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/baby_90.png")

            print("✅ Foto berhasil diupload")
            time.sleep(2)
        except Exception as e:
            print("❌ Gagal upload foto:", e)

        # Isi catatan
        driver.find_element(By.ID, "note").send_keys("Sudah baik")
        time.sleep(2)

        # Klik tombol "Selesai Pekerjaan"
        driver.find_element(By.XPATH, "//button[normalize-space()='Selesaikan Pekerjaan']").click()
        time.sleep(2)

        # Klik bintang rating 5
        try:
            lapor = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//button[normalize-space()='Laporkan masalah']"
            )))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", lapor)
            time.sleep(1)
            lapor.click()
            time.sleep(2)
        except Exception as e:
            print("Gagal klik Laporkan masalah", e)
            driver.quit()
            return

        try:
            # Tunggu elemen muncul
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "photoInputReport")))

            # Pastikan benar <input type="file">
            input_type = upload_input.get_attribute("type")
            if input_type != "file":
                print("❌ Elemen bukan input file. type =", input_type)
            else:
                # Hilangkan 'd-none' agar bisa diakses
                driver.execute_script("arguments[0].classList.remove('d-none');", upload_input)
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                      upload_input)

                # Upload file
                file_path = "D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/test.docx"
                upload_input.send_keys(file_path)
                print("✅ File berhasil diupload:", file_path)

            time.sleep(2)

        except Exception as e:
            print("❌ Gagal upload file:", e)

        driver.find_element(By.XPATH, "//textarea[@id='reportNote']").send_keys("Tidak baik bro")
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[@type='submit'][contains(text(),'Kirim')]").click()

        time.sleep(5)
        driver.quit()

    def TC021(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/accepted-work-request/28")

        # Klik tombol "Selesai Kerja"
        try:
            selesai_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Selesai Kerja']")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", selesai_button)
            time.sleep(1)
            selesai_button.click()
        except Exception as e:
            print("Gagal menemukan tombol 'Selesai Kerja':", e)
            driver.quit()
            return

        # Upload foto
        try:
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "photoInputProof")))
            # Hilangkan class 'd-none' supaya bisa upload
            driver.execute_script("arguments[0].classList.remove('d-none');", upload_input)

            # Scroll ke elemen & isi file
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_input)
            upload_input.send_keys("D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/baby_90.png")

            print("✅ Foto berhasil diupload")
            time.sleep(2)
        except Exception as e:
            print("❌ Gagal upload foto:", e)

        # Isi catatan
        driver.find_element(By.ID, "note").send_keys("Sudah baik")
        time.sleep(2)

        # Klik tombol "Selesai Pekerjaan"
        driver.find_element(By.XPATH, "//button[normalize-space()='Selesaikan Pekerjaan']").click()
        time.sleep(2)

        # Klik bintang rating 5
        try:
            lapor = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//button[normalize-space()='Laporkan masalah']"
            )))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", lapor)
            time.sleep(1)
            lapor.click()
            time.sleep(2)
        except Exception as e:
            print("Gagal klik Laporkan masalah", e)
            driver.quit()
            return

        try:
            # Tunggu elemen muncul
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "photoInputReport")))

            # Pastikan benar <input type="file">
            input_type = upload_input.get_attribute("type")
            if input_type != "file":
                print("❌ Elemen bukan input file. type =", input_type)
            else:
                # Hilangkan 'd-none' agar bisa diakses
                driver.execute_script("arguments[0].classList.remove('d-none');", upload_input)
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                      upload_input)

                # Upload file
                file_path = "D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/baby_90.png"
                upload_input.send_keys(file_path)
                print("✅ File berhasil diupload:", file_path)

            time.sleep(2)

        except Exception as e:
            print("❌ Gagal upload file:", e)

        driver.find_element(By.XPATH, "//textarea[@id='reportNote']").send_keys("Tidak baik bro")
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[@type='submit'][contains(text(),'Kirim')]").click()

        time.sleep(5)
        driver.quit()

    def TC022(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        cookies_file = "../cookiesJobtaker.pkl"
        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("http://127.0.0.1:8000/job-taker/accepted-work-request/40")

        # Klik tombol "Selesai Kerja"
        try:
            selesai_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Selesai Kerja']")))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", selesai_button)
            time.sleep(1)
            selesai_button.click()
        except Exception as e:
            print("Gagal menemukan tombol 'Selesai Kerja':", e)
            driver.quit()
            return

        # Upload foto
        try:
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "photoInputProof")))
            # Hilangkan class 'd-none' supaya bisa upload
            driver.execute_script("arguments[0].classList.remove('d-none');", upload_input)

            # Scroll ke elemen & isi file
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_input)
            upload_input.send_keys("D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/baby_90.png")

            print("✅ Foto berhasil diupload")
            time.sleep(2)
        except Exception as e:
            print("❌ Gagal upload foto:", e)

        # Isi catatan
        driver.find_element(By.ID, "note").send_keys("Sudah baik")
        time.sleep(2)

        # Klik tombol "Selesai Pekerjaan"
        driver.find_element(By.XPATH, "//button[normalize-space()='Selesaikan Pekerjaan']").click()
        time.sleep(2)

        # Klik bintang rating 5
        try:
            lapor = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//button[normalize-space()='Laporkan masalah']"
            )))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", lapor)
            time.sleep(1)
            lapor.click()
            time.sleep(5)
        except Exception as e:
            print("Gagal klik Laporkan masalah", e)
            driver.quit()
            return

        driver.find_element(By.XPATH, "//textarea[@id='reportNote']").send_keys("Tidak baik bro")
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[@type='submit'][contains(text(),'Kirim')]").click()

        time.sleep(5)
        driver.quit()


# Cookies save
# save = startWorkFunctionality()
# save.cookies_save()

# Testing TC001
# tc001 = startWorkFunctionality()
# tc001.TC001()

# Testing TC002
# tc002 = startWorkFunctionality()
# tc002.TC002()

# Testing TC003
# tc003 = startWorkFunctionality()
# tc003.TC003()

# Testing TC004
# tc004 = startWorkFunctionality()
# tc004.TC004()

# Testing TC005
# tc005 = startWorkFunctionality()
# tc005.TC005()

# Testing TC006
# tc006 = startWorkFunctionality()
# tc006.TC006()

# Testing TC007
# tc007 = startWorkFunctionality()
# tc007.TC007()

# Testing TC008
# tc008 = startWorkFunctionality()
# tc008.TC008()

# Testing TC010
# tc010 = startWorkFunctionality()
# tc010.TC010()

# # Testing TC011
# tc011 = startWorkFunctionality()
# tc011.TC011()

# Testing TC012
# tc012 = startWorkFunctionality()
# tc012.TC012()

# Testing TC013
# tc013 = startWorkFunctionality()
# tc013.TC013()

# Testing TC014
# tc014 = startWorkFunctionality()
# tc014.TC014()

# # Testing TC015
# tc015 = startWorkFunctionality()
# tc015.TC015()

# Testing TC016
# tc016 = startWorkFunctionality()
# tc016.TC016()

# Testing TC017
# tc017 = startWorkFunctionality()
# tc017.TC017()

# Testing TC018
# tc018 = startWorkFunctionality()
# tc018.TC018()

# Testing TC019
# tc019 = startWorkFunctionality()
# tc019.TC019()

# Testing TC020
# tc020 = startWorkFunctionality()
# tc020.TC020()

# Testing TC021
# tc021 = startWorkFunctionality()
# tc021.TC021()

# Testing TC022
tc022 = startWorkFunctionality()
tc022.TC022()