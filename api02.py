'''
Ref:

https://www.tutorialspoint.com/requests/requests_file_upload.htm

200 - Success - OK
201 - Success - Create
404 - Client Error - Not Found


'''
import requests

getdata = requests.get('https://jsonplaceholder.typicode.com/users')
print(getdata.status_code)
print(getdata.content)
print(getdata.cookies["__cfduid"])

payload = {'id': 9, 'username': 'Delphine'}
getdata = requests.get('https://jsonplaceholder.typicode.com/users', params = payload)
print(getdata.content)
print(getdata.url)
print(getdata.encoding)
print(getdata.json())

getdata = requests.get('https://jsonplaceholder.typicode.com/users', stream=True)
print(getdata.raw)
print(getdata.raw.read(50))

print(getdata.headers)

myurl = 'https://postman-echo.com/post'
myparams = {'name': 'ABC', 'email':'xyz@gmail.com'}
res = requests.post(myurl, data=myparams)
print(res.text)
