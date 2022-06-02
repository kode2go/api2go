# https://serpapi.com/yahoo-search-api
from serpapi import GoogleSearch
import json

params = {
  "engine": "yahoo",
  "p": "coffee mug",
  "api_key": "6167704a6638a86b04c8e57e23d5e56aba919c1dc1ca753ad3f021fc707ada02"
}

search = GoogleSearch(params)
results = search.get_dict()
# print(results)


json_object = json.dumps(results, indent = 4) 
print(json_object)
