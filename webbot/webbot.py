import os

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0



class Webbot:

    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        driver_dir = os.path.join(base_dir, 'drivers', 'chromedriver')
        try:
            self.driver = webdriver.Chrome(driver_dir)
        except:
            print('Unable to create a new browser session.')
            raise Exception
    
    def open_page(self, url):
        self.driver.get(url)
    
    def fill_text(self):
        pass
    
    def click(self):
        pass
    
    def quit(self):
        try:
            self.driver.quit()
            print('Session successfully terminated.')
        except Exception:
            print('Error quitting browser session.')



if __name__ == '__main__':

    import time
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    driver_dir = os.path.join(base_dir, 'drivers', 'chromedriver')
    print('Selenium powered Webbot\n',
          '__file__ = ', __file__,
          '\nbase_dir = ', base_dir,
          '\ndriver_dir = ', driver_dir, sep='')
          
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(driver_dir)

    # go to the google home page
    driver.get("http://www.google.com")

    # the page is ajaxy so the title is originally this:
    print(driver.title)

    # find the element that's name attribute is q (the google search box)
    inputElement = driver.find_element_by_name("q")

    # type in the search
    inputElement.send_keys("cheese!")

    # submit the form (although google automatically searches now without submitting)
    inputElement.submit()

    try:
        # we have to wait for the page to refresh, the last thing that seems
        #to be updated is the title
        WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

        # You should see "cheese! - Google Search"
        print(driver.title)

    finally:
        time.sleep(5)
        driver.quit()
        print('Success!')



