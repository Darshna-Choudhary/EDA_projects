# IMDb Top 250 Movies — Web Scraping & Exploratory Data Analysis

## Project Objective

This project was created **primarily to practice real-world web scraping** and to understand how scraped data can be cleaned, analyzed, and visualized using Python.
The goal was **not to build a predictive model**, but to gain hands-on experience with:

* scraping a modern, JavaScript-rendered website
* handling messy real-world data
* asking meaningful analytical questions
* deriving data-backed insights

---

## Data Source

* **Website:** IMDb
* **Page Scraped:** IMDb Top 250 Movies
* **URL:** [https://www.imdb.com/chart/top/](https://www.imdb.com/chart/top/)

IMDb was chosen because it represents a realistic scraping challenge due to:

* dynamic content loading
* bot-protection against simple HTTP requests

---

## Tools & Libraries Used

* **Selenium** – to load JavaScript-rendered content in a real browser
* **BeautifulSoup (bs4)** – to parse and extract data from rendered HTML
* **Pandas** – for data cleaning and analysis
* **Matplotlib** – for data visualization

---

## Project Structure

```
IMDb_movie_scrap/
│
├── scraper.py        # Selenium + BeautifulSoup script for scraping IMDb Top 250
├── analysis.py       # Data cleaning, analysis, and visualization logic
├── README.md         # Project documentation
│
├── data/
│   ├── movies.html   # Rendered IMDb HTML saved for inspection/debugging
│   └── movies.csv    # Cleaned dataset extracted from IMDb
```

---

## Data Collected

For each movie in the IMDb Top 250 list:

* Rank
* Title
* Release Year
* Duration
* IMDb Rating
* Number of Votes

---

## Key Analysis Questions

1. **Rating Distribution**

   * Are IMDb Top 250 movies clustered around high ratings?
   * Is the distribution skewed?

2. **Votes vs Rating**

   * Do higher-rated movies always receive more votes?
   * Are there high-rating, low-vote outliers?

3. **Rank vs Rating**

   * Does IMDb rank strictly follow rating?
   * Are there anomalies due to other ranking factors?

4. **Old vs New Movies**

   * Do older movies dominate the Top 250 list?
   * How does movie count vary across decades?

---

## Key Insights

* IMDb Top 250 ratings are **tightly clustered between 8.0 and 9.0**, reflecting strong selection bias.
* The rating distribution is **left-skewed**, with very few movies achieving exceptionally high ratings.
* Higher popularity (votes) does **not guarantee higher ratings**; the relationship is weakly positive.
* IMDb rank generally follows ratings but is **not strictly determined by them**, indicating the influence of IMDb’s weighted ranking algorithm.
* Movies from the **1990s and 2000s dominate** the list, while classic films still maintain a significant presence.

---

## Limitations

* Data is limited to a **single IMDb page snapshot**.
* No genre-level or country-level analysis was performed.
* IMDb ranking logic is proprietary, so conclusions about ranking factors are inferential.

---

## Future Improvements

* Extend scraping to include genres and directors
* Compare IMDb Top 250 with other ranking platforms
* Track changes over time by scraping periodically
* Add interactive visualizations

---

## Why This Project Matters

This project demonstrates:

* Practical web scraping beyond basic `requests`
* Handling JavaScript-rendered websites
* Clean separation between scraping and analysis
* Data-driven reasoning rather than assumptions

It serves as a **foundation project** before moving on to more complex scraping and analytical tasks.