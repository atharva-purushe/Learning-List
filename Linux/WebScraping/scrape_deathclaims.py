from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://economictimes.indiatimes.com/wealth/insure/life-insurance/latest-life-insurance-claim-settlement-ratio-of-insurance-companies-in-india/articleshow/97366610.cms"

source =requests.get(url)
soup = BeautifulSoup(source.text, 'lxml')

tables = soup.find_all('table')
table = tables[1]
# print(table.prettify()[:1000])

rows=table.find_all('tr')
header_tags = rows[1].find_all('td')
headers = [header.text.strip() for header in header_tags]
# print(headers)

data =[]
for row in rows[2:]:
    cells=row.find_all("td")
    row_data=[cell.text.strip() for cell in cells]
    if row_data:
        data.append(row_data)
# print(data)

df = pd.DataFrame(data, columns = headers)
# print(df)
df = df.sort_values('% No. of claims paid', ascending=False)
# df= df.reset_index()
print(df)
# print(df.columns.tolist())
df.to_csv("Death_Claims.csv")
