import re, time, os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service


def func():
    DELAY = 5
    PATH_PWD = os.path.dirname(os.path.realpath(__file__))

    FF_OPTIONS = [
        # '--headless',
        '--no-sandbox',
        '--start-maximized',
        '--start-fullscreen',
        '--single-process',
        '--disable-dev-shm-usage',
        '--incognito',
        '--disable-blink-features=AutomationControlled',
        '--disable-xss-auditor',
        '--disable-web-security',
        '--ignore-certificate-errors',
        '--log-level=3',
        '--disable-notifications',
        '--disable-infobars',
        '--disable-gpu',
        '--disable-extensions',
        
    ]

    SET_PREF = {
        'general.useragent.override':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'permissions.default.desktop-notification': 1,
        'dom.webnotifications.enabled': 1,
        'dom.push.enabled': 1,
        'intl.accept_languages': 'en-US',
    }

    FF_EXP = {
        'useAutomationExtension':False,
        'excludeSwitches':['enable-automation']
    }
    
    myOptions = FirefoxOptions()
    [myOptions.add_argument(opt) for opt in FF_OPTIONS]
    [myOptions.set_preference(key, value) for key, value in SET_PREF.items()]
    
    
    path_gecko = os.path.join(PATH_PWD, 'geckodriver-v0.33.0-win32', 'geckodriver.exe')
    path_firefoxBin = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    
    print('')
    print('[*] path_gecko:', os.path.exists(path_gecko))
    print('[*] path_firefoxBin:', os.path.exists(path_firefoxBin))

    myService = Service(path_gecko)
    myOptions.binary_location = path_firefoxBin

    print('[*] Starting Driver')
    print('')

    driver = webdriver.Firefox(service=myService, options=myOptions)
    

    driver.get('https://www.kijiji.ca')

    time.sleep(DELAY)
    print('[*] Inputting Login')

    driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]').click()
    
    time.sleep(DELAY)

    
    

    # elem = driver.find_element(By.ID, 'emailOrNickname')
    # elem.send_keys("pawn88@live.com")
    # elem.send_keys(Keys.TAB)
    # elem.send_keys('westside')
    # elem.send_keys(Keys.ENTER)

    # time.sleep(DELAY)

    
    # time.sleep(DELAY)
    # print('[*] Deleting Previous Ad')

    # driver.find_element(By.XPATH, '//a[contains(text(), "$600")]')
    # elem.click()






if __name__ == '__main__':
    func()
