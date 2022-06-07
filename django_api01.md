https://codeburst.io/create-a-django-api-in-under-20-minutes-2a082a60f6f3

```
$ curl -i -X GET http://127.0.0.1:8000/api/note/1/   

$ curl -i -X POST -H 'Content-Type: application/json' -d '{"title": "N2", "body": "b2"}' http://127.0.0.1:8000/api/note/

$ curl -i -X GET http://127.0.0.1:8000/api/note/  
```

https://www.postman.com/popcornv/workspace/popcornv-s-public-workspace/request/create?requestId=29859d92-27da-4783-9cb2-124d27587d29


https://stackoverflow.com/questions/4797534/how-to-manually-send-http-post-requests-from-firefox-or-chrome-browser

```
curl -i -X GET http://rest-api.io/items
curl -i -X GET http://rest-api.io/items/5069b47aa892630aae059584
curl -i -X DELETE http://rest-api.io/items/5069b47aa892630aae059584
curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "New item", "year": "2009"}' http://rest-api.io/items
curl -i -X PUT -H 'Content-Type: application/json' -d '{"name": "Updated item", "year": "2010"}' http://rest-api.io/items/5069b47aa892630aae059584
```
