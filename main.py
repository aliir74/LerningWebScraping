import urllib.request
from bs4 import BeautifulSoup

url = "http://www.morganbrown.com/attorneys/index.php"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

print(soup.prettify())




