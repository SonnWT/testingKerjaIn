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


class chatFunctionality():
    def cookies_save(self):
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
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Cari Kerja"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='job-card p-4']//button[contains(@class, 'detail-button')]")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(5)

        # Klik tombol "Hubungi"
        hubungiBtn = wait.until(EC.element_to_be_clickable((By.ID, "button-hubungi")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hubungiBtn)
        time.sleep(2)
        hubungiBtn.click()
        time.sleep(15)


        print("Menyimpan cookies...")
        pickle.dump(driver.get_cookies(), open(cookies_file, "wb"))

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
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Cari Kerja"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='job-card p-4']//button[contains(@class, 'detail-button')]")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(5)

        # Klik tombol "Hubungi"
        hubungiBtn = wait.until(EC.element_to_be_clickable((By.ID, "button-hubungi")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hubungiBtn)
        time.sleep(2)
        hubungiBtn.click()

        # Input pesan di kolom chat
        inputBox = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Tulis pesan...']")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", inputBox)
        time.sleep(1)
        inputBox.send_keys("halo")
        time.sleep(2)

        # Klik tombol kirim chat
        kirimBtn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@class='btn btn-send-circle ms-2 rounded-circle']")
        ))
        kirimBtn.click()

        time.sleep(15)
        driver.quit()

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
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Cari Kerja"))).click()
        time.sleep(2)

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='job-card p-4']//button[contains(@class, 'detail-button')]")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(5)

        # Klik tombol "Hubungi"
        hubungiBtn = wait.until(EC.element_to_be_clickable((By.ID, "button-hubungi")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hubungiBtn)
        time.sleep(2)
        hubungiBtn.click()

        # Input pesan di kolom chat
        inputBox = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Tulis pesan...']")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", inputBox)
        time.sleep(1)
        inputBox.send_keys("halo")
        time.sleep(2)

        # Klik tombol kirim chat
        kirimBtn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@class='btn btn-send-circle ms-2 rounded-circle']")
        ))
        kirimBtn.click()

        time.sleep(15)
        driver.quit()

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
        driver.get("http://127.0.0.1:8000/job-taker/pesan/46")

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Tawar Upah']")
        ))
        element.click()

        time.sleep(15)
        driver.quit()

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
        driver.get("http://127.0.0.1:8000/job-taker/pesan/46")

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Tawar Upah']")
        ))
        element.click()
        time.sleep(2)

        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Batal']")
        ))
        element.click()


        time.sleep(15)
        driver.quit()

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
        driver.get("http://127.0.0.1:8000/job-taker/pesan/46")

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Tawar Upah']")
        ))
        element.click()
        time.sleep(2)

        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Kirim')]")
        ))
        element.click()


        time.sleep(15)
        driver.quit()

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
        driver.get("http://127.0.0.1:8000/job-taker/pesan/46")

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Tawar Upah']")
        ))
        element.click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@placeholder='Masukkan nominal...']").send_keys("test")
        time.sleep(2)

        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Kirim')]")
        ))
        element.click()

        time.sleep(15)
        driver.quit()

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
        driver.get("http://127.0.0.1:8000/job-taker/pesan/46")

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Tawar Upah']")
        ))
        element.click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@placeholder='Masukkan nominal...']").send_keys("150000")
        time.sleep(2)

        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Kirim')]")
        ))
        element.click()

        time.sleep(15)
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
        driver.get("http://127.0.0.1:8000/job-taker/pesan/46")

        # Klik tombol DETAIL pertama yang muncul pada card pekerjaan
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Tawar Upah']")
        ))
        element.click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@placeholder='Masukkan nominal...']").send_keys("150000")
        time.sleep(2)

        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Kirim')]")
        ))
        element.click()

        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Batal Ajukan']")
        ))
        element.click()

        time.sleep(15)
        driver.quit()


# Cookies_save
# csave = chatFunctionality()
# csave.cookies_save()

# Testing TC001
# tc001 = chatFunctionality()
# tc001.TC001()

# Testing TC004
# tc004 = chatFunctionality()
# tc004.TC004()

# Testing TC006
# tc006 = chatFunctionality()
# tc006.TC006()

# Testing TC007
# tc007 = chatFunctionality()
# tc007.TC007()

# Testing TC008
# tc008 = chatFunctionality()
# tc008.TC008()

# Testing TC009
# tc009 = chatFunctionality()
# tc009.TC009()

# Testing TC010
# tc010 = chatFunctionality()
# tc010.TC010()

# Testing TC011
tc011 = chatFunctionality()
tc011.TC011()





