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


class registerFunctionality():
    def TC001(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        # 1. Klik tombol dropdown profil
        profile_dropdown = driver.find_element(By.XPATH, "//a[@id='dropdownProfile']")
        profile_dropdown.click()

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-target='#loginModal']"))
        )
        login_button.click()

        popUplogin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][normalize-space()='Daftar']"))
        )
        popUplogin_button.click()

        popupRegister_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit'][normalize-space()='Daftar']"))
        )
        popupRegister_button.click()

        time.sleep(15)
        driver.quit()

    def TC002(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        # 1. Klik tombol dropdown profil
        profile_dropdown = driver.find_element(By.XPATH, "//a[@id='dropdownProfile']")
        profile_dropdown.click()

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-target='#loginModal']"))
        )
        login_button.click()

        popUplogin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][normalize-space()='Daftar']"))
        )
        popUplogin_button.click()
        time.sleep(2)

        popupRegister_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='first_name']"))
        )
        popupRegister_button.send_keys("Wilson")
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Daftar']").click()

        time.sleep(15)
        driver.quit()

    def TC003(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        # 1. Klik tombol dropdown profil
        profile_dropdown = driver.find_element(By.XPATH, "//a[@id='dropdownProfile']")
        profile_dropdown.click()

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-target='#loginModal']"))
        )
        login_button.click()

        popUplogin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][normalize-space()='Daftar']"))
        )
        popUplogin_button.click()
        time.sleep(2)

        popupRegister_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='password']"))
        )
        popupRegister_button.send_keys("Wilson")
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Daftar']").click()

        time.sleep(15)
        driver.quit()

    def TC004(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        # 1. Klik tombol dropdown profil
        profile_dropdown = driver.find_element(By.XPATH, "//a[@id='dropdownProfile']")
        profile_dropdown.click()

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-target='#loginModal']"))
        )
        login_button.click()

        popUplogin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][normalize-space()='Daftar']"))
        )
        popUplogin_button.click()
        time.sleep(2)

        popupRegister_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='last_name']"))
        )
        popupRegister_button.send_keys("Wilson")
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Daftar']").click()

        time.sleep(15)
        driver.quit()

    def TC005(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        # 1. Klik tombol dropdown profil
        profile_dropdown = driver.find_element(By.XPATH, "//a[@id='dropdownProfile']")
        profile_dropdown.click()

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-target='#loginModal']"))
        )
        login_button.click()

        popUplogin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][normalize-space()='Daftar']"))
        )
        popUplogin_button.click()
        time.sleep(2)

        popupRegister_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='password_confirmation']"))
        )
        popupRegister_button.send_keys("Wilson")
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Daftar']").click()

        time.sleep(15)
        driver.quit()

    def TC006(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        # 1. Klik tombol dropdown profil
        profile_dropdown = driver.find_element(By.XPATH, "//a[@id='dropdownProfile']")
        profile_dropdown.click()

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-target='#loginModal']"))
        )
        login_button.click()

        popUplogin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][normalize-space()='Daftar']"))
        )
        popUplogin_button.click()
        time.sleep(2)

        popupRegister_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='email-register']"))
        )
        popupRegister_button.send_keys("Wilson")
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Daftar']").click()

        time.sleep(15)
        driver.quit()

    def TC007(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        # 1. Klik tombol dropdown profil
        profile_dropdown = driver.find_element(By.XPATH, "//a[@id='dropdownProfile']")
        profile_dropdown.click()

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-target='#loginModal']"))
        )
        login_button.click()

        popUplogin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][normalize-space()='Daftar']"))
        )
        popUplogin_button.click()
        time.sleep(2)

        popupRegister_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='otp']"))
        )
        popupRegister_button.send_keys("Wilson")
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Daftar']").click()

        time.sleep(15)
        driver.quit()

    def TC008(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        # 1. Klik tombol dropdown profil
        profile_dropdown = driver.find_element(By.XPATH, "//a[@id='dropdownProfile']")
        profile_dropdown.click()

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-target='#loginModal']"))
        )
        login_button.click()

        popUplogin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][normalize-space()='Daftar']"))
        )
        popUplogin_button.click()
        time.sleep(2)

        popupRegister_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='password']"))
        )
        popupRegister_button.send_keys("password")
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Wilson")
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("Tjoeng")
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='password_confirmation']").send_keys("password")
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='email-register']").send_keys("wilsonwan16@gmail.com")
        time.sleep(20)

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Daftar']").click()

        time.sleep(15)
        driver.quit()

    def TC009(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()

        # 1. Klik tombol dropdown profil
        profile_dropdown = driver.find_element(By.XPATH, "//a[@id='dropdownProfile']")
        profile_dropdown.click()

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-target='#loginModal']"))
        )
        login_button.click()

        popUplogin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][normalize-space()='Daftar']"))
        )
        popUplogin_button.click()
        time.sleep(2)

        popupRegister_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='password']"))
        )
        popupRegister_button.send_keys("@Kerjain17")
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Wilson")
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("Tjoeng")
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='password_confirmation']").send_keys("@Kerjain17")
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='email-register']").send_keys("sonwt34@gmail.com")
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[@id='send-otp-button']").click()
        time.sleep(20)

        driver.find_element(By.XPATH, "//button[@type='submit'][normalize-space()='Daftar']").click()

        time.sleep(15)
        driver.quit()


# # Testing TC001
# tc001 = registerFunctionality()
# tc001.TC001()

# Testing TC002
# tc002 = registerFunctionality()
# tc002.TC002()

# Testing TC003
# tc003 = registerFunctionality()
# tc003.TC003()

# Testing TC004
# tc004 = registerFunctionality()
# tc004.TC004()

# Testing TC005
# tc005 = registerFunctionality()
# tc005.TC005()

# Testing TC006
# tc006 = registerFunctionality()
# tc006.TC006()

# Testing TC007
# tc007 = registerFunctionality()
# tc007.TC007()

# Testing TC008
# tc008 = registerFunctionality()
# tc008.TC008()

# Testing TC009
tc009 = registerFunctionality()
tc009.TC009()