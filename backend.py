import requests

api_key = 'faf3669fd074d3f7b878ec4489cf9165'


def get_data(place, forecast_days, kind):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = forecast_days * 8
    filtered_data = filtered_data[:nr_values]
    if kind == 'Temperature':
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    if kind == 'Sky':
        filtered_data = [dict['weather'][0]['main']]
    return filtered_data


    return data

if __name__ == '__main__':
    print(len(get_data('tokyo', forecast_days=3, kind='Temperature')))
