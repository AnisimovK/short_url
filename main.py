from urllib.parse import urlparse
import requests
from dotenv import load_dotenv
import os
import argparse


def shorten_url(token, user_url):
    api_shorten_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(
        api_shorten_url,
        headers={'Authorization': f'Bearer {token}'},
        json={"long_url": user_url}
    )
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, user_url):
    api_counter_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'
    parsed_url = urlparse(user_url)
    response = requests.get(
        api_counter_url.format(f'{parsed_url.netloc}{parsed_url.path}'),
        headers={'Authorization': f'Bearer {token}'}
    )
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, user_url):
    api_info_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'
    parsed_url = urlparse(user_url)
    response = requests.get(
        api_info_url.format(f'{parsed_url.netloc}{parsed_url.path}'),
        headers={'Authorization': f'Bearer {token}'}
    )
    return response.ok


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа принимает на вход ссылку, которую '
                    'необходимо сократить, либо bitly ссылку, '
                    'и выводит количество переходов по ней'
    )
    parser.add_argument('user_url', help='Ваша ссылка')
    user_url = parser.parse_args().user_url
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
    try:
        if is_bitlink(token, user_url):
            clicks_count = count_clicks(token, user_url)
            print('Count clicks :', clicks_count)
        else:
            bitly_url = shorten_url(token, user_url)
            print(f'Bitlink : {bitly_url}')
    except requests.exceptions.HTTPError:
        print("You have entered incorrect url, or you made too much requests")
