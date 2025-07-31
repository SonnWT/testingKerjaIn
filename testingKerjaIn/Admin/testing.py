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


class adminFunctionality():
    def TC001(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)

        # 1. Klik dropdown profil
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        # 2. Klik "Ganti Peran"
        ganti_peran = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()

        time.sleep(5)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()


        time.sleep(15)
        driver.quit()

    def TC002(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)

        # 1. Klik dropdown profil
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        # 2. Klik "Ganti Peran"
        ganti_peran = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()

        time.sleep(5)

        driver.find_element(By.XPATH, "//div[@class='card-choice requester']").click()


        time.sleep(15)
        driver.quit()

    def TC003(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)

        # 1. Klik dropdown profil
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        # 2. Klik "Ganti Peran"
        ganti_peran = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()

        time.sleep(5)

        # Temukan elemen terlebih dahulu
        jobTake = driver.find_element(By.XPATH, "//div[@class='card-choice taker']")

        # Scroll agar terlihat di layar
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", jobTake)
        jobTake.click()

        time.sleep(15)
        driver.quit()

    def TC004(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)

        # 1. Klik dropdown profil
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        # 2. Klik "Ganti Peran"
        ganti_peran = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()

        time.sleep(5)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//h4[normalize-space()='40']").click()

        time.sleep(15)
        driver.quit()

    def TC005(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)

        # 1. Klik dropdown profil
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        # 2. Klik "Ganti Peran"
        ganti_peran = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()

        time.sleep(5)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//h4[normalize-space()='2']").click()

        time.sleep(15)
        driver.quit()

    def TC006(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)

        # 1. Klik dropdown profil
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        # 2. Klik "Ganti Peran"
        ganti_peran = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()

        time.sleep(5)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//h4[normalize-space()='7']").click()

        time.sleep(15)
        driver.quit()

    def TC007(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)

        # 1. Klik dropdown profil
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        # 2. Klik "Ganti Peran"
        ganti_peran = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()

        time.sleep(5)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='companyProfitCard']//div[@class='card-header p-3 pt-2']").click()

        time.sleep(15)
        driver.quit()

    def TC008(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)

        # 1. Klik dropdown profil
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        # 2. Klik "Ganti Peran"
        ganti_peran = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()

        time.sleep(5)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='lihat-log']").click()

        time.sleep(15)
        driver.quit()

# Test TC001
# tc001 = adminFunctionality()
# tc001.TC001()

# Test TC002
# tc002 = adminFunctionality()
# tc002.TC002()

# Test TC003
# tc003 = adminFunctionality()
# tc003.TC003()

# Test TC004
# tc004 = adminFunctionality()
# tc004.TC004()

# Test TC005
# tc005 = adminFunctionality()
# tc005.TC005()

# Test TC006
# tc006 = adminFunctionality()
# tc006.TC006()

# Test TC007
# tc007 = adminFunctionality()
# tc007.TC007()

# Test TC008
tc008 = adminFunctionality()
tc008.TC008()