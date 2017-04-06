
import requests
import datetime

city = "New York City"

city = city.replace(" ", "+")
url = "https://www.eventbriteapi.com/v3/events/search/?q="+city
response = requests.get(
    url,
    headers = {
        "Authorization": "Bearer FOFJGDOSGZSEJTYSHPAX",
    },
    verify = True,  # Verify SSL certificate
)

response.json()['pagination']['object_count']


for index in range(2):
    print response.json()['events'][index]['name']['text']
    #print response.json()['events'][index]['description']['text']
    print str(datetime.datetime.strptime(response.json()['events'][0]['start']['utc'], "%Y-%m-%dT%H:%M:%SZ").date())
