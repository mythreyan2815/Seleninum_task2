from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
import re

def extract_phone_number(driver):
    try:
        
        phone_number_element = driver.find_element(By.XPATH, "//a[contains(@href, 'tel:')]")
        phone_number = phone_number_element.text.strip()
        return phone_number if phone_number != "-" else None
    except:
        return None

def extract_email(driver):
    try:
        
        email_element = driver.find_element(By.XPATH, "//a[contains(@href, 'mailto:')]")
        email_address = email_element.text.strip()
        return email_address if email_address != "-" else None
    except:
        return None

def search_company_contact_us(company_name):
    
    chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'

    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_path

    
    driver = webdriver.Chrome(options=chrome_options)

    try:
        
        driver.get("https://www.google.com/")

        
        search_box = driver.find_element("name", "q")
        search_query = f"{company_name} contact us"
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

        
        time.sleep(2)

        
        website_link = driver.find_element(By.CSS_SELECTOR, "div.tF2Cxc a").get_attribute('href')

       
        print(f"Company Name: {company_name}")
        print(f"Website: {website_link}")

        
        driver.get(website_link)

        
        time.sleep(2)

       
        phone_number = extract_phone_number(driver)
        print(f"Phone Number: {phone_number}")

        
        email_address = extract_email(driver)
        print(f"Email Address: {email_address}")

        
        with open('company_data.csv', 'a', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)

            
            if csvfile.tell() == 0:
                csv_writer.writerow(['Company Name', 'Website', 'Phone Number', 'Email Address'])

            csv_writer.writerow([company_name, website_link, phone_number, email_address])

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        
        driver.quit()


with open('company_names.txt', 'r') as file:
    company_names = file.read().splitlines()


for company_name in company_names:
    search_company_contact_us(company_name)
