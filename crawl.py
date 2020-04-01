import requests
from bs4 import BeautifulSoup

def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5h://127.0.0.1:9050',
                       'https': 'socks5h://127.0.0.1:9050'}
    return session

# Make a request through the Tor connection
# IP visible through Tor
session = get_tor_session()
response = session.get("http://relatecxjngl4qs7.onion/").text
soup = BeautifulSoup(response,'lxml')
x = soup.find_all("input")
print(x)


# Above should print an IP different than your public IP
