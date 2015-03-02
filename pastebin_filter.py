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
