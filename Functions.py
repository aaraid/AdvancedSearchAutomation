from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pyperclip

def BrowserSetup(URL):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        global browser
        #browser = webdriver.Chrome(chrome_options=options)
        browser = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", chrome_options=options) #If driver is not on PATH

        browser.set_network_conditions( #simulate slow internet connection
        offline=False,
        latency=10,  # additional latency (ms)
        download_throughput=100 * 1024,  # maximal throughput
        upload_throughput=500 * 1024)  # maximal throughput
        browser.get(URL)
    except:
        browser.quit()
        print("BrowserSetup Error")

def SearchRepository(repository):
    try:
        search_box = browser.find_element(By.NAME, 'q') #dont need wait for first page
        search_box.send_keys(repository + Keys.RETURN)
    except:
        browser.quit()
        print("SearchRepository Error")

def SearchRefinement(language, qty_stars, qty_followers, license_type):
    try:
        global wait
        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="js-pjax-container"]/div/div[2]/div[4]/a')))
        adv_search = browser.find_element(By.XPATH, '//*[@id="js-pjax-container"]/div/div[2]/div[4]/a')
        adv_search.click()

        wait.until(EC.presence_of_element_located((By.ID, 'search_language')))
        select_language = Select(browser.find_element(By.ID, 'search_language'))
        select_language.select_by_value(language)

        stars = browser.find_element(By.ID, 'search_stars')
        stars.send_keys(qty_stars)

        followers = browser.find_element(By.ID, 'search_followers')
        followers.send_keys(qty_followers)

        select_license = Select(browser.find_element(By.ID, 'search_license'))
        select_license.select_by_value(license_type)

        btn_search = browser.find_element(By.XPATH, '//*[@id="search_form"]/div[2]/div/div/button')
        btn_search.click()
    except:
        browser.quit()
        print("RefinementSearch Error")

def CheckResult(qty_results, repository_name):
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="js-pjax-container"]/div/div[3]/div/div[2]/h3')))
        title = browser.find_element(By.XPATH, '//*[@id="js-pjax-container"]/div/div[3]/div/div[2]/h3')
        title_text = title.get_attribute('innerText')
        assert title_text == qty_results #checks if there's only one result / It could be a parameter

        global repository
        repository = browser.find_element(By.XPATH, '//*[@id="js-pjax-container"]/div/div[3]/div/ul/li/div[2]/div[1]/div[1]/a')
        repository_text = repository.get_attribute('innerText')
        assert repository_text == repository_name #checks if result is correct / It could be a parameter
    except:
        browser.quit()
        print("CheckResult Error")

def PrintReadMe(qty_chars):
    try:
        repository.click()

        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title="README.md"]')))
        readme_link = browser.find_element(By.XPATH, '//*[@title="README.md"]')
        readme_link.click()
        
        wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'remote-clipboard-copy')))
        copy_btn = browser.find_element(By.TAG_NAME, 'remote-clipboard-copy')
        copy_btn.click()
        
        status="none"
        while(status=="none"): # checks if copy_btn has changed to success, so data is available at the clipboard
            status = browser.execute_script("btn = document.getElementsByTagName('remote-clipboard-copy')[0]; return getComputedStyle(btn.success).display")
            
        text = pyperclip.paste()
        cut = text[0:qty_chars] # qty of chars to print
        print(cut)
    except:
        browser.quit()
        print("PrintReadMe Error")

def TearDown():
    browser.quit()