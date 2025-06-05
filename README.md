# 📰 Tech News Scraper

A Python-based web scraper that extracts the latest technology news articles from [TechCrunch](https://techcrunch.com) and [Y Combinator's Hacker News](https://news.ycombinator.com). The scraped data is stored in JSON format for further analysis or integration.

## 🚀 Features

- **Automated Browsing**: Utilizes Selenium WebDriver for dynamic content handling.
- **Multi-Source Scraping**: Targets both TechCrunch and Y Combinator's Hacker News.
- **Structured Data Output**: Saves scraped articles in JSON files.
- **Modular Design**: Separate scraper modules for each news source.
- **Environment Configuration**: Supports `.env` files for managing environment variables.

## 🛠️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Anirudh808/tech_news_scraper.git
   cd tech_news_scraper
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory to store any necessary environment variables. For example:
   ```env
   # .env
   # Add your environment variables here
   ```

## 🖥️ Usage

Run the main script to start scraping:
```bash
python run_scrapers.py
```

This will execute the scraping modules for both TechCrunch and Y Combinator, saving the results to:
- `scraped_data_tech_crunch.json`
- `scraped_data_ycombinator.json`

## 📁 Project Structure

```
tech_news_scraper/
├── app.py
├── driver.py
├── run_scrapers.py
├── techcrunch_scraper.py
├── ycombinator_scraper.py
├── requirements.txt
├── .env
├── scraped_data_tech_crunch.json
├── scraped_data_ycombinator.json
└── __pycache__/
```

- `app.py`: Main application logic.
- `driver.py`: Initializes and manages the Selenium WebDriver.
- `run_scrapers.py`: Orchestrates the scraping process.
- `techcrunch_scraper.py`: Scraper module for TechCrunch.
- `ycombinator_scraper.py`: Scraper module for Y Combinator.
- `requirements.txt`: Lists project dependencies.
- `.env`: Stores environment variables.
- `scraped_data_*.json`: Output files containing scraped data.

## ✅ Requirements

- Python 3.x
- Google Chrome browser
- ChromeDriver compatible with your Chrome version
- Selenium

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🙋‍♂️ Author

Developed by [Anirudh808](https://github.com/Anirudh808).
