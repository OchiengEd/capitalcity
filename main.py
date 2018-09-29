#!/usr/bin/env python
from flask import Flask, render_template
import requests, json
import os

api_url = "https://restcountries.eu/rest/v2/name/{}?fields=name;capital;region"
application = Flask(__name__)

@application.route('/')
def landing():
  page = """<html><head><title>World Countries</title></head><body>
    Welcome to worldcountries api. To interact with the api,
    </body></html>"""
  return page

@application.route('/trivia')
def world_countries():
  cc_server = os.environ['COUNTRY_CODE_SRV']
  url = 'http://{}/trivia'.format(cc_server)
  response = requests.get(url)
  if response.status_code == 200:
    trivia_url = 'https://restcountries.eu/rest/v2/alpha/{}?fields=name;capital;region'.format(response.content)
    trivia_response = requests.get(trivia_url)
    if trivia_response.status_code == 200:
      return  render_template('index.html', country=json.loads(str(trivia_response.content)))

@application.route('/capital/<country>')
def get_capital_of_country(country = None):
	url = api_url.format(country)
	response = requests.get(url)
	if response.status_code == 200:
		return render_template('index.html', country=json.loads(str(trivia_response.content)))

def main():
	application.run(port=8090)

if __name__ == '__main__':
	main()
