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


class loginFunctionality():
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
            EC.element_to_be_clickable((By.XPATH, "// button[contains(text(), 'Masuk')]"))
        )
        popUplogin_button.click()

        time.sleep(15)
        driver.quit()

    def TC002(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)

        # 1. Klik tombol dropdown profil
        profile_dropdown = driver.find_element(By.XPATH, "//a[@id='dropdownProfile']")
        profile_dropdown.click()

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-target='#loginModal']"))
        )
        login_button.click()
        time.sleep(2)

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("s")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("s")

        time.sleep(15)
        driver.quit()

    def TC003(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)

        # 1. Klik tombol dropdown profil
        profile_dropdown = driver.find_element(By.XPATH, "//a[@id='dropdownProfile']")
        profile_dropdown.click()

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-target='#loginModal']"))
        )
        login_button.click()
        time.sleep(2)

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("sonwt34@gmail.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("s")
        time.sleep(2)

        modal_background = driver.find_element(By.ID, "loginModal")
        modal_background.click()
        time.sleep(0.5)

        popUplogin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "// button[contains(text(), 'Masuk')]"))
        )
        popUplogin_button.click()

        time.sleep(15)
        driver.quit()

    def TC004(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)

        # 1. Klik tombol dropdown profil
        profile_dropdown = driver.find_element(By.XPATH, "//a[@id='dropdownProfile']")
        profile_dropdown.click()

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-target='#loginModal']"))
        )
        login_button.click()
        time.sleep(2)

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("s@gmail")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Kerjain17")
        time.sleep(2)

        modal_background = driver.find_element(By.ID, "loginModal")
        modal_background.click()
        time.sleep(0.5)

        popUplogin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "// button[contains(text(), 'Masuk')]"))
        )
        popUplogin_button.click()

        time.sleep(15)
        driver.quit()

    def TC005(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)

        # 1. Klik tombol dropdown profil
        profile_dropdown = driver.find_element(By.XPATH, "//a[@id='dropdownProfile']")
        profile_dropdown.click()

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-target='#loginModal']"))
        )
        login_button.click()
        time.sleep(2)

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("sonwt34@gmail.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Kerjain17")
        time.sleep(2)

        popUplogin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "// button[contains(text(), 'Masuk')]"))
        )
        popUplogin_button.click()

        time.sleep(15)
        driver.quit()

    def TC006(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)

        # 1. Klik tombol dropdown profil
        profile_dropdown = driver.find_element(By.XPATH, "//a[@id='dropdownProfile']")
        profile_dropdown.click()

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-target='#loginModal']"))
        )
        login_button.click()
        time.sleep(2)

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("sonwt34@gmail.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Kerjain17")
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='remember_me']").click()

        popUplogin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "// button[contains(text(), 'Masuk')]"))
        )
        popUplogin_button.click()

        time.sleep(15)
        driver.quit()

    def TC007(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)

        # 1. Klik tombol dropdown profil
        profile_dropdown = driver.find_element(By.XPATH, "//a[@id='dropdownProfile']")
        profile_dropdown.click()

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-target='#loginModal']"))
        )
        login_button.click()
        time.sleep(2)

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("sonwt34@gmail.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Kerjain17")
        time.sleep(2)

        popUplogin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "// button[contains(text(), 'Masuk')]"))
        )
        popUplogin_button.click()

        time.sleep(15)
        driver.quit()

    def TC008(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)

        # 1. Klik tombol dropdown profil
        profile_dropdown = driver.find_element(By.XPATH, "//a[@id='dropdownProfile']")
        profile_dropdown.click()

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-target='#loginModal']"))
        )
        login_button.click()
        time.sleep(2)

        popUplogin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//form[@id='login-form']//img[@alt='Google']"))
        )
        popUplogin_button.click()

        time.sleep(30)
        driver.quit()

    def TC009(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("http://127.0.0.1:8000/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)

        # 1. Klik tombol dropdown profil
        profile_dropdown = driver.find_element(By.XPATH, "//a[@id='dropdownProfile']")
        profile_dropdown.click()

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-target='#loginModal']"))
        )
        login_button.click()
        time.sleep(2)

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-login")))
        email_input.send_keys("sonwt34@gmail.com")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-login")))
        password_input.send_keys("@Kerjain17")
        time.sleep(2)

        popUplogin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "// button[contains(text(), 'Masuk')]"))
        )
        popUplogin_button.click()
        time.sleep(2)

        # 1. Klik tombol dropdown profil
        profile_dropdown = driver.find_element(By.XPATH, "//a[@id='dropdownProfile']")
        profile_dropdown.click()

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='dropdown-item d-flex align-items-center gap-1']"))
        )
        login_button.click()

        time.sleep(15)
        driver.quit()


# Testing TC001
# tc001 = loginFunctionality()
# tc001.TC001()

# Testing TC002
# tc002 = loginFunctionality()
# tc002.TC002()

# Testing TC003
# tc003 = loginFunctionality()
# tc003.TC003()

# Testing TC004
# tc004 = loginFunctionality()
# tc004.TC004()

# Testing TC005
# tc005 = loginFunctionality()
# tc005.TC005()

# Testing TC006
# tc006 = loginFunctionality()
# tc006.TC006()

# Testing TC007
# tc007 = loginFunctionality()
# tc007.TC007()

# Testing TC008
# tc008 = loginFunctionality()
# tc008.TC008()

# Testing TC009
tc009 = loginFunctionality()
tc009.TC009()