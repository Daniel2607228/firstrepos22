
'''import urllib.request

opener = urllib.request.build_opener()
response = opener.open("https://httpbin.org/")

print(response.read())

import requests
response = requests.get("https://httpbin.org/")

print(response.content)

import requests
response = requests.post("https://httpbin.org/post", data = "Test data", headers = {"h1":"Test title"})

print(response.text)'''

import requests
res_parse_list=[]

response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                res_parse_list.append(parse_elem_2)

bitcoin = res_parse_list[0]
eth = res_parse_list[1]
the = res_parse_list[2]
print("******* CryptoMarket *******")
print("")
ques = input("Currency(eth, bit, tet): ")
def market():
    if ques == "eth":
        print(f"Ethereum price- {eth}")
    elif ques == "bit":
        print(f"Bitcoin price- {bitcoin}")
    elif ques == "tet":
        print(f"Tether price- {the}")
    else:
        print("Unknown Currency!")

market()
ans = input("Continue?: ")

while ans == "yes":
    ques = input("Currency(eth, bit, tet): ")
    market()
    if ans == "no":
        print("Have a good day!")
        break

'''from bs4 import BeautifulSoup
import requests

response = requests.get("https://coinmarketcap.com/")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")

    soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/markets/"})
    #for elem in soup_list:
    #    print(elem)
    res = soup_list[0].find("span")
    print(res.text)'''




