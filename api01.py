'''
Ref:

https://www.tutorialspoint.com/requests/requests_file_upload.htm

200 - Success - OK
201 - Success - Create
404 - Client Error - Not Found


'''

# Part 1

# Get
payload = {'id': '9', 'username': 'Delphine'}
res = requests.get('https://jsonplaceholder.typicode.com/users',params = payload)
print(res)

# Post
res = requests.post('https://jsonplaceholder.typicode.com/users', data = {'id':'9', 'username':'Delphine'})
print(res)

# Put
res = requests.put('https://jsonplaceholder.typicode.com/users', data =
{'id':'9', 'username':'Delphine'})
print(res)

# Delete
res = requests.delete('https://jsonplaceholder.typicode.com/users')
print(res)
