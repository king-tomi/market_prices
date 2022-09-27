from typing import Dict, Union
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import logging

logging.basicConfig(filename="debug.log", filemode = "a",format = '%(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)


def get_page(url: str) -> Union[BeautifulSoup, None]:
    try:
        req = requests.get(url=url, stream=True)
        if req.status_code == 200:
            soup = BeautifulSoup(req.content, 'html.parser')
            logging.info(f"Successful with status code {req.status_code}")
            return soup
        return None
    except requests.RequestException as e:
        logging.error(f"Error occured {e}")
        return None

def get_page_selenium(url: str):
    try:

        chrome = webdriver.Chrome()
        chrome.maximize_window()
        chrome.get(url=url)
        return chrome
    except Exception:
        logging.error(f"Selenium connection - {logging.ERROR} - Error trying to connect to Selenium")
        return None

def scrape(url: str) -> Union[Dict[str, str], None]:
    """
    scrapes the page for prices of commodities
    
    :input -> url: a `str` object. the link of the site to scrape

    :returns -> a `Dictionary` that contains the name of the product and the associated prices
    """
    target = ["Tomatoes", "Rice", "Maize", "Beans", "Onions"]
    res = {}
    soup = get_page(url)
    if soup is not None:
        price_list = soup.find_all("li")
        new = [li.text for li in price_list]
        for t in target:
            temp = []
            for n in new:
                if t in n:
                    temp.append(n)
            res[t] = temp
        return res