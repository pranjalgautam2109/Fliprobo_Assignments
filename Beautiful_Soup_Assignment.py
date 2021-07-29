#!/usr/bin/env python
# coding: utf-8

# In[1]:


#all the header tags from ‘en.wikipedia.org/wiki/Main_Page’.
get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
from bs4 import BeautifulSoup
import requests
page=requests.get("https://en.wikipedia.org/wiki/Main_Page")
page


# In[5]:


soup=BeautifulSoup(page.content)
h=[]
header_tags=soup.find_all(['h1','h2','h3','h4','h5','h6'])
for i in header_tags:
    h.append(i.text.replace("\n",""))
    
h


# In[7]:


import pandas as pd
d1=pd.DataFrame({})
d1["header_tags"]=h
d1


# In[8]:


#program to display IMDB’s Top rated 100 movies’ data (i.e. Name, IMDB rating, Year of release).
page2=requests.get("https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc")
page2


# In[17]:


soup2=BeautifulSoup(page2.content)
top_100_movies=[]
top100=soup2.find_all('h3',"lister-item-header")
for i in top100:
    top_100_movies.append(i.text.replace("\n",""))
top_100_movies


# In[2]:



get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[3]:


#program to scrape cricket ratings for Men
from bs4 import BeautifulSoup
import requests
page5=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
soup5=BeautifulSoup(page5.content)


# In[56]:


matches=[]
points=[]
ratings=[]
xyz=[]

match=soup5.find_all('td', class_="rankings-block__banner--matches")
for i in match:
    matches.append(i.text)
random=[]
match2=soup5.find_all('td', class_="table-body__cell u-center-text")
for i in match2:
    random.append(i.text)
    
for i in range(0,len(random),2):
    matches.append(random[i])
    
point=soup5.find_all('td', class_="rankings-block__banner--points")
for i in point:
    points.append(i.text)

for i in range(1,len(random),2):
    points.append(random[i])
    
rating=soup5.find_all('td',class_="rankings-block__banner--rating u-text-right")
for i in rating:
    ratings.append(i.text.split())

rating2=soup5.find_all('td', class_="table-body__cell u-text-right rating")
for i in rating2:
    ratings.append(i.text)

teams=[]
random4=[]
team=soup5.find_all('span',"u-hide-phablet")
for i in team:
    random4.append(i.text)
for i in range(0,20):
    teams.append(random4[i])

rankings=[]
ranking=soup5.find_all('td', class_="rankings-block__banner--pos")
for i in ranking:
    rankings.append(i.text)
ranking2=soup5.find_all('td', class_="table-body__cell table-body__cell--position u-text-right")
for i in ranking2:
    rankings.append(i.text)

import pandas as pd

DF5=pd.DataFrame({})
DF5["Position"]=rankings
DF5["Team"]=teams
DF5["Matches"]=matches
DF5["Points"]=points
DF5["Rating"]=ratings
DF5


# In[89]:


#program to scrape cricket ratings for Women

page6=requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")
soup6=BeautifulSoup(page6.content)
matches2=[]
points2=[]
ratings2=[]
xyz2=[]

match2w=soup6.find_all('td', class_="rankings-block__banner--matches")
for i in match2w:
    matches2.append(i.text)
random2w=[]
match2w=soup6.find_all('td', class_="table-body__cell u-center-text")
for i in match2w:
    random2w.append(i.text)
    
for i in range(0,len(random2w),2):
    matches2.append(random2w[i])
    
point2=soup6.find_all('td', class_="rankings-block__banner--points")
for i in point2:
    points2.append(i.text)

for i in range(1,len(random2w),2):
    points2.append(random2w[i])
    
rating2w=soup6.find_all('td',class_="rankings-block__banner--rating u-text-right")
for i in rating2w:
    ratings2.append(i.text.split())

rating2w=soup6.find_all('td', class_="table-body__cell u-text-right rating")
for i in rating2w:
    ratings2.append(i.text)

teams2=[]
random4w=[]
team2=soup6.find_all('span',"u-hide-phablet")
for i in team2:
    random4w.append(i.text)
for i in range(0,10):
    teams2.append(random4w[i])

rankings2=[]
ranking2=soup6.find_all('td', class_="rankings-block__banner--pos")
for i in ranking2:
    rankings2.append(i.text)
ranking2w=soup6.find_all('td', class_="table-body__cell table-body__cell--position u-text-right")
for i in ranking2w:
    rankings2.append(i.text)

import pandas as pd

DF6=pd.DataFrame({})
DF6["Position"]=rankings2
DF6["Team"]=teams2
DF6["Matches"]=matches2
DF6["Points"]=points2
DF6["Rating"]=ratings2
DF6


# In[113]:


