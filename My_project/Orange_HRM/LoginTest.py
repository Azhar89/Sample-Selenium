from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append("C://Users/HARDSTONE/PycharmProjects/Demo_projects")
from My_project.POM_Pages.HomePOM import HomePage
from My_project.POM_Pages.LoginPOM import LoginPage
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/HARDSTONE/PycharmProjects/Demo_projects/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()

        homepage = HomePage(driver)

        homepage.click_welcome()
        homepage.click_logout()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test is completed.")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/HARDSTONE/PycharmProjects/Demo_projects/Report'))
