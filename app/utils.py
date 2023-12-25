from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException


def get_element_text(driver, selector):
    return WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector))).text.strip()


def process_product(product_url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--pageLoadStrategy=normal')

    driver = webdriver.Chrome(options=chrome_options)


    try:
        driver.get(product_url)

        product_name = get_element_text(driver, 'h1[data-test-id="text__product-name"]')
        price_text = get_element_text(driver, 'div.price div.new-price')
        old_price_text = get_element_text(driver, 'span.currency.old-price')
        total_price_text = get_element_text(driver, 'div.total-price span.currency')

        result = f"Заголовок товара: {product_name}\nСтоимость товара: {price_text}\nСтарая цена: {old_price_text}\nИтоговая цена: {total_price_text}\n---"
        return result, None
    except WebDriverException as wde:
        return None, f"Error processing product URL {product_url}"

    finally:

        driver.quit()
