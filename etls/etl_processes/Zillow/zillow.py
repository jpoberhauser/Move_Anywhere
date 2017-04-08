import requests
import urllib
from xml.etree import ElementTree as ET

zillow_id = 'X1-ZWz1fg0blk8umj_4dboj'

state = 'wa'
city = 'seattle'
#parameters = {"state": state, "city": city, "childtype" : 'neighborhood'}
#url = "http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=" + zillow_id + "&"
#response = requests.get(url, params = parameters)



url = "http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=" + zillow_id + "&" + 'state=' + state + '&city=' + city + '&childtype=neighborhood'

root = ET.parse(urllib.urlopen(url)).getroot()
print root
print '\n'

items = root.findall('response/list/region')
for item in items:
    print item.find('id').text
    print item.find('name').text
    #print item.find('zindex').text
    # Print the status code of the response.
#print(response.status_code)

# Get the response data as a python object.  Verify that it's a dictionary.

# import xmltodict
#
# with open(response) as fd:
#     doc = xmltodict.parse(fd.read())
#
# print(doc)