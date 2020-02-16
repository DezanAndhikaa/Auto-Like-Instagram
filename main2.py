from selenium import webdriver
from time import sleep
import random
import sys
from selenium.webdriver.chrome.options import Options


class InstagramBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath(
            "//a[contains(text(), 'Log in')]").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "//input[@name=\"username\"]").send_keys("codinginsample1@gmail.com")

        self.driver.find_element_by_xpath(
            "//input[@name=\"password\"]").send_keys("codingindingin")

        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(4)
        self.driver.get("https://www.instagram.com/p/B8geym5gguZ/")
        sleep(2)

        like = self.driver.find_element_by_class_name("wpO6b ")
        sleep(2)
        like.click()

        sleep()


# +62 812-9155-4432
InstagramBot()
