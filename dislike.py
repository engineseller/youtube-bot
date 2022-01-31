#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time

from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager as CM

print(r"""\
        ╓░▒▒╦╗
        jÜ¢¢╩╩▒_               r▒▒Ü¢¢Ä¢ÄÄÄ▒╗╓r                     ╓░░▒▒Ä▒⌐
       j¢╩¢▒R╚ºªÜ▒mr╖╓╓.    ºΓ          º╚¢╩¢¢▒╗▒▒╓        ╓    ╖▒▒╝¢¢¢¢¢╩¢¢▒
      ºº╚ªº        j╚╩¢¢Ä=       ╖r▒▒▒▒▒▒m╓º¢╩¢╩¢¢¢¢¢¢▒▒▒Ü¢╩¢¢¢¢¢¢¢╝╩╩¢╩¢╩¢╩░
      ┌¢▒▒Ü░r▒▒▒»╓▒╝¢╩¢ª      ╓▒Ü╩¢¢¢╩¢¢¢¢¢¢▒╝¢╩¢╩¢╩¢╩¢¢¢╝¢╩¢╩¢╩¢╩¢╩¢╩¢╩╩╩¢╩¢░r░═
      ¢╩¢¢╩¢¢¢¢¢¢¢¢╩╩╩▒      ▒Ü¢╩╩¢╩╩╩╩╩¢╩¢╩¢╝¢╩¢░º╝¢╩╩╩¢╩¢╩╩╩¢╩¢╩¢╩╩╩╩╩¢╩¢╩╩¢¢▒R
        «╩¢╩¢╩¢╩╩╩¢╩¢▒      ▒Ö╩╩¢╩¢╩¢╩¢╩¢╩╩╩¢╩¢╩╩Γ  ªºº ¢╩¢╩¢╩¢╩╩╩¢╩¢╩¢╩¢╩╩╩¢╩¢▒
        º▒╝╩¢╩¢╩¢╩╩╩¢▒     ▐Ü╝¢╝¢╩╩╩¢╩¢╩¢╩╩╩¢ª╙º      ╔▒╝╩╩╩¢╩¢╩¢╩╩╩¢╩¢╩¢╩╩╩¢╩¢¢▒
      º¬²ê╩╩¢╩¢╩¢╩¢╩¢░      ¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢¢▒▒▒¬     ²╩╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢░
        ª╝¢╩¢╩¢╩¢╩¢╩╩¢      j╝¢╩¢╩¢╩¢╩¢╩¢╩╩╩¢╩¢¢¢Γ «Ä▒▒▒╝╝¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩╩╩¢╩¢╝¢╓_
         «¢╩¢╩¢╩¢╩¢╩¢╩▒      º╩╩¢╩¢╩¢╩¢╩¢╩╩╩¢╩¢╩¢░▒Ö¢¢¢¢¢╩╩╩¢╩¢╩¢╩¢╩¢╩╩╩¢╩╩╩¢╩¢╩▒╝▒.
          j╝╩╩¢╩¢╩¢╩╩╩¢▒╖      º¢╩╩╩¢╩¢╩¢╩╩╚j▒╝╩¢Ä¢╝¢╝¢╩¢╩¢╩╩╩¢╩¢╩╩¢¢╩▒╚╙ºΓ
            │¢╚╝╩╩¢╩¢╩¢▒╝▒╗         ºººº  ╓▒╝¢╩╩╩╩¢╩¢╩¢▒╚▒╝╩╩╩╩=º
                 ╩¢╩╩╩¢¬    º!r╗╓   ╓╖r   ╙==  j╩  ╙º
                  ╙ºº └       └¢¢¢▒Ä=º        ¢╩ª
""")


def stop(n):
    time.sleep(randint(2, n))


def youtube_login(email, password):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-infobars")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--unlimited-storage")
    options.add_argument('--disable-features=UserAgentClientHint')
    options.add_argument("--mute-audio")
    options.add_argument('--no-sandbox')

    # options.add_argument("--window-size=1920,1080")
    # options.add_argument('--headless')
    # options.add_argument(f'--proxy-server={proxy_type}://{proxy}')

    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    options.add_experimental_option('useAutomationExtension', False)
    # options.add_experimental_option('prefs', {'intl.accept_languages': 'en_US,en'})

    driver = webdriver.Chrome(options=options, executable_path=CM().install())

    # driver.execute_script("document.body.style.zoom='80%'")
    driver.execute_script('window.localStorage.clear();')
    driver.delete_all_cookies()

    driver.get(
        'https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

    # finding email field and putting our email on it
    email_field = driver.find_element_by_xpath('//*[@id="identifierId"]')
    email_field.send_keys(email)
    driver.find_element_by_id("identifierNext").click()
    stop(5)

    # finding pass field and putting our pass on it
    find_pass_field = (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    WebDriverWait(driver, 50).until(EC.presence_of_element_located(find_pass_field))
    pass_field = driver.find_element(*find_pass_field)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable(find_pass_field))
    pass_field.send_keys(password)
    driver.find_element_by_id("passwordNext").click()
    stop(5)

    WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-masthead button#avatar-btn")))
    print("Login Success")

    return driver


def do_process(driver, urls):
    if len(urls) == 0:
        print('Dislike Finished!')
        return []

    # Pop a URL from the array
    url = urls.pop()

    # Visit page
    driver.get(url)
    driver.implicitly_wait(1)

    # checking if video is unavailable
    if not check_exists_by_xpath(driver, '//*[@id="movie_player"]'):
        return do_process(driver, urls)

    # checking if comments are disabled
    if not check_exists_by_xpath(driver, '//*[@id="simple-box"]/ytd-comment-simplebox-renderer'):
        return do_process(driver, urls)

    # checking if video is a livestream
    if check_exists_by_xpath(driver, '//*[@id="contents"]/ytd-message-renderer'):
        return do_process(driver, urls)

    driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
    time.sleep(2)

    dislike_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[5]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[2]/a/yt-icon-button/button/yt-icon'
    dislike_button = EC.presence_of_element_located(By.XPATH, dislike_xpath)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable(dislike_button)).click()

    print('Disliked: ' + url)

    stop(5)

    return do_process(driver, urls)


def get_urls():
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file = base_dir + '/urls.txt'

    urls = []
    try:
        with open(file, 'r') as rfile:
            data = rfile.readlines()
            for i in data:
                if i not in urls:  # check duplicate
                    urls.append(i)
            rfile.close()
    except IOError:
        print('Urls is empty!')

    return urls


def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False

    return True


def do_submit():
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file = base_dir + '/accounts.txt'

    urls = get_urls()
    if len(urls) == 0:
        print('Urls is empty!')
        sys.exit(0)

    try:
        with open(file, 'r') as rfile:
            accounts = rfile.readlines()
            for account in accounts:
                data = account.strip().split(':')
                if len(data) != 2:
                    continue
                driver = youtube_login(data[0], data[1])
                do_process(driver, urls)
                driver.quit()
                time.sleep(2)
            rfile.close()
    except IOError:
        print('Accounts is empty!')


if __name__ == '__main__':
    do_submit()
