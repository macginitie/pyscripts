from datetime import datetime as dt
import requests
import bs4


def get_date_str():
    ds = str(dt.now().date())
    return ds.replace('-', '.')


def get_wikipage():
    res = None
    try:
        res = requests.get('https://en.wikipedia.org/wiki/COVID-19_pandemic#Epidemiology') 
        res.raise_for_status()  
    except Exception as err:
        print(err)
        
    return res
    
    
def get_world_count(page):    
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table', {'id':'thetable'})
    th = table.select('th')
    world = str(th[8])
    
    return world[-13:-6].replace(',', '')
       
    
def get_US_count(page):
    
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table', {'id':'thetable'})
    td = table.select('td')
    UScount = str(td[1])
    
    return UScount[-13:-6].replace(',', '')


if __name__ == '__main__':

    d8 = get_date_str()
    page = get_wikipage()
    if page is not None:
        world = get_world_count(page)
        US = get_US_count(page)
    
    print('{0}, {1}, {2}\n'.format(d8, US, world))
