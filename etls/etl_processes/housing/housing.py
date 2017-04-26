from selenium import webdriver
import selenium
from selenium.webdriver.support.ui import Select
from geopy.geocoders import Nominatim
import json


def get_props(city, pay_type, driver):
    """
    :param city: city to search for formatted 'city, state abbr.'
    :param pay_type: either 'apartments' or 'realestateandhomes-search' - plugged directly into query string
    :return: returns list of dicts where each dictionary is an individual property
    """
    # Parse city
    print city, pay_type
    city, state = city.split(",")
    search_city = city
    state = state[1:]
    if ' ' in city:
        search_city = "-".join(city.split())

    search_type = "rent" if pay_type == 'apartments' else "buy"
    query_url = 'https://realtor.com/'+pay_type+'/'+search_city+"_"+state+'?pgsz=50'
    driver.get(query_url)

    num_pages = 50
    prop_vals = []
    for i in range(num_pages): # for each
        # print i,
        # need to put this in a loop to go to next page after pulling info
        props = driver.find_elements_by_class_name('srp-item-details')
        # driver.implicitly_wait(10)
        for prop in props:
            # print prop
            try:
                pv = {}
                pv['price'] = prop.find_element_by_class_name('srp-item-price').text
                pv['address'] = prop.find_element_by_class_name('listing-street-address').text
                pv['city'] = c.split(",")[0]
                pv['zip'] = prop.find_element_by_class_name('listing-postal').text
                pv['apt_name'] = prop.find_element_by_class_name('listing-community').text
                pv['type'] = search_type
                # pv['prop_type'] = 'apartment'
                prop_vals.append(pv)
            except:
                continue
        try:
            driver.find_element_by_css_selector('a.next').click()
        except:
            break

    return prop_vals

def get_data():
    cities = ['San Francisco, CA','Chicago, IL','Boston, MA','Miami, FL','New York, NY','Austin, TX']
    types = ['apartments','realestateandhomes-search']

    driver = webdriver.Chrome('/usr/local/bin/chromedriver')

    res_list = []
    for c in cities:
        for t in types:
            res_list += get_props(c, t, driver)

    driver.close()

    return res_list


if __name__ == "__main__":
    get_data()



