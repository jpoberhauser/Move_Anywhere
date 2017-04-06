
import requests

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

for index in range(10):
    print response.json()['events'][index]['name']['text']
    print response.json()['events'][0]['start']['utc']
