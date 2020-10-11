from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests

app = Flask(__name__)


@app.route('/check', methods=['POST'])
def check():
    city_name = request.get_json()['city_name']
    try:
        api_url = "http://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
        url = api_url + city_name
        response = requests.get(url)
        content = response.json()
        icon = 'http://openweathermap.org/img/w/' + \
            str(content['weather'][0]['icon']) + '.png'
        city_weather = {
            "city": city_name,
            "temperature": str(content['main']['temp']) + '° F',
            "description": content['weather'][0]['description'],
            "icon": icon,
        }
    except:
        city_weather = {
            'city': 'City not found',
            'temperature': '0° F',
            'description': 'No description',
            'icon': '/static/exclamation-triangle-solid.svg'
        }

    return jsonify(city_weather)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
