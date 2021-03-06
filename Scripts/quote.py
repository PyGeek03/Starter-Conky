#!/usr/bin/python2.7

from bs4 import BeautifulSoup
from lxml import html
import requests
import yaml
import re

def readConfiguration():
    # open the configuration file in read mode
    config_file = open('config.yml', 'r')
    # now load the yaml
    config = yaml.load(config_file)
    config_file.close()
    return config


def readQuote(config):
    # get the quote page
    page = requests.get(config['quote']['url'])
    # make the soup
    soup = BeautifulSoup(page.text, "lxml")
    # lets find the quotes
    data = dict()
    quotes  = soup.find_all(title="view quote")
    authors = soup.find_all(title="view author")
    for i in range(0,5):
        data[str(i+1) + '_quote']  = re.sub(r'\s+', r' ', unicode(quotes[i].text).strip())
        data[str(i+1) + '_author'] = re.sub(r'\s+', r' ', unicode(authors[i].text).strip())
    return data


def writeQuote(data):
    # open the file for writing
    quote_file = open('/tmp/starter-conky/quote.tmp', 'w')
    # write the quotes
    for key in data:
        quote_file.write(key + ':' + str(data[key]) + '\n')
    # close the file
    quote_file.close()


# read the configuration file
config = readConfiguration()
# read the quotes
data = readQuote(config)
data['status'] = 'FILLED'
# write them to a file
writeQuote(data)
