import foursquare
from _creds import *
from time import sleep
import pprint as pp

#client = foursquare.Foursquare(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
client = foursquare.Foursquare(access_token=ACCESS_TOKEN)
query= client.venues.search(params={'query': 'coffee','ll': '35.6891975,51.3889736'})
#print type (query) is dict
pp.pprint (query)

#for i in client.venues.search(params={'query': 'coffee','ll': '35.6891975,51.3889736'}):
	#sleep(0.5)
	#rint i
	#pprint.pprint i