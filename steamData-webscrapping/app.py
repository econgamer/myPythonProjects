import requests
from bs4 import BeautifulSoup
import pandas

l = []
base_url = "http://store.steampowered.com/search/?os=win&specials=1&page="

r = requests.get(base_url)
c = r.content

soup = BeautifulSoup(c, "html.parser")
page_nr = soup.find_all("div",{"class":"search_pagination_right"})
page_nr_a = page_nr[0].find_all("a")

NumberOfPage = page_nr_a[-2].text


for page in range(1, int(NumberOfPage)+1):
    r = requests.get(base_url + str(page) + ".html")
    c = r.content

    soup = BeautifulSoup(c, "html.parser")



    all = soup.find_all("div",{"id":"search_result_container"})
    all2 = all[0].find_all("a")

    ItemList = soup.find_all("div", {"class": "responsive_search_name_combined"})


    for item in ItemList:
        d={}
        try:
            price_list = item.find_all("div", {"class":"col search_price discounted responsive_secondrow"})[0].text
            a, d["originalPrice"], d["discountedPrice"] = price_list.split("HK$")
            d["originalPrice"] = d["originalPrice"].rstrip()
            d["discountedPrice"] = d["discountedPrice"].rstrip()

        except:
            print(None)

        try:
            d["discountRate"] = item.find_all("div", {"class":"col search_discount responsive_secondrow"})[0].text
            d["discountRate"] = d["discountRate"].rstrip()
            a, d["discountRate"] = d["discountRate"].split("\n-")


        except:
            print(None)
        try:
            d["productName"] = item.find_all("div", {"class":"col search_name ellipsis"})[0].text
            d["productName"] = d["productName"].rstrip()
            a, d["productName"] = d["productName"].split("\n")
        except:
            print(None)

        print(" ")

        l.append(d)


df = pandas.DataFrame(l)
print(df)
df.to_csv("Output.csv")
