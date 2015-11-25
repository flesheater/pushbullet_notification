#! /usr/local/bin/python

token = ''

import pycurl
import cStringIO
import json
import urllib

response = cStringIO.StringIO()
postNote = {'type': 'note', 'title': 'Title'}
postData = urllib.urlencode(postNote)

c = pycurl.Curl()
c.setopt(pycurl.URL,'https://api.pushbullet.com/v2/pushes')
		
c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
c.setopt(pycurl.HTTPHEADER, ['Content-type: application/x-www-form-urlencoded'])
		
csrf_token_header = 'Access-Token: ' + token
c.setopt(pycurl.HTTPHEADER, [csrf_token_header])

c.setopt(pycurl.WRITEFUNCTION, response.write)
c.setopt(pycurl.POST, 1)
		
c.setopt(pycurl.POSTFIELDS, postData)
c.perform()
c.close()

