#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Momo Outaadi (M4ll0k)

import httplib 
import sys
import re
import getopt


class Shish(object):
	#Shish - Test all headers values with your payload
 	def __init__(self,kwargs):
		self.kwargs=kwargs
	
	def Usage(self,exit=False):
		print "@Testing all headers values with your payload"
		print "@Coded by M4ll0k\n"
		print " -u --url\tTarget URL (eg:examples.com)"
		print " -p --payload\tSet payload"
		print " -c --code\tWrite results when return code (400,<400,>400)"
		print " -h --help\tShow this help\n"
		if exit:
			sys.exit(0)
	
	#def Payload(self,payload):
		#if isinstance(payload,unicode):
			#return payload.encode('utf-8')
		#if type(payload) is not str and isinstance(payload,str):
			#return str(payload)
	
	def Main(self):
		if len(sys.argv)<=3:
			self.Usage(True)
		try:
			opts,args =getopt.getopt(self.kwargs,"u:p:c:h",["url=","payload=","code=","help"])
		except getopt.error,error:
			pass
		for o,a in opts:
			if o in ('-u','--url'):
				_url = a 
			elif o in ('-p','--payload'):
				_payload = a
			elif o in ('-c','--code'):
				_code = a			
			elif o in ('-h','--help'):
				self.Usage(True)
		db = open('headers.txt','rb')
		for x in db:
			print "{}[*]{} Testing {}{}{} value with: {}{}{}".format('\033[1;34m','\033[0m','\033[1;32m',str(x.split('\n')[0].split('"')[1]),'\033[0m','\033[1;33m',_payload,'\033[0m')
			try:
				con = httplib.HTTP(_url)
				con.putrequest('GET','/')
				con.putheader('User-agent','Mozilla/5.0 (X11; Linux x86_64; rv:15.0) Gecko/20120724 Debian Iceweasel/15.0')
				con.putheader('Host',_url)				
				con.putheader('{}'.format(str(x.split('\n')[0].split('"')[1])),'{}'.format(_payload))
				con.endheaders()
				c,m,h=con.getreply()
				r = con.getfile().read()
				print c,m
				print h
				if '<' in _code:
					if c == _code.split('<')[1]:
						print r
				elif '>' in _code:
					if c == _code.split('>')[1]:
						print r
				elif c == _code:
					print r
			except Exception,error:
				pass
def main(sys_):
	try:
		Shish(sys_).Main()
	except KeyboardInterrupt:
		sys.exit("[!] Keyboard Interrupt by user")
main(sys.argv[1:])
