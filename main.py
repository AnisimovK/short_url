from urllib.parse import urlparse
import requests
from dotenv import load_dotenv
import os


def shorten_url(token, user_url):
    response = requests.post(
        api_shorten_url,
        headers={'Authorization': f'Bearer {token}'},
        json={"long_url": user_url}
    )
    response.raise_for_status()
    print(response.json()['link'])
    return response.json()['link']


def count_clicks(token, user_url):
    parsed_url = urlparse(user_url)
    response = requests.get(
        api_url_counter.format(f'{parsed_url.netloc}{parsed_url.path}'),
        headers={'Authorization': f'Bearer {token}'}
    )
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, user_url):
    parsed_url = urlparse(user_url)
    response = requests.get(
        api_info.format(f'{parsed_url.netloc}{parsed_url.path}'),
        headers={'Authorization': f'Bearer {token}'}
    )
    return response.ok


if __name__ == '__main__':
    user_url = input('Input url: ')
    load_dotenv()
    token = os.environ['TOKEN']
    api_shorten_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    api_url_counter = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'
    api_info = 'https://api-ssl.bitly.com/v4/bitlinks/{}'
    try:
        if is_bitlink(token, user_url):
            clicks_count = count_clicks(token, user_url)
            print('Count clicks :', clicks_count)
        else:
            bitly_url = shorten_url(token, user_url)
            print(f'Bitlink : {bitly_url}')
    except requests.exceptions.HTTPError:
        print("You have entered incorrect url, or you made too much requests")

