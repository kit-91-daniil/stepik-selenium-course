import time
import unittest
from selenium import webdriver


class TestAbs(unittest.TestCase):
    def setUp(self):
        self.link1 = "http://suninjuly.github.io/registration1.html"
        self.link2 = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.close()

    def test_registration1(self):
        self.browser.get(self.link1)
        time.sleep(1)
        self.input1 = self.browser.find_element_by_css_selector(".first_block input.first")
        self.input1.send_keys("Ivan")
        self.input2 = self.browser.find_element_by_css_selector(".first_block input.second")
        self.input2.send_keys("Petrov")
        self.input3 = self.browser.find_element_by_css_selector(".first_block input.third")
        self.input3.send_keys("my_mail@mail.ru")
        self.input4 = self.browser.find_element_by_css_selector(".second_block input.first")
        self.input4.send_keys("my_number")
        self.input5 = self.browser.find_element_by_css_selector(".second_block input.second")
        self.input5.send_keys("my_address")
        self.button = self.browser.find_element_by_css_selector("button.btn")
        self.button.click()

        self.welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        self.welcome_text = self.welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == self.welcome_text

    def test_registration2(self):
        try:
            self.browser.get(self.link2)
            self.input1 = self.browser.find_element_by_css_selector(".first_block input.first")
            self.input1.send_keys("Ivan")
            self.input2 = self.browser.find_element_by_css_selector(".first_block input.second")
            self.input2.send_keys("Petrov")
            self.input3 = self.browser.find_element_by_css_selector(".first_block input.third")
            self.input3.send_keys("my_mail@mail.ru")
            self.input4 = self.browser.find_element_by_css_selector(".second_block input.first")
            self.input4.send_keys("my_number")
            self.input5 = self.browser.find_element_by_css_selector(".second_block input.second")
            self.input5.send_keys("my_address")
            self.button = self.browser.find_element_by_css_selector("button.btn")
            self.button.click()

            self.welcome_text_elt = self.browser.find_element_by_tag_name("h1")
            self.welcome_text = self.welcome_text_elt.text

            assert "Congratulations! You have successfully registered!" == self.welcome_text

        finally:
            time.sleep(2)


if __name__ == "__main__":
    unittest.main()
