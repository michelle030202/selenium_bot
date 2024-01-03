"""
Automation script using Selenium for interacting with the Bootswatch website.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Bot:
    """
    A class to automate interactions with the Bootswatch website using Selenium.
    """
    def __init__(self):
        """
        Initializes the Chrome WebDriver and navigates to the Bootswatch default page.
        """
        self.driver = webdriver.Chrome()
        self.driver.get("https://bootswatch.com/default/")

    def login(self, email, password):
        """
        Enters email and password into the login form.

        Args:
            email (str): Email to be entered in the email input field.
            password (str): Password to be entered in the password input field.
        """
        email_bar_element = self.driver.find_element(By.ID, "exampleInputEmail1")
        email_bar_element.send_keys(email)
        password_bar_element = self.driver.find_element(By.ID, "exampleInputPassword1")
        password_bar_element.send_keys(password)

    def select_option(self, option):
        """
        Selects an option from the dropdown.

        Args:
            option (str): The text of the option to be selected from the dropdown.
        """
        wait = WebDriverWait(self.driver, 10)
        dropdown = wait.until(EC.element_to_be_clickable((By.ID, "exampleSelect1")))
        select = Select(dropdown)
        select.select_by_visible_text(option)
        selected_option = select.first_selected_option.text
        assert selected_option == "2", f"Option {option} was not selected"

    def close_browser(self):
        """
        Closes the Chrome WebDriver and quits the browser.
        """
        self.driver.quit()


if __name__ == "__main__":
    bot = Bot()
    bot.login("michelle030202@gmail.com", "123456")
    bot.select_option("2")
    bot.close_browser()
