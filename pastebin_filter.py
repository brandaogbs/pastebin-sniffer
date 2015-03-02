#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import subprocess
import shlex
#import dis

def get_sh(command):#retorna linha (url) por linha pro conn_pbin
    p = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = p.stdout.readline()
        if output:
        	print "url: ", output.strip()
	else: 
		print "escape :("
		break

#def wget_filter():
#	end_of_pipeu= grep.stdout
#	print 'SAIDA ENDPIPE:'
#	for line in end_of_pipe:
#   		print '\t', line.strip()

def check_content(content):#vai checar o assunto do conn_pbin
	print "nothing"	


def conn_pbin(): #vai abrir o site apartir de cada linha do get_sh
	url = get_sh('./get_links.sh')
	
	
print conn_pbin()


