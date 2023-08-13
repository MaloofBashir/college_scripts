from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import os







def extract_pdf(reg_no):
    time.sleep(2)
    driver=webdriver.Chrome()

    driver.get("https://egov.uok.edu.in/CollegeAdm/AdmDetails/StudentStatus_Promotional.aspx?rcodert=20211&rsemid=5&appid=908iiou1234mn&serviceid=1xx258660021553")
    wait = WebDriverWait(driver, 100)
    input_element = wait.until(EC.visibility_of_element_located((By.ID, "txtRegNo")))
    input_element.send_keys(reg_no)

    status_button= wait.until(EC.visibility_of_element_located((By.ID, "btnFormStatus")))
    status_button.click()


    pyautogui.hotkey("ctrl", "p")
    time.sleep(2)
  
    pyautogui.press("enter")
    time.sleep(2)
    text_to_type = reg_no

    pyautogui.press("a")
    pyautogui.typewrite(text_to_type)
    pyautogui.typewrite(text_to_type)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press("enter")
    pyautogui.press('tab')

    time.sleep(3)
    pyautogui.press("enter")

# input=driver.find_element_by_id("txtRegNo")
count=1
def download_pdfs():
    with open("roolno.txt",'r') as file:
        contents=file.read()
        values=contents.split(",")
        for val in values:
            extract_pdf(val)
            

download_pdfs()