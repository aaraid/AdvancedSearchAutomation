from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pyperclip

try:

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(chrome_options=options)
    #browser = webdriver.Chrome(executable_path=r"C:\chromedriver.exe") If driver is not on PATH

    browser.set_network_conditions(
    offline=False,
    latency=20,  # additional latency (ms)
    download_throughput=100 * 1024,  # maximal throughput
    upload_throughput=500 * 1024)  # maximal throughput

    browser.get('https://github.com/')

    search_box = browser.find_element(By.NAME, 'q')
    search_box.send_keys('react' + Keys.RETURN)

    wait = WebDriverWait(browser, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="js-pjax-container"]/div/div[2]/div[4]/a')))
    adv_search = browser.find_element(By.XPATH, '//*[@id="js-pjax-container"]/div/div[2]/div[4]/a')
    adv_search.click()

    wait.until(EC.presence_of_element_located((By.ID, 'search_language')))
    select_language = Select(browser.find_element(By.ID, 'search_language'))
    select_language.select_by_value('JavaScript')

    stars = browser.find_element(By.ID, 'search_stars')
    stars.send_keys('>45')

    followers = browser.find_element(By.ID, 'search_followers')
    followers.send_keys('>50')

    select_license = Select(browser.find_element(By.ID, 'search_license'))
    select_license.select_by_value('bsl-1.0')

    btn_search = browser.find_element(By.XPATH, '//*[@id="search_form"]/div[2]/div/div/button')
    btn_search.click()

    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="js-pjax-container"]/div/div[3]/div/div[2]/h3')))
    title = browser.find_element(By.XPATH, '//*[@id="js-pjax-container"]/div/div[3]/div/div[2]/h3')
    title_text = title.get_attribute('innerText')
    assert title_text == '1 repository result'

    repository = browser.find_element(By.XPATH, '//*[@id="js-pjax-container"]/div/div[3]/div/ul/li/div[2]/div[1]/div[1]/a')
    repository_text = repository.get_attribute('innerText')
    assert repository_text == 'mvoloskov/decider'
    repository.click()

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title="README.md"]')))
    readme_link = browser.find_element(By.XPATH, '//*[@title="README.md"]')
    readme_link.click()
    
    wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'remote-clipboard-copy')))
    copy_btn = browser.find_element(By.TAG_NAME, 'remote-clipboard-copy')
    copy_btn.click()
    
    status="none"
    while(status=="none"):
        status = browser.execute_script("btn = document.getElementsByTagName('remote-clipboard-copy')[0]; return getComputedStyle(btn.success).display")
        
    text = pyperclip.paste()
    cut = text[0:299]
    print(cut)

    browser.quit()
except Exception as e:
    browser.quit()
    print(e)
