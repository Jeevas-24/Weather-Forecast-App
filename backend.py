import requests

api_key = 'faf3669fd074d3f7b878ec4489cf9165'


def get_data(place='Tokyo', forecast_days=None, kind=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == '__main__':
    print(get_data('tokyo'))
