# Web Scraping Using Python

## Requests

```python
import requests

URL = 'https://www.google.com'
text = requests.get(URL).text # html code
```

## BeautifulSoup

```python
import requests
from bs4 import BeautifulSoup

URL = 'https://www.google.com'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
```