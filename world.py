#!/usr/bin/env python

import csv
from bottle import  default_app, run, redirect, error, route, template, static_file, get
import logging
logging.getLogger().setLevel(logging.DEBUG)


@error(404)
def error404(error):
    return '404 Nothing here, sorry'


@route('/static/:path#.+#', name='static')
def static(path):
    print '--' + path
    logging.error("uuu")
    logging.info("ggg")
    return static_file(path, root='static')


@get('/favicon.ico')
def get_favicon():
    return ''


@route('/')
def main():
    return template('start_page', countries=load_countries())
#     redirect("static/main.html")


@route('/<country_code>')
def hello(country_code):
#     if country_code is None:
#         redirect("static/main.html")
    dictionary = build_dict(country_code)  # print dictionary
    if len(dictionary) == 0:
        return template('not_found', name=country_code)
    else:
        return template('country_template', dictionary=dictionary)


def build_dict(country_code):
    # 0  name
    # 1  local-name
    # 2  top-level domain
    # 6  ISO 4217 currency code(s) (currency)
    # 7  calling code(s) (calling-code)
    # 8  capital city (capital)
    # 9  alternative spellings (alt-spellings)
    # 11 region
    # 12 subregion
    # 13 language in English
    dictionary = {}
    with open("countries.csv") as f:
        spamreader = csv.reader(f, delimiter=';')
        for row in spamreader:
            codes = row[2].lower().split(',')
            for cod in codes:
                if cod[1:] == country_code.lower():
                    dictionary['name'] = row[0]
                    dictionary['local-name'] = row[1]
                    dictionary['top-level-domain'] = row[2]
                    dictionary['calling-code'] = row[7]
                    dictionary['capital-city'] = row[8]
                    dictionary['region'] = row[11]
                    dictionary['subregion'] = row[12]
                    dictionary['language'] = row[13]
                    return dictionary

#     print country_code + " not found"
    return dictionary


def load_countries():
    dictionary = {}
    with open("countries.csv") as f:
        spamreader = csv.reader(f, delimiter=';')
        for row in spamreader:
            dictionary[row[0]] = row[2].lower().split(',')[0][1:]
#             dictionary['name'] = row[0]

    return dictionary


# run(host='localhost', port=8080)

application = default_app()
