#!/bin/bash
mkdir /tmp/starter-conky

function update
{
    TMP_FILE="$1"
    CACHE_FILE="$2"
    if [ -e $TMP_FILE ]; then
        cp $TMP_FILE $CACHE_FILE
    else
        cp $CACHE_FILE $TMP_FILE
    fi
}

update /tmp/starter-conky/fact.tmp    Cache/fact.tmp
update /tmp/starter-conky/quote.tmp   Cache/quote.tmp
update /tmp/starter-conky/weather.tmp Cache/weather.tmp

sleep 5
conky -d -c co_main    > /tmp/starter-conky/starter-conky.log &
conky -d -c co_weather > /tmp/starter-conky/starter-conky.log &
conky -d -c co_fact    > /tmp/starter-conky/starter-conky.log &
conky -d -c co_quote   > /tmp/starter-conky/starter-conky.log &
