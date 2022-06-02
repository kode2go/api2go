params = {
  "engine": "yelp_reviews",
  "place_id": "-4ofMtrD7pSpZIX5pnDkig",
  "api_key": "###6167704a6638a86b04c8e57e23d5e56aba919c1dc1ca753ad3f021fc707ada02"
}

search = GoogleSearch(params)
results = search.get_dict()
reviews = results['reviews']

json_object = json.dumps(reviews, indent = 4) 
print(json_object)

results_json = json.loads(json_object)

for keyval in results_json:
	# print(keyval['user']['name'])
	print(f"User name {keyval['user']['name']} and rating is: {keyval['rating']}")

