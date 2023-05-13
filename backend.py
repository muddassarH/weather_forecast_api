import requests
API_KEY = "3a7eeddfdd24a59acffa7703db68ebce"


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filter_data = data['list']
    nr_values = 8 * forecast_days
    filter_data = filter_data[:nr_values]
    if kind == "Temperature":
        filter_data = [dict["main"]["temp"] for dict in filter_data]
    if kind == "Sky":
        filter_data = [dict["weather"]["0"]["main"] for dict in filter_data]
    return filter_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))