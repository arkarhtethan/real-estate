import requests
from bs4 import BeautifulSoup

response = requests.get('http://127.0.0.1:8000/property/')

soup = BeautifulSoup(response.content, 'html.parser')

select = soup.find("select",attrs={"name":"state"})

for option in select.find_all('option'):

    print(option.get_text('value'))
    print(option)


