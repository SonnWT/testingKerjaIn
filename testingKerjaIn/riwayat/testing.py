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


class riwayatFunctionality():
    def TC001(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        cookies_file = "../cookiesJobtaker.pkl"

        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Reload halaman agar cookies aktif
        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        # Klik tombol "Cari Kerja"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Riwayat"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Diterima']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(5)

    def TC002(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        cookies_file = "../cookiesJobtaker.pkl"

        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Reload halaman agar cookies aktif
        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        # Klik tombol "Cari Kerja"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Riwayat"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Dibatalin']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(5)

    def TC003(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        cookies_file = "../cookiesJobtaker.pkl"

        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Reload halaman agar cookies aktif
        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        # Klik tombol "Cari Kerja"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Riwayat"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Dikerjain']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(5)

    def TC004(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        cookies_file = "../cookiesJobtaker.pkl"

        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Reload halaman agar cookies aktif
        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        # Klik tombol "Cari Kerja"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Riwayat"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Ditinjau']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(5)

    def TC005(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        cookies_file = "../cookiesJobtaker.pkl"

        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Reload halaman agar cookies aktif
        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        # Klik tombol "Cari Kerja"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Riwayat"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Selesai']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(5)

    def TC006(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        cookies_file = "../cookiesJobtaker.pkl"

        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Reload halaman agar cookies aktif
        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        # Klik tombol "Cari Kerja"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Riwayat"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[normalize-space()='Berlangsung (4)']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(15)

    def TC007(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        cookies_file = "../cookiesJobtaker.pkl"

        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Reload halaman agar cookies aktif
        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        # Klik tombol "Cari Kerja"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Riwayat"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[normalize-space()='Selesai (2)']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(15)

    def TC008(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        cookies_file = "../cookiesJobtaker.pkl"

        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Reload halaman agar cookies aktif
        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        # Klik tombol "Cari Kerja"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Riwayat"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[normalize-space()='Dibatalin (1)']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(15)

    def TC009(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        cookies_file = "../cookiesJobtaker.pkl"

        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Reload halaman agar cookies aktif
        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        # Klik tombol "Cari Kerja"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Riwayat"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Selesai']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(2)

        btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ms-2 fw-medium']")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        btn.click()

        time.sleep(30)

    def TC010(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        cookies_file = "../cookiesJobtaker.pkl"

        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Reload halaman agar cookies aktif
        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        # Klik tombol "Cari Kerja"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Riwayat"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Selesai']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(2)

        # # Klik bintang rating 5
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
        driver.find_element(By.ID, "comment").send_keys("All is good")
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[normalize-space()='Kirim']").click()

        time.sleep(5)
        driver.quit()

    def TC011(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        cookies_file = "../cookiesJobtaker.pkl"

        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Reload halaman agar cookies aktif
        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        # Klik tombol "Cari Kerja"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Riwayat"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Selesai']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(2)

        # # Klik bintang rating 5
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

        # # Isi komentar dan kirim
        # driver.find_element(By.ID, "comment").send_keys("All is good")
        # time.sleep(1)

        driver.find_element(By.XPATH, "//button[normalize-space()='Kirim']").click()

        time.sleep(5)
        driver.quit()

    def TC012(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        cookies_file = "../cookiesJobtaker.pkl"

        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Reload halaman agar cookies aktif
        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        # Klik tombol "Cari Kerja"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Riwayat"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Selesai']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(2)

        # # Klik bintang rating 5
        # try:
        #     bintang_5 = wait.until(EC.element_to_be_clickable((
        #         By.XPATH, "//i[contains(@class, 'star-rating') and @data-value='4']"
        #     )))
        #     driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", bintang_5)
        #     time.sleep(1)
        #     bintang_5.click()
        #     time.sleep(1)
        # except Exception as e:
        #     print("Gagal klik bintang rating:", e)
        #     driver.quit()
        #     return

        # # Isi komentar dan kirim
        comment = wait.until(EC.element_to_be_clickable((
            By.ID, "comment"
        )))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", comment)
        time.sleep(1)
        comment.send_keys("All is good")
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[normalize-space()='Kirim']").click()

        time.sleep(5)
        driver.quit()

    def TC013(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        cookies_file = "../cookiesJobtaker.pkl"

        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Reload halaman agar cookies aktif
        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        # Klik tombol "Cari Kerja"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Riwayat"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Selesai']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(2)

        # # Klik bintang rating 5
        # try:
        #     bintang_5 = wait.until(EC.element_to_be_clickable((
        #         By.XPATH, "//i[contains(@class, 'star-rating') and @data-value='4']"
        #     )))
        #     driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", bintang_5)
        #     time.sleep(1)
        #     bintang_5.click()
        #     time.sleep(1)
        # except Exception as e:
        #     print("Gagal klik bintang rating:", e)
        #     driver.quit()
        #     return

        # # Isi komentar dan kirim
        # comment = wait.until(EC.element_to_be_clickable((
        #     By.ID, "comment"
        # )))
        # driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", comment)
        # time.sleep(1)
        # comment.send_keys("All is good")
        # time.sleep(1)

        driver.find_element(By.XPATH, "//button[normalize-space()='Kirim']").click()

        time.sleep(5)
        driver.quit()

    def TC014(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        cookies_file = "../cookiesJobtaker.pkl"

        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Reload halaman agar cookies aktif
        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        # Klik tombol "Cari Kerja"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Riwayat"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Selesai']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(2)

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

    def TC015(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        cookies_file = "../cookiesJobtaker.pkl"

        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Reload halaman agar cookies aktif
        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        # Klik tombol "Cari Kerja"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Riwayat"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Selesai']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(2)

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

        try:
            # Tunggu elemen muncul
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "reportImageInput")))

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

        driver.find_element(By.XPATH, "//button[@id='submitReportButton']").click()

        time.sleep(5)
        driver.quit()

    def TC016(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        cookies_file = "../cookiesJobtaker.pkl"

        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Reload halaman agar cookies aktif
        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        # Klik tombol "Cari Kerja"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Riwayat"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Selesai']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(2)

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

        try:
            # Tunggu elemen muncul
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "reportImageInput")))

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

        driver.find_element(By.XPATH, "//button[@id='submitReportButton']").click()

        time.sleep(5)
        driver.quit()

    def TC017(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        cookies_file = "../cookiesJobtaker.pkl"

        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Reload halaman agar cookies aktif
        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        # Klik tombol "Cari Kerja"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Riwayat"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Selesai']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(2)

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

        try:
            # Tunggu elemen muncul
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "reportImageInput")))

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

        driver.find_element(By.XPATH, "//button[@id='submitReportButton']").click()

        time.sleep(5)
        driver.quit()

    def TC018(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        cookies_file = "../cookiesJobtaker.pkl"

        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Reload halaman agar cookies aktif
        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        # Klik tombol "Cari Kerja"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Riwayat"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Selesai']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(2)

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

        try:
            # Tunggu elemen muncul
            upload_input = wait.until(EC.presence_of_element_located((By.ID, "reportImageInput")))

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

        driver.find_element(By.XPATH, "//button[@id='submitReportButton']").click()

        time.sleep(5)
        driver.quit()

    def TC019(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        cookies_file = "../cookiesJobtaker.pkl"

        print("Memuat cookies...")
        cookies = pickle.load(open(cookies_file, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Reload halaman agar cookies aktif
        driver.get("http://127.0.0.1:8000/job-taker/beranda")

        # Klik tombol "Cari Kerja"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Riwayat"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Selesai']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(2)

        try:
            bintang_5 = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//button[normalize-space()='Laporkan masalah']"
            )))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", bintang_5)
            time.sleep(1)
            bintang_5.click()
            time.sleep(5)
        except Exception as e:
            print("Gagal klik close", e)
            driver.quit()
            return

        # try:
        #     # Tunggu elemen muncul
        #     upload_input = wait.until(EC.presence_of_element_located((By.ID, "reportImageInput")))
        #
        #     # Pastikan benar <input type="file">
        #     input_type = upload_input.get_attribute("type")
        #     if input_type != "file":
        #         print("❌ Elemen bukan input file. type =", input_type)
        #     else:
        #         # Hilangkan 'd-none' agar bisa diakses
        #         driver.execute_script("arguments[0].classList.remove('d-none');", upload_input)
        #         driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        #                               upload_input)
        #
        #         # Upload file
        #         file_path = "D:/DATA D/CAWU 5/Web Programming/testingKerjaIn/baby_90.png"
        #         upload_input.send_keys(file_path)
        #         print("✅ File berhasil diupload:", file_path)
        #
        #     time.sleep(2)
        #
        # except Exception as e:
        #     print("❌ Gagal upload file:", e)

        driver.find_element(By.XPATH, "//textarea[@id='reportNote']").send_keys("Tidak baik bro")
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[@id='submitReportButton']").click()

        time.sleep(5)
        driver.quit()


# Testing TC001
# tc001 = riwayatFunctionality()
# tc001.TC001()

# # Testing TC002
# tc002 = riwayatFunctionality()
# tc002.TC002()

# Testing TC003
# tc003 = riwayatFunctionality()
# tc003.TC003()

# Testing TC004
# tc004 = riwayatFunctionality()
# tc004.TC004()

# Testing TC005
# tc005 = riwayatFunctionality()
# tc005.TC005()

# Testing TC006
# tc006 = riwayatFunctionality()
# tc006.TC006()

# Testing TC007
# tc007 = riwayatFunctionality()
# tc007.TC007()

# Testing TC008
# tc008 = riwayatFunctionality()
# tc008.TC008()

# Testing TC009
# tc009 = riwayatFunctionality()
# tc009.TC009()

# Testing TC010
# tc0010 = riwayatFunctionality()
# tc0010.TC010()

# Testing TC011
# tc0011 = riwayatFunctionality()
# tc0011.TC011()

# Testing TC012
# tc0012 = riwayatFunctionality()
# tc0012.TC012()

# Testing TC013
# tc0013 = riwayatFunctionality()
# tc0013.TC013()

# Testing TC014
# tc0014 = riwayatFunctionality()
# tc0014.TC014()

# # Testing TC015
# tc0015 = riwayatFunctionality()
# tc0015.TC015()

# Testing TC016
# tc0016 = riwayatFunctionality()
# tc0016.TC016()

# Testing TC017
# tc0017 = riwayatFunctionality()
# tc0017.TC017()

# Testing TC018
# tc0018 = riwayatFunctionality()
# tc0018.TC018()

# Testing TC019
tc0019 = riwayatFunctionality()
tc0019.TC019()