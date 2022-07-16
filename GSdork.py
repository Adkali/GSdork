import datetime
import time
import requests
from bs4 import BeautifulSoup
import sys

# Colors
Yellow = "\033[1;33;40m"
Red = "\033[1;31;40m"
Normal = "\033[0;0m"
BM = "\033[1;35;40m"


# Banner Call
def BannerShow():
    print(f'''
|  _____  |{Yellow}A{Normal}
| |\ ___| | {Red}D{Normal}
| | |   | | K
| | |___| | {BM}A{Normal}
\ | |____\| L
 \|_________I 

    ''')


BannerShow()


def G_Example():
    print(f'''
{Red}Operators Examples{Normal}
>> site: [exmaple.com] filetype:[pdf]
>> inurl:[cyber] inbody [threat]
>> passwords filetype[docx] site:[example.com]
>> allintext:hacking
>> how to * website [ '*' used to search pages contains anything before your word ]
>> allintext:username filetype:log
    ''')


G_Example()

while True:
    total = 0
    Payload = input(f"Search Query ('{Yellow}esc{Normal}' for exit): ")  # Search
    if Payload == "esc":
        break
    R_Number = input("Results As Possible (Default is 10): ")  # Results as number
    Default = "10"
    Payloads = f"q={Payload}"

    Headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582",
        "Method": "GET"
    }
    if R_Number == Default:
        URL = f"https://www.google.co.il/search?{Payloads}&num=10"
    else:
        URL = f"https://www.google.co.il/search?{Payloads}&num={R_Number}"
    r = requests.get(URL, params=Headers)
    H = r.headers
    for keys, values in r.headers.items():
        print(f"{keys},{values}")
    if r.status_code == 200:
        print(f"Status code:{r.status_code} - Success!\n")
        time.sleep(2)
    else:
        print("Something went wrong, please try again...")
        time.sleep(2)
        break
    # Using BeautifulSoup for parsing tags inside source
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.findAll("a", href=True)
    for link in links:
        try:  # Get links, split them and use indexed
            LinkHref = link.get("href")  # Href tags
            if "url?q=" in LinkHref and not "webcache" in LinkHref:  # using if statment on 'url?q='
                SplitLinks = LinkHref.split("/url?q=") # Split if does
                total += 1
                print(f"{total}>> {SplitLinks[1].split('&sa=U')[0]}")  # Split again, show only links [ index 0 ]
                time.sleep(0.5)
                print(f"{Yellow}Results: Total of {total} URLS were found.{Normal}")

        except KeyboardInterrupt:
            print("User stopped process, exit...")
            exit()

        except IndexError:
            if IndexError:
                break
            print("Out of range, try again please...")
