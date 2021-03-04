import json
import os
from operation import run
from selenium import webdriver

if __name__ == "__main__":

    ''' pass in parameters '''
    username = 'nhd123456ekek@gmail.com'
    password = '5387Ekek'
    url = 'https://www.nike.com/tw/launch/t/womens-air-max-viva-wheat'
    options = webdriver.FirefoxOptions()
    headless = False
    if headless:
        options.add_argument("--headless")

    webdriver_path = 'C:/Users/Kenny/Desktop/geckodriver.exe'  # path to gickodriver
    executable_path = webdriver_path
    driver = webdriver.Firefox(executable_path=executable_path, firefox_options=options, log_path=os.devnull)

    shoe_type = 'CM'  # default="M", choices=("M", "W", "Y", "C", "XXS", "XS", "S", "L", "XL")
    shoe_size = '23'
    shipping_address = None  # json.loads()
    shipping_option = 'STANDARD'  # STANDARD, TWO_DAY or NEXT_DAY
    screenshot_path = None
    select_payment = False
    purchase = False
    num_retries = None
    dont_quit = False
    cvv = None
    page_load_timeout = 2

    run(
        driver=driver, shoe_type=shoe_type, username=username, password=password, url=url,
        shoe_size=shoe_size, shipping_option=shipping_option, shipping_address=shipping_address,
        screenshot_path=screenshot_path, select_payment=select_payment, page_load_timeout=page_load_timeout,
        purchase=purchase, num_retries=num_retries, dont_quit=dont_quit, cvv=cvv
    )
