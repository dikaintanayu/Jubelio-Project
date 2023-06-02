from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class JubelioTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.addCleanup(self.driver.quit)

    #page login with correct credential
    def test_page_login(self):
        self.driver.get('https://app.jubelio.com/login')
        self.driver.find_element(By.CSS_SELECTOR,'[name="email"]').send_keys('qa.rakamin.jubelio@gmail.com')
        self.driver.find_element(By.CSS_SELECTOR,'[name="password"]').send_keys('Jubelio123!')
        self.driver.find_element(By.CSS_SELECTOR,'[type="submit"]').click()
        sleep(5)
        selamatText = self.driver.find_element(By.XPATH,('//*[@id="page-wrapper"]/div[2]/div/div/div[1]/h1')).text
        self.assertIn('Selamat Datang', selamatText)  
    

    #page login with incorrect credential
    def test_page_login_incorrect_credential(self):       
        self.driver.get('https://app.jubelio.com/login')
        self.driver.find_element(By.CSS_SELECTOR,'[name="email"]').send_keys('qa.rakamin.jubelio@gmail.com')
        self.driver.find_element(By.CSS_SELECTOR,'[name="password"]').send_keys('Jubelio12')
        self.driver.find_element(By.CSS_SELECTOR,'[type="submit"]').click()
        sleep(5)
        incorrectText = self.driver.find_element(By.XPATH,('//*[@id="root"]/div/div[1]/li')).text
        self.assertIn('Password atau email anda salah.', incorrectText)
        

if __name__ == '__main__':
    unittest.main(verbosity=2)
        


