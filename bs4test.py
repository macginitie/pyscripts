import requests
import bs4
res = requests.get('https://www.w3.org/testing/')
try:
  res.raise_for_status()  
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  for a in soup.select('a'):
    print(a.attrs)  
except Exception as err:
  print(err)
  
  
# import requests
# import bs4
# res = requests.get('https://www.w3.org/testing/')
try:
  res.raise_for_status()  
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  for p in soup.select('p'):
    print(p.getText())  
except Exception as err:
  print(err)
  
# import requests
res = requests.get('https://www.w3.org/TR/PNG/iso_8859-1.txt')
try:
  res.raise_for_status()
  iso_file = open('iso_8859.txt', 'wb')
  for chunk in res.iter_content(100000):
    iso_file.write(chunk)  
except Exception as err:
  print(err)
finally:
  if iso_file is not None:
    iso_file.close()