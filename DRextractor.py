from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def open_and_save_urls(search_url, output_file):
    driver = webdriver.Chrome()
    print("DRextractor Start........................................ + BY Uday Patel")

    try:
        driver.get(search_url)
        time.sleep(10)
        result_urls = [a.get_attribute("href") for a in driver.find_elements(By.CSS_SELECTOR, 'h2 a')]
        filtered_urls = [url for url in result_urls if "/mobiledoc/jsp/" in url]
        with open(output_file, "a") as file:
            for url in filtered_urls:
                file.write(url + "\n")

        print(f"Filtered URLs saved to {output_file}")

 
        for value in range(11, 92, 10):
            updated_url = search_url.replace("first=1", f"first={value}")
            driver.execute_script(f"window.open('{updated_url}', '_blank');")
            time.sleep(10)
            result_urls = [a.get_attribute("href") for a in driver.find_elements(By.CSS_SELECTOR, 'h2 a')]
            filtered_urls = [url for url in result_urls if "/mobiledoc/jsp/" in url]
            with open(output_file, "a") as file:
                for url in filtered_urls:
                    file.write(url + "\n")

            print(f"ALL URLs saved to {output_file}")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    finally:
        driver.quit()

search_url = "https://www.bing.com/search?q=allinurl%3a%2fmobiledoc%2fjsp+site%3aecwcloud.com&qs=n&sp=-1&lq=0&pq=allinurl%3a%2fmobiledoc%2fjsp+site%3aecwcloud.com&sc=2-41&sk=&cvid=5EE7CCB496ED49A499B43A8B0747D1D8&ghsh=0&ghacc=0&ghpl=&FPIG=718C811DA9C54B6C9D7A8669DAF9B372&first=1&FORM=PERE"
output_file = "filtered_bing_search_results.txt"

open_and_save_urls(search_url, output_file)
