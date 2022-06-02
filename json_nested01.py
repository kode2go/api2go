#!/usr/bin/env python3

# Import json module
import json
# https://linuxhint.com/search_json_python/

# Define json variable of nested data
nestedData = """{
 "watch":
 {
    "men":{
     "brand":"Titan",
      "price":200
    },
    "women":{
     "brand":"Citizen",
     "price":250
    },
    "kid":{
     "brand":"Blancpain",
     "price":100
    }
 }
}"""

# Load the json data
watchlist = json.loads(nestedData)

# print(watchlist['watch'])

for i in watchlist['watch']:
  print(i)

# Search 'brand' for women
if 'brand' in watchlist['watch']['women']:
 print(watchlist['watch']['women']['brand'])
