# short_url

Make a short url and count there clicks Программа принимает на вход ссылку, которую '
                    'необходимо сократить, либо bitly ссылку, '
                    'и выводит количество переходов по ней'


## How to install

Python3 should already be installed.
Create and activate virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

Use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```

Get api bitly api token, place it to .env file in count_clicks directory

```
cd short_url
echo "BITLY_TOKEN=absbsbsbsbssbsbba22222222341414asd" >> .env
```

Help:
```
python3 main.py -h
```

## Usage
Example. Creating short url:
```
python3 main.py https://dvmn.org
```

Example. Info about count of clicks on a link.:
```
python3 main.py https://bit.ly/3Nse9mZ
```
