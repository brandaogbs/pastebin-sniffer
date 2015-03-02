#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import subprocess
#import dis
 
def wget_filter():
	subprocess.call("rm archive*", shell=True)
	wget = subprocess.Popen(['wget', 'http://pastebin.com/archive'], 
                        stdout=subprocess.PIPE,
                        )
	cat = subprocess.Popen(['cat', 'archive'],
                        stdin=wget.stdout,
                        stdout=subprocess.PIPE,
                        )
	grep = subprocess.Popen(['grep', 'i_p0'],
                        stdin=cat.stdout,
                        stdout=subprocess.PIPE,
                        )

	end_of_pipe = grep.stdout
	print 'SAIDA ENDPIPE:'
	for line in end_of_pipe:
    		print '\t', line.strip()


def href_filter():
	r = str(wget_filter())
	print r


print wget_filter()
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
        	print output.strip()
	else: 
		print "escape ;X"
		break

#def wget_filter():
#	end_of_pipeu= grep.stdout
#	print 'SAIDA ENDPIPE:'
#	for line in end_of_pipe:
#   		print '\t', line.strip()

def check_content(content):#vai checar o assunto do conn_pbin
	


def conn_pbin(): #vai abrir o site apartir de cada linha do get_sh
	url = get_sh('cat get_info.sh')
	
	
#print conn_pbin()


