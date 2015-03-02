pastebin-sniffer
================ 

A set of scripts to filter the content of pastebin's archive.

Dictionaries
------------

The only filter in this current version is a word filter. The filter will look for each word in the selected dictionary in each of the links present in the pastebin's archive. The available dictonaries are:

 - password
 - bitcoin
 - nudes

The dictonaries contain related strings that may appear in the raw data.

Prerequisites
-------------

You may need to install some python2 libs:

 - requests
 - BeautifulSoup

Usage
-----

	chmod +x pastebin-sniffer
	./pastebin-sniffer <dictionary> 
