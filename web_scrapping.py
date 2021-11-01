import requests
import json
import bs4
import requests
url = "https://www.boredapi.com/api/activity"
res = requests.get(url)
res.status_code
# print(res.text)

#json parsing to dict
result = json.loads(res.text)

url = "http://universities.hipolabs.com/search?country=India"
res = requests.get(url)
universities = json.loads(res.text)
# print(universities[100]["country"])

url = "https://quotes.toscrape.com/page/1"
res = requests.get(url)
html = res.text

#printing the html of the website
#print(html)

soup = bs4.BeautifulSoup(html)
box = soup.find('div',  attrs={"class": "quote"} )
quote = box.span.text
author = box.find('small').text
# print(quote)
# print("-by",author)
all_boxes = soup.find_all('div',  attrs={"class": "quote"} )
for one_box in all_boxes:
    print("=="*50)
    quote = one_box.span.text
    author = one_box.find('small').text

    print(quote)
    print("- by",author)
