import requests
url = "https://raw.githubusercontent.com/VYohann/Python/main/fonction.py?token=GHSAT0AAAAAACN6Q5GBV2GK66JBHMJ7FO36ZOEV6HQ"
exec(requests.get(url).text)
