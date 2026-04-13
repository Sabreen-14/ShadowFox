from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url = input("Enter website URL: ")

try:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req)
    html = response.read()

    soup = BeautifulSoup(html, "html.parser")

    print("\nPage Title:", soup.title.string)

    print("\nHeadings:")
    for tag in soup.find_all(['h1', 'h2', 'h3']):
        print(tag.get_text())

except Exception as e:
    print("Error:", e)
