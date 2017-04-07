import requests
import urllib
from xml.etree import ElementTree as ET

gs_key = 'odxpxezbavaey2hbsst8ogxx'

state = 'CA'   #state
q = 'SanFrancisco'  #seach query string
levelCode = 'elementary-schools'    #level of school: elementary-schools, middle-schools, or high-schools
limit = '50'         #maximum number or results to return


url = 'http://api.greatschools.org/search/schools?key=' + gs_key + '&state=' + state + '&q=' + q + '&levelCode=' + levelCode + '&limit=' + limit
print(url)
root = ET.parse(urllib.urlopen(url)).getroot()
print root
print '\n'

items = root.findall('school')
for item in items:
    try:
        print item.find('gsId').text
    except:
        print 'No Value'
    try:
        print item.find('name').text
    except:
        print 'No Value'
    print item.find('type').text
    print item.find('gradeRange').text
    print item.find('enrollment').text
    try:
        print item.find('parentRating').text
    except:
        print 'No Value'
    print item.find('city').text
    print item.find('state').text
    print item.find('address').text
    print item.find('phone').text
    print item.find('lat').text
    print item.find('lon').text
    print item.find('overviewLink').text
    print item.find('ratingsLink').text
    print item.find('reviewsLink').text
