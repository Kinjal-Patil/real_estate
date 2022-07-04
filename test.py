import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

url = "https://cleartax.in/s/chapter-72-iron-steel-gst-rate-hsn-code"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find("table")
tab_data = [[cell.text for cell in row.find_all(["th", "td"])]
            for row in table.find_all("tr")]
df = pd.DataFrame(tab_data)

df.to_excel('raw_data.xlsx', index=False, header=False)

