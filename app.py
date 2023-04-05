#!/usr/bin/env python

#-----------------------------------------------------------------------
# penny.py
# Author: Bob Dondero
#-----------------------------------------------------------------------

from flask import Flask, request, make_response, render_template
from database import search

#-----------------------------------------------------------------------

app = Flask(__name__, template_folder='.')

#-----------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():

    html = render_template('index.html')
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/searchresults', methods=['GET'])
def search_results():

    city = request.args.get('city')
    print(city)
    if (city is None) or (city.strip() == ''):
        response = make_response('')
        return response

    cities = search(city)  # Exception handling omitted

    html = '''
    <table>
    <thead>
        <tr>
            <th>City</th>
            <th>Country</th>
        </tr>
    </thead>
    <tbody>
    '''

    pattern = '''
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td style="display:none;">%s</td>
    </tr>
    '''
    for city in cities:
        # print("city: ", city)
        html += pattern % (city[0], city[1], city[2])

        # html += pattern % city.to_tuple()

    html += '''
    </tbody>
    </table>
    '''

    response = make_response(html)
    return response