#program to scrape freshers job from internshal.com
page7=requests.get("https://internshala.com/fresher-jobs")
soup7=BeautifulSoup(page7.content)
job_title=[]
company=[]
ctc=[]
date=[]
t1=soup7.find_all('div',"heading_4_5 profile")
for i in t1:
    job_title.append(i.text.replace("\n",""))

t2=soup7.find_all('div',class_="heading_6 company_name")
for i in t2:
    company.append(i.text.replace("\n",""))
t3=soup7.find_all('div',class_="item_body")
x=[]
for i in t3:
    x.append(i.text)
for i in range(1, len(x),3):
    ctc.append(x[i].replace("\n",""))
for i in range(2, len(x),3):
    date.append(x[i].replace("\n",""))
date
DF7=pd.DataFrame({})
DF7["Job Title"]=job_title
DF7["Company"]=company
DF7["CTC"]=ctc
DF7["date"]=date
DF7


# In[125]:


#Program to scrape house details from nobroker.com
page10=requests.get("https://www.nobroker.in/property/sale/noida/multiple?searchParam=W3sibGF0IjoyOC42Mjc5ODEsImxvbiI6NzcuMzY0ODU2NywicGxhY2VJZCI6IkNoSUpuMjN6YmtYbEREa1J5RFpoS0xHUmNUcyIsInBsYWNlTmFtZSI6IlNlY3RvciA2MiJ9LHsibGF0IjoyOC41Njk1ODY3LCJsb24iOjc3LjM4MjUxODUsInBsYWNlSWQiOiJDaElKbDRLUFpsN3ZERGtSZzJ2VDBxZ0V5VjQiLCJwbGFjZU5hbWUiOiJTZWN0b3IgNzYifSx7ImxhdCI6MjguNTcwMzE3LCJsb24iOjc3LjMyMTgxOTYsInBsYWNlSWQiOiJDaElKRDBlaExFX2tERGtSTTdTX2JGdVFfNHciLCJwbGFjZU5hbWUiOiJTZWN0b3IgMTgifV0=&radius=2.0")
soup10=BeautifulSoup(page10.content)
name=[]
loc=[]
area=[]
emi=[]
price=[]
t1=soup10.find_all('h2', class_="heading-6 font-semi-bold nb__1AShY")
for i in t1:
    name.append(i.text)
t2=soup10.find_all('div', "nb__2CMjv")
for i in t2:
    loc.append(i.text)
t3=soup10.find_all('div', "font-semi-bold heading-6")
y=[]
for i in t3:
    y.append(i.text)
for i in range(1,len(y),3):
    emi.append(y[i])
for i in range(0,len(y),3):
    area.append(y[i])
for i in range(2,len(y),3):
    price.append(y[i])
DF10=pd.DataFrame({})
DF10["Property Name"]=name
DF10["Locality"]=loc
DF10["Area"]=area
DF10["Price"]=price
DF10["EMI"]=emi
DF10


# In[138]:


#Program to scrape 7 days forecast of San Francisco
page8=requests.get("https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.YQLoZ70zbIU")
soup8=BeautifulSoup(page8.content)
time=[]
temp=[]
description=[]
t1=soup8.find_all('p',class_="period-name")
for i in t1:
    time.append(i.text)
t2=soup8.find_all('p',class_="temp temp-high")
for i in t2:
    temp.append(i.text)
t4=soup8.find_all('p',class_="temp temp-low")
for i in t4:
    temp.append(i.text)
t3=soup8.find_all('p',class_="short-desc")
for i in t3:
    description.append(i.text)
DF8=pd.DataFrame({})
DF8["Time Period"]=time
DF8["temp"]=temp
DF8["Description"]=description
DF8


# In[148]:


#Program to scrape top 100 Indian Movies
page3=requests.get("https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=461131e5-5af0-4e50-bee2-223fad1e00ca&pf_rd_r=6N76HQ6YH02Q634HDD80&pf_rd_s=center-1&pf_rd_t=60601&pf_rd_i=india.toprated&ref_=fea_india_ss_toprated_india_tr_india250_sm")
soup3=BeautifulSoup(page3.content)
name=[]
rating=[]
year=[]
t1=soup3.find_all('td', class_="titleColumn")
for i in t1:
    for j in i.find_all('a'):
        name.append(j.text)
t2=soup3.find_all('td', class_="ratingColumn imdbRating")
for i in t2:
    rating.append(i.text.replace("\n",""))
t3=soup3.find_all('span', class_="secondaryInfo")
for i in t3:
    year.append(i.text)
DF3=pd.DataFrame({})
DF3["Movie"]=name
DF3["IMDB Rating"]=rating
DF3["Year of Release"]=year
DF3


# In[ ]:




