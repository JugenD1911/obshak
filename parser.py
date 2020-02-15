import requests
from bs4 import BeautifulSoup

URL = 'https://www.cvedetails.com/vulnerability-list/vendor_id-452/product_id-3264/version_id-111276/Mozilla-Firefox-3.6.17.html'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36', 'accept': '*/*'}



def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html5lib')
    table = soup.findChildren('table')
    my_table = table[0]

    rows = my_table.findChildren(['th', 'tr'])
    for row in rows:
    	cells = row.findChildren('td')
    	for cell in cells:
    		value = cell.text
    		print(value)

    #cve = []
    #for item in items:
    	#cve.append({
    		#'title': item.find('table',class_='searchresults sortable').get_text()
    		#})
    #print(cve)




def parse():
    html = get_html(URL)
    if html.status_code == 200:
        cars = get_content(html.text)
    else:
        print('Error')


parse()
