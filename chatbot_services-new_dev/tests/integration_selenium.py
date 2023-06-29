import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class FinBot(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def check_title(self):
        self.assertEqual("Goldman Sachs" , self.driver.title)

    def check_scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 0);")


    def check_dropdown(self):
        dropdown = self.driver.find_element(By.XPATH,"/html/body/div/div/nav/div[2]/button")
        time.sleep(1)
        dropdown.click()
        time.sleep(1)
        dropdown.click()

    def check_new_chat(self):
        time.sleep(1)
        new_chat_btn = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[5]/button")
        time.sleep(1)
        new_chat_btn.click()
        time.sleep(1)
    
    def check_cross(self):
        cross = self.driver.find_element(By.XPATH,"/html/body/div/div/main/div/div[5]/div/div/div/div[1]/button[1]")
        time.sleep(1)
        cross.click()
        time.sleep(1)
    
    def check_subtitle(self):
        finbot = self.driver.find_element(By.XPATH,"/html/body/div/div/main/div/div[5]/div/div/div/div[1]")
        time.sleep(1)
        finbot_text = "FinBOT 🤖"
        self.assertEqual(finbot_text, finbot.text)
        time.sleep(1)

    def check_minimize(self):
        m_button = self.driver.find_element(By.XPATH,"/html/body/div/div/main/div/div[5]/div/div/div/div[1]/button[2]")
        time.sleep(1)
        m_button.click()
        time.sleep(1)
        m_button.click()
        time.sleep(1)

    def check_maximize(self):
        m_button = self.driver.find_element(By.XPATH,"/html/body/div/div/main/div/div[5]/div/div/div/div[1]/button[3]")
        time.sleep(1)
        m_button.click()
        time.sleep(1)
        c_button = self.driver.find_element(By.XPATH,"/html/body/div/div/main/div/div[6]/div/button")
        time.sleep(1)
        c_button.click()
        time.sleep(1)
    
    def check_query(self):
        ip_field = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[5]/div/div/div/div[3]/form/input")
        question = "What types of investments does Goldman Sachs allow?"
        for char in question:
            ip_field.send_keys(char)
            time.sleep(0.2)
        time.sleep(1)
        ip_field.send_keys(Keys.ENTER)
        time.sleep(15)
        resp_block = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[5]/div/div/div/div[2]/div[3]/div/span")
        time.sleep(6)
        self.assertNotEqual("", resp_block.text)
    
    def check_positive_feedback(self):
        time.sleep(55)
        yes_button = self.driver.find_element(By.XPATH,"/html/body/div/div/main/div/div[5]/div/div/div/div[2]/div[6]/div/span/div/button[1]")
        time.sleep(1)
        yes_button.click()
        time.sleep(2)
        response = self.driver.find_element(By.XPATH,"/html/body/div/div/main/div/div[5]/div/div/div/div[2]/div[7]/div/span")
        self.assertEqual("Thank you for valuable response", response.text)


    def check_negative_feedback(self):
        time.sleep(2)
        no_button = self.driver.find_element(By.XPATH,"/html/body/div/div/main/div/div[5]/div/div/div/div[2]/div[6]/div/span/div/button[2]")
        no_button.click()
        time.sleep(2)
        response = self.driver.find_element(By.XPATH,"/html/body/div/div/main/div/div[5]/div/div/div/div[2]/div[8]/div/span")
        self.assertEqual("We are really sorry to hear that. You can contact us at query@gs.com", response.text)
    
    def test_runner(self):
        driver = self.driver
        driver.get(self.front)
        time.sleep(2)
        
        self.check_title()
        self.check_scroll()
        self.check_dropdown()
        self.check_new_chat()
        self.check_cross()
        self.check_new_chat()
        self.check_subtitle()
        self.check_minimize()
        self.check_maximize()
        self.check_query()
        self.check_positive_feedback()
        self.check_negative_feedback()
    
        self.driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run FinBot tests')
    parser.add_argument('--front', type=str, help='Frontend link to test')
    args = parser.parse_args()

    if args.front:
        FinBot.front = args.front
    else:
        print("Please give frontend link.")
        exit()

    unittest.main(argv=[''], verbosity=2, exit=False)
