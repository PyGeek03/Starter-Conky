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
    for i in range(0,1000):
        data['fact'] = unicode(soup(class_='sliderText')[0].text).strip()
        data['fact'] = re.sub(r'\s+', r' ', data['fact'])

    # lets find the quotes
    return data


def writeFact(data):
    # open the file for writitng
    fact_file = open('/tmp/starter-conky/fact.tmp', 'w')
    # write the fact
    fact_file.write('fact:' + data['fact'].encode('utf-8'))
    fact_file.write('\nstatus:' + data['status'])
    # close the file
    fact_file.close()


# read the configuration file
config = readConfiguration()
# read the quotes
data = readFact(config)
data['status'] = 'FILLED'
# write them to a file
writeFact(data)
