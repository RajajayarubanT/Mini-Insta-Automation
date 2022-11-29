from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random
import time
import win32clipboard

def sleep_for_period_of_time():
    limit = random.randint(7,10)
    time.sleep(5)


def main():
    options = webdriver.ChromeOptions()
    # options.add_argument("--lang=en") #default
    userdatadir = "C:/Users/rajaj/AppData/Local/Google/Chrome/User Data" #existing chrome account
    
    options.add_argument(f"--user-data-dir={userdatadir}")
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    
    tag = "nseindia"
    
    browser.get("https://www.instagram.com/explore/tags/{}/".format(tag))
    time.sleep(5)
    
    xpath_focus_content_base = "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[1]/"
    xpath_focus_content = "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[1]/div[1]/a"
    xpath_focus_content = "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[1]/div[2]/a"

    limit = 2
    
    _limit = range(limit)
    
    content_collected = []

    for i in _limit:
        
        xpath_focus_content_str = xpath_focus_content_base + "div[{}]/a".format(i+1)
                
        xpath_focus_content = browser.find_element(By.XPATH, xpath_focus_content_str)
        
        content_collected.append(xpath_focus_content.get_attribute("href"))
            
            
    print(content_collected)
    sleep_for_period_of_time()

  
if __name__ == "__main__":
    main()
