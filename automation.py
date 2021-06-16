import os
import setup
from selenium.webdriver import Chrome
from selenium import webdriver
from datetime import datetime
import time

username = ''
password = ''
download_dir = setup.driver_setup(mode='root')
driver_location = setup.driver_setup(mode='path')


def start_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_experimental_option('prefs', {'download.default_directory': download_dir})
    driver = Chrome(executable_path=driver_location, options=options)

    return driver


def cuid_login(driver):
    cuid_username = driver.find_element_by_xpath(
        '/html/body/div/div/form/input[1]'
    )
    cuid_username.send_keys(username)

    cuid_password = driver.find_element_by_xpath(
        '/html/body/div/div/form/input[2]'
    )
    cuid_password.send_keys(password)

    cuid_login_button = driver.find_element_by_xpath(
        '/html/body/div/div/form/input[4]'
    )
    cuid_login_button.click()


def sf_login(driver):
    driver.get("https://lumn.my.salesforce.com/")

    sf_sso_button = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div[6]/button[1]'
    )
    sf_sso_button.click()

    cuid_login(driver)


def bssapp(driver, ban):
    driver.get("https://bssapp.savvis.net/")
    driver.get("https://bssapp.savvis.net/vantive/AIPOptionsSearchForm.cgi?sessionId=1%27")

    ban_search = driver.find_element_by_xpath(
        '/html/body/form/table/tbody/tr[2]/th/input'
    )
    ban_search.send_keys(ban)

    filter_active = driver.find_element_by_xpath(
        '/html/body/form/table/tbody/tr[7]/th[2]/select/option[2]'
    )
    filter_active.click()

    time.sleep(5)

    excel_button = driver.find_element_by_xpath(
        '/html/body/form/table/tbody/tr[9]/td/table/tbody/tr[2]/td[1]/input[3]'
    )
    excel_button.click()

    now = datetime.now()

    downloaded_file = download_dir + setup.what_am_i('divider') + 'AIPOptionsSearchResults.cgi'
    processed_file = download_dir + setup.what_am_i('divider') + now.strftime("%Y-%m-%d %H-%M-%S - ") + ban + ' - aips'

    while not os.path.exists(downloaded_file):
        time.sleep(5)

    os.rename(downloaded_file, processed_file + '.html')

    driver.close()

    return processed_file