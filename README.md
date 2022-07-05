# Tatoeba-Cangarejo---Find-Sentences-without-Direct-or-Indirect-Translations

## Started with Cangarjo's Python 3 Script

My aim is to create the same type of output, but to limit the results to sentences owned by native speakers.
This should help lower the number of errors found in the data.
Also, most language learners would probably prefer to learn from sentences created by native speakers.
After members have finished translating all the sentences owned by native speakers, then they could run Cangarejo's original script to find all the other sentences.

## Files needed

* https://downloads.tatoeba.org/exports/sentences_detailed.tar.bz2

Or: https://downloads.tatoeba.org/exports/sentences_detailed.csv

* https://downloads.tatoeba.org/exports/links.tar.bz2

Or: https://downloads.tatoeba.org/exports/links.csv

* nativespeakers.tsv

These are the data statments in http://bit.ly/nativespeakers, with the quotes and commas removed.
You can use the file in this directory, or harvest newer data, if any, from http://bit.ly/nativespeakers.

### Example:
```
acm	hasenj	46
acm	salemazez	1
afb	hamzah	45
afb	Huda_Mohammad	45
afb	hadalabadi	3
afb	Muhammed_abdoon	2
afb	OmarSyr	1
etc.
```

### The original HTML file looked like this:
```
"acm	hasenj	46",
"acm	salemazez	1",
"afb	hamzah	45",
"afb	Huda_Mohammad	45",
"afb	hadalabadi	3",
"afb	Muhammed_abdoon	2",
"afb	OmarSyr	1",
"afr	CJuser01	1013",
etc.
```
