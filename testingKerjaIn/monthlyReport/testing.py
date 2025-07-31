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


class monthlyReportFunctionality():
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
            (By.XPATH, "//a[normalize-space()='Laporan Bulanan']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        time.sleep(15)

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
            (By.XPATH, "//a[normalize-space()='Laporan Bulanan']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(3)
        element.click()

        # Scroll dan klik tombol "Mulai Kerja"
        start_button = driver.find_element(By.XPATH, "//button[normalize-space()='Download']")
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", start_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", start_button)
        time.sleep(15)


# Testing TC001
# tc001 = monthlyReportFunctionality()
# tc001.TC001()

# Testing TC002
tc002 = monthlyReportFunctionality()
tc002.TC002()