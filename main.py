#!/usr/bin/env python
from flask import Flask
import requests, json

api_url = "https://restcountries.eu/rest/v2/name/{}?fields=name;capital"
application = Flask(__name__)

@application.route('/capital/<country>')
def get_capital_city(country = None):
	url = api_url.format(country)
	response = requests.get(url)
	if response.status_code == 200:
		return response.content

def main():
	application.run(port=8090)

if __name__ == '__main__':
	main()
