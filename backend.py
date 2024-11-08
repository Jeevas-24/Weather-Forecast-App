import requests

api_key = 'faf3669fd074d3f7b878ec4489cf9165'


def get_data(place, forecast_days):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = forecast_days * 8
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == '__main__':
    print(get_data('tokyo', forecast_days=3))
