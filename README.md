# Serene-Conky
Nice and clean conky theme, made using lua, cairo and python

# Requirements:

This Conky theme requires python libraries of getting the data from the web, many of them will already be installed on the system, but if they are not you can install them using the instruction given below

## pip
We need a number of python libraries, first install pip
### On Ubuntu
    sudo apt-get install python-pip
### On Fedora
    sudo yum install python-pip
If their is any problem consult their [documentation](https://pip.pypa.io/en/stable/installing.html)

## pyyaml
This package is needed for parsing yaml files
### On Ubuntu
    sudo apt-get install python-yaml
### On Fedora
    sudo yum install python-yaml
### For Arch Linux
    sudo pacman -S python2-yaml
### Using pip
    sudo pip install pyyaml

## python-forecast.io  For All Distros
    sudo pip install python-forecastio

## BeautiFul Soup
For scrapping data out of html pages
### For Ubuntu
    sudo apt-get install python-bs4
### FOr Arch Linux
    sudo pacman -S python-beautifulsoup4
### Using pip
    sudo pip install beautifulsoup4

## lxml
For parsing html
### For Ubuntu
    sudo apt-get install python-lxml
### FOr Arch Linux
    sudo pacman -S python-lxml
### Using pip
    sudo pip install lxml


# Configuration:
The main configuration is in config.yml (not complete yet)
Edit co_main co_fact co_quote co_weather and change minimum_size 1366 748 to your laptop screen size

## Weather
You will need an api key from [forcast.io](http://forecast.io). Go to <http://https://developer.forecast.io/>, register and you will see the api and the bottom of the page. Copy and paste it in the **config.yml** file.

We also need the latitude and longitude, for to [forecast.io](http://forecast.io) and search for your city. Now in the url you will see the latitude and longitude, copy and paste them in the **config.yml** file.

Choose the unit, for C and km/h use **ca** and for F and mph use **us**


# Run
To start the theme, just go in its directory and use
    ./start.sh
After making the files in Scripts/ and start.sh executable
 "chmod +x start.sh" and do the same for all the scripts in /Scripts folder
