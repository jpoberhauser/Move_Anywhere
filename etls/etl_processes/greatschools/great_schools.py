import requests
import urllib
from xml.etree import ElementTree as ET

gs_key = 'odxpxezbavaey2hbsst8ogxx'

# state = 'NY'   #state
# q = 'NewYork'  #seach query string
# levelCode = 'elementary-schools'    #level of school: elementary-schools, middle-schools, or high-schools
# limit = '200'         #maximum number or results to return
#
#
# url = 'http://api.greatschools.org/search/schools?key=' + gs_key + '&state=' + state + '&q=' + q + '&limit=' + limit
# print(url)
# root = ET.parse(urllib.urlopen(url)).getroot()
# print root
# print '\n'


def get_data():
    gs_key = 'odxpxezbavaey2hbsst8ogxx'
    city_state = [['NewYork', 'NY'],['Austin', 'TX'],['SanFrancisco', 'CA'],['Boston', 'MA'],['Chicago', 'IL'],['Miami', 'FL']]

    res_list = ['schools']



    for item in city_state:
        school_dict = {}
        q = item[0]
        state = item[1]
        url = 'http://api.greatschools.org/search/schools?key=' + gs_key + '&state=' + state + '&q=' + q
        root = ET.parse(urllib.urlopen(url)).getroot()
        items = root.findall('school')
        if q == 'NewYork':
            q = 'New York'
        if q == 'SanFrancisco':
            q = 'San Francisco'
        for item in items:
            try:
                school_dict['gsId']= item.find('gsId').text
            except:
                school_dict['gsId']= 'NULL'
            try:
                school_dict['name']= item.find('name').text
            except:
                school_dict['name'] = 'NULL'
            try:
                school_dict['type'] = item.find('type').text
            except:
                school_dict['type'] = 'NULL'
            try:
                school_dict['gradeRange']= item.find('gradeRange').text
            except:
                school_dict['gradeRange'] = 'NULL'
            try:
                school_dict['enrollment'] = item.find('enrollment').text
            except:
                school_dict['enrollment'] = 'NULL'
            try:
                school_dict['parentRating'] = item.find('parentRating').text
            except:
                school_dict['parentRating'] = 'NULL'
            try:
                school_dict['city']= q
            except:
                school_dict['city'] = 'NULL'
            try:
                school_dict['state']= state
            except:
                school_dict['state'] = 'NULL'
            try:
                school_dict['address'] =  item.find('address').text
            except:
                school_dict['address'] = 'NULL'
            try:
                school_dict['phone'] = item.find('phone').text
            except:
                school_dict['phone'] = 'NULL'
            try:
                school_dict['lat']= item.find('lat').text
            except:
                school_dict['lat'] = 'NULL'
            try:
                school_dict['lon'] = item.find('lon').text
            except:
                school_dict['lon'] = 'NULL'
            try:
                school_dict['overviewLink']=item.find('overviewLink').text
            except:
                school_dict['overviewLink'] = 'NULL'
            try:
                school_dict['ratingsLink'] = item.find('ratingsLink').text
            except:
                school_dict['ratingsLink'] = 'NULL'
            try:
                school_dict['reviewsLink'] = item.find('reviewsLink').text
            except:
                school_dict['reviewsLink'] = 'NULL'
        res_list.append(school_dict)
    return res_list




if __name__ == "__main__":
    schools = get_data()


