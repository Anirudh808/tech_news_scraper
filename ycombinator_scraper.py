from driver import SeleniumDriver
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json

driver = SeleniumDriver()

# Configure logging for better feedback
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_ycombinator_articles():
    """
    Navigates to Ycombinator news and scrapes article titles and links.
    Assumes the driver is already initialized.
    """
    url = "https://news.ycombinator.com/newest"
    logging.info(f"Navigating to {url}")
    driver.driver.get(url)

    try:
        # Use explicit wait to ensure elements are loaded before trying to find them
        logging.info("Waiting for articles to load...")
        WebDriverWait(driver.driver, 20).until(
            EC.presence_of_all_elements_located((By.ID, "hnmain"))
        )
        logging.info("Articles located.")

        articles = driver.driver.find_elements(By.CSS_SELECTOR, "#hnmain > tbody > tr:nth-child(3) > td > table > tbody > tr.athing.submission")
        if not articles:
            logging.warning("No articles found with the specified selector. Check the website's HTML.")
            return []

        scraped_data = []
        for article in articles:
          try:
              title_element = article.find_elements(By.CSS_SELECTOR, "td.title > span.titleline > a")
              if title_element:
                  title = title_element[0].text
                  link = title_element[0].get_attribute("href")
                  scraped_data.append({"title": title, "link": link})
                  logging.info(f"Found article: {title} - {link}")
              else:
                  logging.warning("Article without a valid title/link structure found.")
          except Exception as e:
              logging.warning(f"Could not extract title/link for an article: {e}")

        with open("scraped_data_ycombinator.json", "w") as file:
            file.write(json.dumps(scraped_data))
        return scraped_data

    except Exception as e:
        logging.error(f"Error during scraping YCombinator: {e}")
        return []
    