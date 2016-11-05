# Serene-Conky
Nice and clean conky theme, made using lua, cairo and python

# Requirements:
This Conky theme requires some python libraries for collecting data from the web, many of which might already have been installed on your system. If they are not, you can install them using the instructions given below.

## pip
We need a number of python libraries, so first install pip
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

## python-forecast.io  
### For all distros
    sudo pip install python-forecastio

## BeautiFul Soup
For scrapping data out of html pages
### For Ubuntu
    sudo apt-get install python-bs4
### For Arch Linux
    sudo pacman -S python-beautifulsoup4
### Using pip
    sudo pip install beautifulsoup4

## lxml
For parsing html
### For Ubuntu
    sudo apt-get install python-lxml
### For Arch Linux
    sudo pacman -S python-lxml
### Using pip
    sudo pip install lxml

# Configuration:
The main configuration is in config.yml (not complete yet)
In the files co_main, co_fact, co_quote and co_weather, modify the line "minimum_size 1366 748" to match your actual screen size. For example, your screen is 1366 x 768, so the line should be changed to "minimum_size 1366 768".

## Weather
You will need an api key from [darksky.net](https://darksky.net). Go to <https://darksky.net/dev/>, register and you will see your api key at the bottom of the page. Copy and paste it into the corresponding line in **config.yml** file.

We also need the latitude and longitude of where you are, you can get them by going to [darksky.net](https://darksky.net) and then search for your city. In the url, there will be the latitude and longitude, just copy and paste them into the correct line in the **config.yml** file.

You can also select your preferred units: for C and km/h use **ca**, for F and mph use **us**.

# Run
First, make start.sh and all the scripts in Scripts/ executable:
 "chmod +x start.sh" and do the same for all the scripts in /Scripts folder.
To start the theme, just go to Starter-Conky/ and use the command:
    ./start.sh
