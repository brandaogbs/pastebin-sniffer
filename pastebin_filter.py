#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import subprocess
import shlex
import requests
import BeautifulSoup
import sys

def get_sh(command):
        p = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
        while True:
                output = p.stdout.readline()
                if output:
                        print "Try: ", output.strip()
                        raw_content(output.strip())
                else:
                        print "Escape :("
                        break

# Main function
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
					print "True ========> ", url
					
					

def get_raw_text(subreddit):
    raw_text = []
    r = requests.get(subreddit)
    if r.status_code != 200:
        return None
    soup = BeautifulSoup.BeautifulSoup(r.content)
    for a in soup.findAll('textarea'):
        raw_text.append(a.text)
    return raw_text

#for i in get_links_from(url):
#    print "%s" % (link_name)

print init_pastebin()
