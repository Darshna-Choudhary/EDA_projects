from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)

url = "https://m.imdb.com/chart/top/"
driver.get(url)
time.sleep(5)
html = driver.page_source
with open("data/movies.html", "w", encoding = "utf-8") as f:
    f.write(html)
driver.quit()

soup = BeautifulSoup(html, "html.parser")
movies = soup.find_all("li",class_="ipc-metadata-list-summary-item")
data = []

for movie in movies:
    rank = int(movie.select_one("div.ipc-signpost__text").text.split("#")[1])
    title = movie.find("h3").text
    metadata = movie.select_one("div.sc-b4f120f6-6.kprlzj.cli-title-metadata")
    if not metadata:
        continue
    items = metadata.select("span.sc-b4f120f6-7.hoOxkw.cli-title-metadata-item")
    year = items[0].text.strip() if len(items) > 0 else None
    duration = items[1].text.strip() if len(items) > 1 else None
    ratings = movie.select_one("span.ipc-rating-star--rating").text
    votes = movie.select_one("span.ipc-rating-star--voteCount").text.split("(")[1].split(")")[0]
    data.append({
        "Rank" : rank,
        "Title" : title,
        "Year" : year,
        "Duration" : duration,
        "Ratings" : ratings,
        "Votes" : votes
    })

df = pd.DataFrame(data)
df.to_csv("data/movies.csv", index = False)