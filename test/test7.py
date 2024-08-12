import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('/tmp/metrics.json', 'w') as outfile:
    json.dump(data, outfile)

with open('/tmp/metrics.json') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')    

'''
{
	"people": [{
		"name": "Scott",
		"website": "stackabuse.com",
		"from": "Nebraska"
	}, {
		"name": "Larry",
		"website": "google.com",
		"from": "Michigan"
	}, {
		"name": "Tim",
		"website": "apple.com",
		"from": "Alabama"
	}]
}
'''