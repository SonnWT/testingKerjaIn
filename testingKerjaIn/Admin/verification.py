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
        time.sleep(2)

        driver.find_element(By.XPATH, "//h4[normalize-space()='2']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsButton']").click()


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

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//h4[normalize-space()='2']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='approvedVerificationsButton']").click()


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

        time.sleep(3)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//h4[normalize-space()='2']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='rejectedVerificationsButton']").click()


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

        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//h4[normalize-space()='2']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[1]/td[8]/a[1]").click()

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

        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//h4[normalize-space()='2']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[1]/td[8]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='userSearchShow']").send_keys("Sierra\n")

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

        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//h4[normalize-space()='2']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[1]/td[8]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='userSearchShow']").send_keys("4342872732731353\n")

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

        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//h4[normalize-space()='2']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[1]/td[8]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='userSearchShow']").send_keys("10")

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
        ganti_peran = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()

        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[1]/td[8]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='userSearchShow']").send_keys("10")
        time.sleep(3)

        driver.find_element(By.XPATH, "//button[@id='clearSearchShow']").click()

        time.sleep(15)
        driver.quit()

    def TC009(self):
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

        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[2]/td[8]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='nextRequestButton']").click()

        time.sleep(15)
        driver.quit()

    def TC010(self):
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

        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[2]/td[8]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='previousRequestButton']").click()

        time.sleep(15)
        driver.quit()

    def TC011(self):
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

        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[2]/td[8]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='backButton']").click()

        time.sleep(15)
        driver.quit()

    def TC012(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[2]/td[8]/a[1]").click()
        time.sleep(2)

        # Klik tombol pertama: tolak
        hubungiBtn = driver.find_element(By.XPATH,
                                         "//button[@id='rejectButton']")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hubungiBtn)
        time.sleep(2)
        hubungiBtn.click()

        # Tunggu modal muncul
        wait.until(EC.visibility_of_element_located((By.ID, "rejectReasonModal")))
        time.sleep(1)  # tunggu animasi modal

        driver.find_element(By.XPATH, "//button[@id='BatalButton']").click()

        time.sleep(5)
        driver.quit()

    def TC013(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[2]/td[8]/a[1]").click()
        time.sleep(2)

        # Klik tombol pertama: tolak
        hubungiBtn = driver.find_element(By.XPATH,
                                         "//button[@id='rejectButton']")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hubungiBtn)
        time.sleep(2)
        hubungiBtn.click()

        # Tunggu modal muncul
        wait.until(EC.visibility_of_element_located((By.ID, "rejectReasonModal")))
        time.sleep(1)  # tunggu animasi modal

        driver.find_element(By.XPATH, "//button[@id='TolakVerifikasi']").click()

        time.sleep(5)
        driver.quit()

    def TC014(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[2]/td[8]/a[1]").click()
        time.sleep(2)

        # Klik tombol pertama: tolak
        hubungiBtn = driver.find_element(By.XPATH,
                                         "//button[@id='rejectButton']")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hubungiBtn)
        time.sleep(2)
        hubungiBtn.click()

        # Tunggu modal muncul
        wait.until(EC.visibility_of_element_located((By.ID, "rejectReasonModal")))
        time.sleep(1)  # tunggu animasi modal

        driver.find_element(By.XPATH, "//textarea[@id='rejection_reason']").send_keys("Karena ga pantas")
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[@id='TolakVerifikasi']").click()

        time.sleep(5)
        driver.quit()

    def TC015(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[2]/td[8]/a[1]").click()
        time.sleep(2)

        # Klik tombol pertama: tolak
        hubungiBtn = driver.find_element(By.XPATH,
                                         "//button[@id='rejectButton']")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hubungiBtn)
        time.sleep(2)
        hubungiBtn.click()

        # Tunggu modal muncul
        wait.until(EC.visibility_of_element_located((By.ID, "rejectReasonModal")))
        time.sleep(1)  # tunggu animasi modal

        driver.find_element(By.XPATH, "//span[normalize-space()='NIK Mismatch']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[@id='TolakVerifikasi']").click()

        time.sleep(5)
        driver.quit()

    def TC016(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[2]/td[8]/a[1]").click()
        time.sleep(2)

        # Klik tombol pertama: tolak
        hubungiBtn = driver.find_element(By.XPATH,
                                         "//button[@id='approveButton']")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hubungiBtn)
        time.sleep(2)
        hubungiBtn.click()

        # Tunggu modal muncul
        wait.until(EC.visibility_of_element_located((By.ID, "approveConfirmationModal")))
        time.sleep(1)  # tunggu animasi modal

        driver.find_element(By.XPATH, "//button[@id='CancelBtn']").click()

        time.sleep(5)
        driver.quit()

    def TC017(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[2]/td[8]/a[1]").click()
        time.sleep(2)

        # Klik tombol pertama: tolak
        hubungiBtn = driver.find_element(By.XPATH,
                                         "//button[@id='approveButton']")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hubungiBtn)
        time.sleep(2)
        hubungiBtn.click()

        # Tunggu modal muncul
        wait.until(EC.visibility_of_element_located((By.ID, "approveConfirmationModal")))
        time.sleep(1)  # tunggu animasi modal

        driver.find_element(By.XPATH, "//button[@id='yesApproveBtn']").click()

        time.sleep(5)
        driver.quit()

    def TC018(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[2]/td[8]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//select[@id='statusFilteredUserDropdown']").click()

        time.sleep(15)
        driver.quit()

    def TC019(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='approvedVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='lihat-detail']").click()
        time.sleep(2)

        time.sleep(15)
        driver.quit()

    def TC020(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='approvedVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='lihat-detail']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='userSearchShow']").send_keys("Leatha")

        time.sleep(15)
        driver.quit()

    def TC021(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='approvedVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='lihat-detail']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='userSearchShow']").send_keys("6916277312548650")

        time.sleep(15)
        driver.quit()

    def TC022(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='approvedVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='lihat-detail']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='userSearchShow']").send_keys("11")

        time.sleep(15)
        driver.quit()

    def TC023(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='approvedVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='lihat-detail']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='userSearchShow']").send_keys("11")
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[@id='clearSearchShow']").click()

        time.sleep(15)
        driver.quit()

    def TC024(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='approvedVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[2]/td[9]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='nextRequestButton']").click()

        time.sleep(15)
        driver.quit()

    def TC025(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='approvedVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[3]/td[9]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='previousRequestButton']").click()

        time.sleep(15)
        driver.quit()

    def TC026(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='approvedVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[3]/td[9]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='backButton']").click()

        time.sleep(15)
        driver.quit()

    def TC026(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='approvedVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[3]/td[9]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='backButton']").click()

        time.sleep(15)
        driver.quit()

    def TC027(self):
        print("test")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='approvedVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[3]/td[9]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//select[@id='statusFilteredUserDropdown']").click()

        time.sleep(15)
        driver.quit()

    def TC028(self):
        print("test")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='rejectedVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[3]/td[8]/a[1]").click()

        time.sleep(15)
        driver.quit()

    def TC029(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='rejectedVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[3]/td[8]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='userSearchShow']").send_keys("Derek")

        time.sleep(15)
        driver.quit()

    def TC030(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='rejectedVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[3]/td[8]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='userSearchShow']").send_keys("9477107755075152")

        time.sleep(15)
        driver.quit()

    def TC031(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='rejectedVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[3]/td[8]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='userSearchShow']").send_keys("7")

        time.sleep(15)
        driver.quit()

    def TC032(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='rejectedVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[3]/td[8]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='userSearchShow']").send_keys("7")
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[@id='clearSearchShow']").click()

        time.sleep(15)
        driver.quit()

    def TC033(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='rejectedVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[3]/td[8]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='nextRequestButton']").click()

        time.sleep(15)
        driver.quit()

    def TC034(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='rejectedVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[3]/td[8]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='previousRequestButton']").click()

        time.sleep(15)
        driver.quit()

    def TC035(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='rejectedVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[3]/td[8]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='backButton']").click()

        time.sleep(15)
        driver.quit()

    def TC036(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='rejectedVerificationsButton']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//tbody/tr[3]/td[8]/a[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//select[@id='statusFilteredUserDropdown']").click()

        time.sleep(15)
        driver.quit()

    def TC037(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Login dan navigasi
        profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownProfile")))
        profile_dropdown.click()

        ganti_peran = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='dropdown-item d-flex align-items-center gap-1']")))
        ganti_peran.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("admin@example.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Super645!")

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Login']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='card-choice admin']//h3").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@id='pendingVerificationsCard']//div[@class='card-footer p-3']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='userSearchIndex']").send_keys("Derek")
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='userSearchIndex']").click()
        time.sleep(2)

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
# tc008 = adminFunctionality()
# tc008.TC008()

# Test TC009
# tc009 = adminFunctionality()
# tc009.TC009()

# Test TC010
# tc010 = adminFunctionality()
# tc010.TC010()

# Test TC011
# tc011 = adminFunctionality()
# tc011.TC011()

# Test TC012
# tc012 = adminFunctionality()
# tc012.TC012()

# Test TC013
# tc013 = adminFunctionality()
# tc013.TC013()

# Test TC014
# tc014 = adminFunctionality()
# tc014.TC014()

# Test TC015
# tc015 = adminFunctionality()
# tc015.TC015()

# Test TC016
# tc016 = adminFunctionality()
# tc016.TC016()

# Test TC017
# tc017 = adminFunctionality()
# tc017.TC017()

# Test TC018
# tc018 = adminFunctionality()
# tc018.TC018()

# Test TC019
# tc019 = adminFunctionality()
# tc019.TC019()

# Test TC020
# tc020 = adminFunctionality()
# tc020.TC020()

# Test TC021
# tc021 = adminFunctionality()
# tc021.TC021()

# Test TC022
# tc022 = adminFunctionality()
# tc022.TC022()

# Test TC023
# tc023 = adminFunctionality()
# tc023.TC023()

# Test TC024
# tc024 = adminFunctionality()
# tc024.TC024()

# Test TC025
# tc025 = adminFunctionality()
# tc025.TC025()

# Test TC026
# tc026 = adminFunctionality()
# tc026.TC026()

# Test TC027
# tc027 = adminFunctionality()
# tc027.TC027()

# Test TC028
# tc028 = adminFunctionality()
# tc028.TC028()

# Test TC029
# tc029 = adminFunctionality()
# tc029.TC029()

# Test TC030
# tc030 = adminFunctionality()
# tc030.TC030()

# Test TC031
# tc031 = adminFunctionality()
# tc031.TC031()

# Test TC032
# tc032 = adminFunctionality()
# tc032.TC032()

# Test TC033
# tc033 = adminFunctionality()
# tc033.TC033()

# Test TC034
# tc034 = adminFunctionality()
# tc034.TC034()

# Test TC035
# tc035 = adminFunctionality()
# tc035.TC035()

# Test TC036
# tc036 = adminFunctionality()
# tc036.TC036()

# Test TC037
tc037 = adminFunctionality()
tc037.TC037()