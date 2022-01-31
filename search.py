#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import random
import spintax

from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
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
        print('Search Finished!')
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

    if 'music.youtube.com' in url:
        play_music(driver)
        time.sleep(45)
    else:
        play_video(driver)
        time.sleep(45)
        save_bandwidth(driver)
        time.sleep(5)
        change_playback_speed(driver)

    print('Search: ' + url)

    stop(5)

    return do_process(driver, urls)


def play_video(driver):
    try:
        driver.find_element_by_css_selector('[title^="Pause (k)"]')
    except:
        try:
            driver.find_element_by_css_selector('button.ytp-large-play-button.ytp-button').send_keys(Keys.ENTER)
        except:
            try:
                driver.find_element_by_css_selector('[title^="Play (k)"]').click()
            except:
                try:
                    driver.execute_script("document.querySelector('button.ytp-play-button.ytp-button').click()")
                except:
                    pass


def play_music(driver):
    try:
        driver.find_element_by_xpath('//*[@id="play-pause-button" and @title="Pause"]')
    except:
        try:
            driver.find_element_by_xpath('//*[@id="play-pause-button" and @title="Play"]').click()
        except:
            driver.execute_script('document.querySelector("#play-pause-button").click()')


def save_bandwidth(driver):
    try:
        driver.find_element_by_css_selector("button.ytp-button.ytp-settings-button").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[contains(text(),'Quality')]").click()
        time.sleep(2)

        random_quality = random.choices(['144p', '240p', '360p'], cum_weights=(0.7, 0.9, 1.00), k=1)[0]
        quality = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//span[contains(string(),'{random_quality}')]")))
        driver.execute_script("arguments[0].scrollIntoViewIfNeeded();", quality)
        quality.click()

    except:
        try:
            driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').click()
        except:
            pass


def change_playback_speed(driver):
    playback_speed = randint(2, 2)
    if playback_speed == 1:
        driver.find_element_by_id('movie_player').send_keys('<' * randint(1, 3))
    elif playback_speed == 2:
        driver.find_element_by_id('movie_player').send_keys('>' * randint(1, 3))


def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False

    return True


def search_video(driver):
    urls = []

    base_dir = os.path.dirname(os.path.realpath(__file__))
    file = base_dir + '/keywords.txt'

    try:
        key = driver.find_element_by_name('search_query')

        # get keyword list and extract each key
        with open(file, 'r') as f:
            keywords = [line.strip() for line in f]
            random_keyword = random.choice(keywords)
            keys = spintax.spin(random_keyword)

            # send keyword in the search box
            for char in keys:
                key.send_keys(char)

        time.sleep(1)

        # click search icon
        driver.find_element_by_css_selector('#search-icon-legacy > yt-icon').click()
        time.sleep(3)
        # click filter button to filter the videos for the recently uploaded, you can remove or edit this option
        driver.find_element_by_css_selector('#container > ytd-toggle-button-renderer > a').click()
        time.sleep(3)

        # filtering for last hour
        driver.find_element_by_xpath("(//yt-formatted-string[@class='style-scope ytd-search-filter-renderer'])[1]").click()
        time.sleep(3)

        # grabbing videos titles
        for i in range(2):
            ActionChains(driver).send_keys(Keys.END).perform()
            time.sleep(1)

        titles = driver.find_elements_by_xpath('//*[@id="video-title"]')

        # getting url from href attribute in title
        for i in titles:
            if i.get_attribute('href') is not None:
                urls.append(i.get_attribute('href'))
            else:
                continue
    except:
        print('There is a missing or corrupt query')

    return urls


def do_submit():
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file = base_dir + '/accounts.txt'

    try:
        with open(file, 'r') as rfile:
            accounts = rfile.readlines()
            for account in accounts:
                data = account.strip().split(':')
                if len(data) != 2:
                    continue
                driver = youtube_login(data[0], data[1])
                urls = search_video(driver)
                do_process(driver, urls)
                driver.quit()
                time.sleep(2)
            rfile.close()
    except IOError:
        print('Accounts is empty!')


if __name__ == '__main__':
    do_submit()
