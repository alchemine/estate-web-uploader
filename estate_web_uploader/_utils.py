"""Utility module.
"""

# from estate_web_uploader.common import *

from time import sleep
from retrying import retry

import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    options = Options()
    options.add_argument('--disable-gpu')
    # options.add_argument('--headless')
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


@retry(wait_fixed=1000)
def submit_text_retry(driver, text, css_selector=None, send_return=False, sleep_before=1, sleep_after=0):
    sleep(sleep_before)
    if css_selector is None:
        input_element = driver.switch_to.active_element
    else:
        input_element = driver.find_element(By.CSS_SELECTOR, css_selector)
    input_element.send_keys(text)
    sleep(sleep_after)
    if send_return:
        input_element.send_keys(Keys.RETURN)


@retry(wait_fixed=1000)
def send_active_return(driver):
    elem = driver.switch_to.active_element
    elem.send_keys(Keys.RETURN)


@retry(wait_fixed=1000)
def click_button_retry(driver, selector, sleep_before=1, sleep_after=0):
    sleep(sleep_before)
    button = driver.find_element(By.CSS_SELECTOR, selector)
    button.click()
    sleep(sleep_after)
