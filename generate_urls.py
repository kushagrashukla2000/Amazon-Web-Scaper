from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import config


def generate_urls():
    config.load_config()
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0")
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    url = "https://www.amazon.in/s?k=" + config.CONFIG["product"]

    driver.get(url)

    time.sleep(6)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    links = soup.select("div.s-title-instructions-style a")

    hrefs = []

    for a in links:
        hrefs.append("https://www.amazon.in" + a.get("href"))

    driver.quit()

    return hrefs