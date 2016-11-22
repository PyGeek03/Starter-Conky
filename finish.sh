#!/bin/sh
cd /home/pygeek03/bin/Starter-Conky
cp /tmp/starter-conky/fact.tmp     Cache/fact.tmp
cp /tmp/starter-conky/quote.tmp    Cache/quote.tmp
cp /tmp/starter-conky/weather.tmp  Cache/weather.tmp
kill $(pgrep ^conky$)
