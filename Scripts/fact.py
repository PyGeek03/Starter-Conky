#!/usr/bin/python2.7

from bs4 import BeautifulSoup
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


def readFact(config):
    # get the quote page
    page = requests.get(config['fact']['url'])
    # make the soup
    soup = BeautifulSoup(page.text, "lxml")
    # get the fact
    data = dict()
    for i in range(0,2):
        data[str(i+1) + '_fact'] = re.sub(r'\s+', r' ', unicode(soup(class_='glossaryhomebox')[i].text).strip())

    # lets find the quotes
    return data


def writeFact(data):
    # open the file for writing
    fact_file = open('/tmp/starter-conky/fact.tmp', 'w')
    # write the facts
    for key in data:
        fact_file.write(key + ':' + data[key].encode('utf-8') + '\n')
    # close the file
    fact_file.close()


# read the configuration file
config = readConfiguration()
# read the facts
data = readFact(config)
data['status'] = 'FILLED'
# write them to a file
writeFact(data)
