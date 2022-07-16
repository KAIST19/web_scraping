import requests

url = input("Enter a URL: ")
html = requests.get(url).text

print(html)