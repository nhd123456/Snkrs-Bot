import sys
import json
import os
from operation import run
from selenium import webdriver

if __name__ == "__main__":

    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--url", required=True)
    parser.add_argument("--shoe-size", default=None)
    parser.add_argument("--login-time", default=None)
    parser.add_argument("--release-time", default=None)
    parser.add_argument("--screenshot-path", default=None)
    parser.add_argument("--html-path", default=None)
    parser.add_argument("--page-load-timeout", type=int, default=2)
    parser.add_argument("--driver-type", default="firefox", choices=("firefox", "chrome"))
    parser.add_argument("--headless", action="store_true")
    parser.add_argument("--select-payment", action="store_true")
    parser.add_argument("--purchase", action="store_true")
    parser.add_argument("--num-retries", type=int, default=1)
    parser.add_argument("--dont-quit", action="store_true")
    parser.add_argument("--shoe-type", default="M", choices=("M", "W", "Y", "C", "XXS", "XS", "S", "L", "XL"))
    parser.add_argument("--shipping-option", default="STANDARD", choices=("STANDARD", "TWO_DAY", "NEXT_DAY"))
    parser.add_argument("--cvv", default=None)
    parser.add_argument("--shipping-address", default=None)
    parser.add_argument("--webdriver-path", required=False, default=None)
    args = parser.parse_args()
    '''

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
