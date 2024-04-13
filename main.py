from flask import Flask, jsonify, request
import requests 
app = Flask(__name__)
def weather():
    city = request.args.get('city')
    api_key = '4a7d6d74bc157f639d27daa1c98395b1'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)