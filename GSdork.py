import time
import requests
from bs4 import BeautifulSoup
import threading


# ---------------- Esc/Results=10 ----------------

EXIT_COMMAND = "esc"
DEFAULT_RESULTS = 10

# ---------------- Colors To Be Defined ----------------

Yellow = "\033[1;33;40m"
Red = "\033[1;31;40m"
Normal = "\033[0;0m"
BM = "\033[1;35;40m"

# ---------------- Banner Show ----------------
def Banner_Show():
    print(f'''
|  _____  |{Yellow}A{Normal}
| |\ ___| | {Red}D{Normal}
| | |   | | K
| | |___| | {BM}A{Normal}
\ | |____\| L
 \|_________I 
GoogleDorkQuery
    ''')

Banner_Show()
time.sleep(1.5)
# ---------------- Examples Of Operators ----------------
def G_Examples():
    print(f'''
{Red}Operators Examples{Normal}
>> site: [exmaple.com] filetype:[pdf]
>> inurl:[cyber] inbody [threat]
>> passwords filetype[docx] site:[example.com]
>> allintext:hacking
>> how to * website [ '*' used to search pages contains anything before your word ]
>> allintext:username filetype:log
    ''')


G_Examples()

# ---------------- Function taking search query, numbers of results ----------------
def GetSearchResult(search_query, num_results=DEFAULT_RESULTS):
    total = 0
    payload = f"q={search_query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582",
        "Method": "GET"
    }
    url = f"https://www.google.co.il/search?{payload}&num={num_results}"
    r = requests.get(url, params=headers)
    if r.status_code != 200:
        print("Something went wrong, please try again...")
        return

    # ---------------- Start The Magic ----------------
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.findAll("a", href=True)
    for link in links:
        try:
            link_href = link.get("href")
            if "url?q=" in link_href and not "webcache" in link_href:
                split_links = link_href.split("/url?q=")
                total += 1
                print(f"{total}>> {split_links[1].split('&sa=U')[0]}")
                #time.sleep(0.5)
        except Exception:
            print("An error occurred, please try again...")
    print(f"{Yellow}Results: Total of {total} URLS were found.{Normal}")

while True:
    search_query = input(f"Search Query ('{Yellow}{EXIT_COMMAND}{Normal}' for exit): ")
    if search_query == EXIT_COMMAND:
        break
    try:
        Num_Results = int(input("Results As Possible (Default is 10): "))
    except ValueError:
        Num_Results = DEFAULT_RESULTS
    s_thread = threading.Thread(target=GetSearchResult, args=(search_query, Num_Results))
    #START/JOIN
    s_thread.start()
    s_thread.join()
