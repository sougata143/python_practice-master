#install Beaustifulsoap by 'pip install Beautifulsoup' or 'conda install Beautifulsoup' command
import urllib3
from bs4 import BeautifulSoup

# Fetch the html file
http = urllib3.PoolManager()
url = 'http://tutorialspoint.com/python/python_overview.htm'
# response = urllib3.urlopen('http://tutorialspoint.com/python/python_overview.htm')
response = http.request('GET', url)
html_doc = response.read()

# Parse the html file
# soup = BeautifulSoup(html_doc, 'html.parser')
soup = BeautifulSoup(response.data)

# Format the parsed html file
strhtm = soup.prettify()

# Print the first few characters
print (strhtm[:225])
print (soup.title)
print(soup.title.string)
print(soup.a.string)
print(soup.b.string)

#Extracting All Tags
for x in soup.find_all('b'): print(x.string)