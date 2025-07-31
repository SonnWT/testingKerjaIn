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


class searchFunctionality():
    def TC001(self):
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

        # Click tombol Cari Kerja
        driver.find_element(By.LINK_TEXT, "Cari Kerja").click()
        time.sleep(2)

        # memberikan input sesuai title job yang ada pada saat testing dilaksankan
        driver.find_element(By.XPATH, "//input[@id='input-area']").send_keys("Laborum nemo dolores ut vitae earum.")
        time.sleep(2)

        # Klik tombol CARI
        driver.find_element(By.XPATH, "//button[normalize-space()='CARI']").click()

        time.sleep(15)
        driver.quit()

    def TC002(self):
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

        # Click tombol Cari Kerja
        driver.find_element(By.LINK_TEXT, "Cari Kerja").click()
        time.sleep(2)

        # Klik tombol CARI
        driver.find_element(By.XPATH, "//button[normalize-space()='CARI']").click()

        time.sleep(15)
        driver.quit()

    def TC003(self):
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

        # Click tombol Cari Kerja
        driver.find_element(By.LINK_TEXT, "Cari Kerja").click()
        time.sleep(2)

        # memberikan input zzzz untuk memastikan
        driver.find_element(By.XPATH, "//input[@id='input-area']").send_keys("zzzzz")
        time.sleep(2)

        # klik tombol CARI
        driver.find_element(By.XPATH, "//button[normalize-space()='CARI']").click()

        time.sleep(15)
        driver.quit()

    def TC004(self):
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

        # Click tombol Cari Kerja
        driver.find_element(By.LINK_TEXT, "Cari Kerja").click()
        time.sleep(2)

        # klik tombol CARI
        driver.find_element(By.XPATH, "//button[normalize-space()='CARI']").click()

        time.sleep(15)
        driver.quit()


    def TC007(self):
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

        # Click tombol Cari Kerja
        driver.find_element(By.LINK_TEXT, "Cari Kerja").click()
        time.sleep(2)

        # Click detail button in the first job that appear
        element = driver.find_element(By.XPATH, "//div[9]//ul[1]//button[1]")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)  # opsional: beri jeda
        element.click()

        time.sleep(15)
        driver.quit()

    def TC008(self):
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

        # Click tombol Cari Kerja
        driver.find_element(By.LINK_TEXT, "Cari Kerja").click()
        time.sleep(15)
        driver.quit()

    def TC009(self):
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

        # Click tombol Cari Kerja
        driver.find_element(By.LINK_TEXT, "Cari Kerja").click()

        time.sleep(15)
        driver.quit()

    def TC010(self):
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


        # Click tombol Cari Kerja
        driver.find_element(By.LINK_TEXT, "Cari Kerja").click()
        time.sleep(2)

        # Click detail button in the first job that appear
        element = driver.find_element(By.XPATH, "//div[9]//ul[1]//button[1]")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)  # opsional: beri jeda
        element.click()

        # Temukan elemen terlebih dahulu
        hubungiBtn = driver.find_element(By.XPATH, "//a[@id='button-hubungi']")

        # Scroll agar terlihat di layar
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hubungiBtn)
        time.sleep(1)  # beri waktu render, jika perlu

        # Klik elemen
        hubungiBtn.click()

        time.sleep(15)
        driver.quit()

    def TC011(self):
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

        # Click tombol Cari Kerja
        driver.find_element(By.LINK_TEXT, "Cari Kerja").click()
        time.sleep(2)

        # Click detail button in the first job that appear
        element = driver.find_element(By.XPATH, "//div[9]//ul[1]//button[1]")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)  # opsional: beri jeda
        element.click()

        # Temukan elemen terlebih dahulu
        hubungiBtn = driver.find_element(By.XPATH, "//button[@id='submit-offer-button']")

        # Scroll agar terlihat di layar
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hubungiBtn)
        time.sleep(1)  # beri waktu render, jika perlu
        driver.find_element(By.XPATH, "//input[@id='offer-amount-input']").send_keys(15000)
        time.sleep(2)
        hubungiBtn.click()

        time.sleep(15)
        driver.quit()

    def TC012(self):
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

        # Click tombol Cari Kerja
        driver.find_element(By.LINK_TEXT, "Cari Kerja").click()
        time.sleep(2)

        # Click detail button in the first job that appear
        element = driver.find_element(By.XPATH, "//div[9]//ul[1]//button[1]")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)  # opsional: beri jeda
        element.click()

        # Temukan elemen terlebih dahulu
        hubungiBtn = driver.find_element(By.XPATH, "//button[@id='submit-offer-button']")

        # Scroll agar terlihat di layar
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hubungiBtn)
        time.sleep(2)
        hubungiBtn.click()

        time.sleep(15)
        driver.quit()

    def TC013(self):
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

        # Click tombol Cari Kerja
        driver.find_element(By.LINK_TEXT, "Cari Kerja").click()
        time.sleep(2)

        # Click detail button in the first job that appear
        element = driver.find_element(By.XPATH, "//div[9]//ul[1]//button[1]")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)  # opsional: beri jeda
        element.click()

        # Temukan elemen terlebih dahulu
        hubungiBtn = driver.find_element(By.XPATH, "//div[@class='detail-buttons-placeholder d-flex gap-2 justify-content-end mt-auto align-items-center']//button[@class='details-button-item btn-terima-modal'][normalize-space()='Terima']")

        # Scroll agar terlihat di layar
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hubungiBtn)
        time.sleep(2)
        hubungiBtn.click()

        # tunggu sampai pop up confirmation muncul
        wait = WebDriverWait(driver, 5)

        # cari button Ya, Saya Yakin
        sureBtn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='confirm-accept-job']")))
        sureBtn.click()
        time.sleep(15)

        driver.find_element(By.LINK_TEXT, "Cari Kerja").click()

        time.sleep(15)
        driver.quit()

    def TC014(self):
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

        # Click tombol Cari Kerja
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
        sureBtn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='cancel-accept-job']")))
        sureBtn.click()

        time.sleep(15)
        driver.quit()


# Testing TC001
# tc001 = searchFunctionality()
# tc001.TC001()

# Testing TC002
# tc002 = searchFunctionality()
# tc002.TC002()

# Testing TC003
# tc003 = searchFunctionality()
# tc003.TC003()

# Testing TC004
# tc004 = searchFunctionality()
# tc004.TC004()

# Testing TC005 manual karena menghitung ada berapa job yang ditampilkan

# Testing TC006
# tc006 = searchFunctionality()
# tc006.TC006()

# Testing TC007
# tc007 = searchFunctionality()
# tc007.TC007()

# Testing TC008
# tc008 = searchFunctionality()
# tc008.TC008()

# Testing TC009
# tc009 = searchFunctionality()
# tc009.TC009()

# Testing TC010
# tc010 = searchFunctionality()
# tc010.TC010()

# Testing TC011
# tc011 = searchFunctionality()
# tc011.TC011()

# Testing TC012
# tc012 = searchFunctionality()
# tc012.TC012()

# Testing TC013
# tc013 = searchFunctionality()
# tc013.TC013()

# Testing TC014
tc014 = searchFunctionality()
tc014.TC014()



