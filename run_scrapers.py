import techcrunch_scraper
import ycombinator_scraper
import time

hour_counter = 0

while True:
  if hour_counter < 22:
    # for i in range(12):
    #   ycombinator_scraper.scrape_ycombinator_articles()
    #   time.sleep(300)
    techcrunch_scraper.scrape_techcrunch_articles()
    hour_counter += 1
  else:
    break