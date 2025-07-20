import requests
import pandas
from bs4 import BeautifulSoup
#imbd website link
link="https://www.imdb.com/chart/top/"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(link,headers=headers)
print(response)

#information of the website
inf=BeautifulSoup(response.content,'html.parser')
print(inf.text)

#names of movies
names=inf.find_all('h3',class_="ipc-title__text ipc-title__text--reduced")
name=[]
for i in names[1:21]:
    n=i.get_text()
    name.append(n)
print(name)

#year of relase and duration
years=inf.find_all('div',class_="sc-29531a57-7 hpTDgy cli-title-metadata")
year=[]
for i in years[1:21]:
    y=i.get_text()
    year.append(y)
print(year)

#ratings
ratings=inf.find_all('span',class_="ipc-rating-star--rating")
rating=[]
for i in ratings[1:21]:
    r=i.get_text()
    rating.append(r)
print(rating)

#storing in csv file using pandas and date frame
data={'names of movies':name,'year of release and duration':year,'ratiings':rating}
store=pandas.DataFrame(data)
print(store)
store.to_csv("imbd_scraping_data.csv")