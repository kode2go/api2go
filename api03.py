'''
Ref:

https://www.tutorialspoint.com/requests/requests_file_upload.htm

200 - Success - OK
201 - Success - Create
404 - Client Error - Not Found

'''

import requests

# Cookies
cookies = dict(test='test123')
getdata = requests.get('https://httpbin.org/cookies',cookies=cookies)
print(getdata.text)

# Error Handling

'''
Timeouts can be easily added to the URL you are requesting. It so happens that,
 you are using a third-party URL and waiting for a response. It is always a good practice
  to give a timeout on the URL, as we might want 
the URL to respond within a timespan with a response or an error. Not doing so,
 can cause to wait on that request indefinitely.
'''
getdata = requests.get('https://jsonplaceholder.typicode.com/users',timeout=0.001)
print(getdata.text)  

# With a timeout of 1 second, we can get the response for the URL requested.
getdata = requests.get('https://jsonplaceholder.typicode.com/users',timeout=1.001)
print(getdata.text)  

# Authentication

from requests.auth import HTTPBasicAuth
response_data = requests.get('httpbin.org/basic-auth/admin/admin123', auth = HTTPDigestAuth('admin', 'admin123'))
print(response_data.text)  

# Event Hook
# We can add events to the URL requested using event hooks
def printData(r, *args, **kwargs):
   print(r.url)
   print(r.text)
getdata = requests.get('https://jsonplaceholder.typicode.com/users', hooks={'response': printData}) 

# Event Proxy

'''
Using Http-proxy is additional security assigned to manage the data exchange between client and server. 
'''
proxies = {
'http': 'http://localhost:8080'
}
res = requests.get('http://httpbin.org/', proxies=proxies)
print(res.status_code) 


