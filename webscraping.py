import requests
import pandas
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/search?q=iphone+13&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_4_4_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_4_na_na_na&as-pos=4&as-type=RECENT&suggestionId=iphone+13&requestId=47340e10-c785-44ba-a1c9-c0b13d1b418b&as-searchtext=ipho")
# print(response)

soup=BeautifulSoup(response.content, 'html.parser')
# print("soup")

names=soup.find_all("div",class_="_4rR01T")
name=[]
for i in names[0:10]:
    d=i.get_text()
    name.append(d)
# print(name)

ratings=soup.find_all("div",class_="_3LWZlK")
rate=[]
for i in ratings[0:10]:
    d=i.get_text()
    rate.append(float(d))
# print(rate)

reviews=soup.find_all("span",class_="_2_R_DZ")
review=[]
for i in reviews[0:10]:
    d=i.get_text()
    review.append(d)
# print(review)

prices=soup.find_all("div",class_="_30jeq3 _1_WHN1")
price=[]
for i in prices[0:10]:
    d=i.get_text()
    price.append(d)
# print(price)

features=soup.find_all("div",class_="fMghEO")
feature=[]
for i in features[0:10]:
    d=i.get_text()
    feature.append(d)
# print(feature)

links=soup.find_all("a",class_="_1fQZEK")
link=[]
for i in links[0:10]:
    d="https://www.flipkart.com"+i['href']
    link.append(d)
# print(link)

images=soup.find_all("img",class_="_396cs4")
image=[]
for i in images[0:10]:
    d=i['src']
    image.append(d)
# print(image)

data={
    "Names":name,
    # in incase we get error here use this:"Names":pandas.Series(name)
    "Price":price,
    "Ratings":rate,
    "Reviews":review,
    "Images":image,
    "links":link,
    "Features":feature
}

# print(data)

df = pandas.DataFrame(data)
# print(df)
df.to_csv("Iphone 13 Models.csv")