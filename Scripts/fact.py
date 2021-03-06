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
    # get the fact page
    page = requests.get(config['fact']['url'])
    # make the soup
    soup = BeautifulSoup(page.text, "lxml")
    # get the facts
    did_you_know = soup.find("div", {"class":"dyk-content"})
    tech_term    = soup.find("div", {"class":"dtt-content"})

    facts = dict()
    if len(tech_term.text) <= 512:
        facts['1_fact'] = re.sub(r'\s+', r' ', unicode(tech_term.text).strip())
    else:
        facts['1_fact'] = re.sub(r'\s+', r' ', unicode(did_you_know.text).strip())
    if len(did_you_know.text) <= 512:
        facts['2_fact'] = re.sub(r'\s+', r' ', unicode(did_you_know.text).strip())
    else:
        facts['2_fact'] = re.sub(r'\s+', r' ', unicode(tech_term.text).strip())
    return facts


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
