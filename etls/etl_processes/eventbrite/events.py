
import requests
import datetime


def get_data():
    cities = ['New York, NY','Austin, TX','San Francisco, CA','Boston, MA','Chicago, IL','Miami, FL']

    res_list = ['events']
    for city in cities:
        city = city.replace(" ", "+")
        print city
        url = "https://www.eventbriteapi.com/v3/events/search/?q="+city
        response = requests.get(
            url,
            headers = {
                "Authorization": "Bearer FOFJGDOSGZSEJTYSHPAX",
            },
            verify = True,  # Verify SSL certificate
        )
        for index in response.json()['events']:
            event_dict = {}
            event_dict['city'] = city
            event_dict['event_name'] = index['name']['text']
            event_dict['event_description'] = index['description']['text']
            event_dict['event_date'] = str(datetime.datetime.strptime(index['start']['utc'], "%Y-%m-%dT%H:%M:%SZ").date())
            res_list.append(event_dict)


if __name__ == "__main__":
    get_data()
