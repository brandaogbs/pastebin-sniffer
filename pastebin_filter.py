#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import subprocess
import shlex
import requests
import BeautifulSoup
import sys
import time

flag=""
lastflag=""

def get_sh(command):
	global flag
	global lastflag
        p = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
        flag = p.stdout.readline().strip()
	while True:
                output = p.stdout.readline()
		if output and (str(output).strip() != str(lastflag).strip()):
			raw_content(output.strip())
		else:
			lastflag = flag
                        break

def init_pastebin():
        url = get_sh('./get_links.sh')

def open_dictionary():
	with open(sys.argv[1], 'r') as file:
		f = file.read()
		dictionary = f.split('\n')
		return dictionary

def raw_content(url):
        content = get_raw_text(url)
	dic = open_dictionary()
	for key in dic:
		if key:
			for i in content:
				if (i.__contains__(key)):
					print "Relevant :", url
					return None					
					

def get_raw_text(url):
    raw_text = []
    r = requests.get(url)
    if r.status_code != 200:
        return None
    soup = BeautifulSoup.BeautifulSoup(r.content)
    for a in soup.findAll('textarea'):
        raw_text.append(a.text)
    return raw_text

while(True):
	print init_pastebin()
	time.sleep(66)
