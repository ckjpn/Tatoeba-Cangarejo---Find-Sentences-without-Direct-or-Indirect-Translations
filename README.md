# Tatoeba-Cangarejo---Find-Sentences-without-Direct-or-Indirect-Translations

## Note that this is a planned project and nothing has been added to Cangarjo's original script yet.


## Started with Cangarjo's Python 3 Script

My aim is to create the same type of output, but to limit the results to sentences owned by native speakers.
This should help lower the number of errors found in the data.
Also, most language learners would probably prefer to learn from sentences created by native speakers.
After members have finished translating all the sentences owned by native speakers, then they could run Cangarejo's original script to find all the other sentences.

I would use the list of native speakers that I have compiled (https://bit.ly/nativespeakers).  This list also identifies native speakers who were part of the project before TRANG added the feature to include one's native language as something that gets exported.  Also, I have chosen not to trust those who have multiple native languages listed, since many seem to either exaggerate or are over-confident in their "nativeness" of languages other than their native language. I do write to such members and ask them to identify their "real" native language or strongest language and add such members to my list with that language.

## Files needed

* https://downloads.tatoeba.org/exports/sentences_detailed.tar.bz2

Or: https://downloads.tatoeba.org/exports/sentences_detailed.csv

* https://downloads.tatoeba.org/exports/links.tar.bz2

Or: https://downloads.tatoeba.org/exports/links.csv

* nativespeakers.tsv

These are the data statments in http://bit.ly/nativespeakers, with the quotes and commas removed.
You can use the file in this directory, or harvest newer data, from http://bit.ly/nativespeakers, which is much more likely to be up-to-date.

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
