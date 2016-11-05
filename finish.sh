#!/bin/sh
cp /tmp/fact.tmp    Cache/fact.tmp
cp /tmp/quote.tmp   Cache/quote.tmp
cp /tmp/weather.tmp Cache/weather.tmp
kill $(pgrep ^conky$)
