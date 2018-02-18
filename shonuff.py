import shodan

# every time a developer publishes private api keys in a github repo, a kitten cries
SHODAN_API_KEY = "YOUR_API_KEY_HERE"

api = shodan.Shodan(SHODAN_API_KEY)

try:
	results = api.search('apache')

	# Show the results
	#print 'Results found: %s' % results['total']
	for result in results['matches']:
		# print 'IP: %s' % result['ip_str']
	  print '%s' % result['ip_str']
		# print result['data']
		# print ''

except shodan.APIError, e:
	print 'Error: %s' % e

	# print result['data']
	# print ''
