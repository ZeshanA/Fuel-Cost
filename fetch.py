from lxml import html
import requests


def fetch_price():
    url = 'https://www.allstarcard.co.uk/fuel-card-services' \
          '/uk-fuel-price-information/'
    page = requests.get(url)
    tree = html.fromstring(page.content)
    price = float(
        tree.xpath('//*[@id="fuel-price-pump"]/div/div[1]/span/text()')[0]) / 100
    return price
