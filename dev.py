#!/usr/bin/env python
# coding: utf8
#requests is broken SSL certificates not being handled correctly.
#If you want to remove the warnings, use the code below.
import urllib2
#urllib2.disable_warnings()
# and verify=False with request.get or post method
#AttributeError: 'module' object has no attribute 'disable_warnings'
print "hello world from dev.py"
import sys
#import urllib2
#import urllib
import requests
import time
time.sleep(15)

#payload = {
#    'cmd': 'login',
#    'action': 'login',
#    'username': 'UserName',
#    'password': 'password'
#}

#with session() as c:
#    c.post('http://example.com/login.php', data=payload)
#    r_login = c.post('https://www.stockwatch.com/login.aspx', data=payload)
#    print (c.cookies)
#    print (r_login.status_code)
#    print (r_login.headers)
#    print (r_login.text)

#headers2 = {'Cookie':'XXX=43709162%2c385549%2c57162%2cUserName'}
#s = requests.Session()
#s.get('https://www.stockwatch.com/',verify=False)

#    response = c.get('https://www.stockwatch.com/Quote/Download.aspx?type=date&format=ascii&dest=file&exopt=N&ex=T&ats=Y',headers=headers2)
#response = s.get('https://www.stockwatch.com/Quote/Download.aspx?type=date&format=ascii&dest=file&exopt=N&ex=T&ats=Y',headers=headers2,verify=False)
#response = s.get('https://www.stockwatch.com/Quote/Download.aspx?type=date&format=ascii&dest=file&exopt=N&ex=T&ats=Y&id=UserName&pw=password')
#print(response.headers)
#print(response.text)


#PHP is an HTML-embedded scripting language. 
#url = "http://httpbin.org/headers"

#print url
#req = urllib2.Request(url)
#try:
#  response = urllib2.urlopen(req)
#except urllib2.URLError as e:
#    if hasattr(e, 'reason'):
#        print 'We failed to reach a server.'
#        print 'Reason: ', e.reason
#    if hasattr(e, 'code'):
#        print 'The server couldn\'t fulfill the request.'
#        print 'Error code: ', e.code
#else:  
#  webContent = response.read()          
#  print 'length=', len(webContent)       
#  print webContent
#  print "Done fetchhtmlDaylyStockwatch.py"
