from datetime import datetime as dt
import requests
import bs4


def get_date_str():
    ds = str(dt.now().date())
    return ds.replace('-', '.')


def get_wikipage():
    res = None
    try:
        # I think including '#Epidemiology' has no effect here, 
        # but I suppose it doesn't hurt either
        res = requests.get('https://en.wikipedia.org/wiki/COVID-19_pandemic#Epidemiology') 
        res.raise_for_status()  
    except Exception as err:
        print(err)
        
    return res
    
    
def get_world_count(table):
    th = table.select('th')
    world = str(th[8])
    return world[-13:-6].replace(',', '')
       
    
def get_US_count(table):
    td = table.select('td')
    US = str(td[1])   
    return US[-13:-6].replace(',', '')


if __name__ == '__main__':

    d8 = get_date_str()
    page = get_wikipage()
    if page is not None:
        soup = bs4.BeautifulSoup(page.text, 'html.parser')
        table = soup.find('table', {'id':'thetable'})
        world = get_world_count(table)
        US = get_US_count(table)
        print('{0}, {1}, {2}'.format(d8, US, world))
    else:
        print('error: no internet connection, perhaps?')
