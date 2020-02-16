from selenium import webdriver
from time import sleep
import random
import sys
from selenium.webdriver.chrome.options import Options


class InstagramBot:
    def __init__(self, password, uname):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath(
            "//a[contains(text(), 'Log in')]").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "//input[@name=\"username\"]").send_keys(uname)

        self.driver.find_element_by_xpath(
            "//input[@name=\"password\"]").send_keys(password)

        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(4)

        self.driver.get("https://www.instagram.com/adellaftr/")

        # gathering photos
        pic_hrefs = []
        for i in range(1, 7):
            try:
                self.driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)
                # get tags
                hrefs_in_view = self.driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href)
                 for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            self.driver.get(pic_href)
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                sleep(random.randint(2, 4))
                def like_button(): return self.driver.find_element_by_class_name("wpO6b ")
                like_button().click()

            except Exception as e:
                sleep(2)
            unique_photos -= 1
        sleep()


# +62 812-9155-4432
InstagramBot("stringpass", "stringuname")
