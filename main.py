from urllib.parse import urlparse
import requests
from dotenv import load_dotenv
import os


short_url = 'https://api-ssl.bitly.com/v4/bitlinks'
counter_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'
is_bitlink_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'


def shorten_url(bitly_token, user_url):
    response = requests.post(
        short_url,
        headers={'Authorization': f'Bearer {bitly_token}'},
        json={"long_url": user_url}
    )
    response.raise_for_status()
    return response.json()['link']


def count_clicks(bitly_token, user_url):
    parsed_url = urlparse(user_url)
    response = requests.get(
        counter_url.format(f'{parsed_url.netloc}{parsed_url.path}'),
        headers={'Authorization': f'Bearer {bitly_token}'}
    )
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(bitly_token, user_url):
    parsed_url = urlparse(user_url)
    response = requests.get(
        is_bitlink_url.format(f'{parsed_url.netloc}{parsed_url.path}'),
        headers={'Authorization': f'Bearer {bitly_token}'}
    )
    return response.ok


if __name__ == '__main__':
    user_url = input('Input url: ')
    load_dotenv()
    bitly_token = os.environ['BITLY_TOKEN']
    try:
        if is_bitlink(bitly_token, user_url):
            clicks_count = count_clicks(bitly_token, user_url)
            print('Count clicks :', clicks_count)
        else:
            bitly_url = shorten_url(bitly_token, user_url)
            print(f'Bitlink : {bitly_url}')
    except requests.exceptions.HTTPError:
        print("You have entered incorrect url, or you made too much requests")

