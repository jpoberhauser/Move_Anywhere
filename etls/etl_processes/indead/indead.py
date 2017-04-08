from indeed import IndeedClient 

def get_data():
    client = IndeedClient('7381316591612982')
    params = {
        'q' : "front end engineer",
        'l' : "austin",
        'userip' : "172.68.141.95",
        'useragent' : """Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36
                        (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36""",
        'limit' : 25
    }
    search_response = client.search(**params)

    cities = ['New York, NY','Austin, TX','San Francisco, CA','Boston, MA','Chicago, IL','Miami, FL']
    jobs = ['Front End Engineer','Back End Engineer','Data Science','Product Management','Director of Engineering',
           'Data Engineer','Data Analyst','Accounting','Marketing','Finance','Nurse','Doctor','Lawyer','Paralegal',
           'sales','customer_service','human resources','executive assistant','operations','teacher','maintenance',
           'security guards']
    
    res_list = ['jobs']
    for c in cities:
        for j in jobs:
            params = {
                'q' : j,
                'l' : c,
                'userip' : "172.68.141.95",
                'useragent' : """Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36
                                (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36""",
                'limit' : 25
            }
            search_response = client.search(**params)
            for res in search_response['results']:
                job_dict = {}
                if not res['expired']:
                    job_dict['city'] = res['city']
                    job_dict['date_posted'] = res['date']
                    job_dict['company'] = res['company']
                    job_dict['title'] = res['jobtitle']
                    job_dict['url'] = res['url']
                    job_dict['job_id'] = res['jobkey']
                    job_dict['state'] = res['state']
                    job_dict['snippet'] = res['snippet']
                res_list.append(job_dict)

    return res_list

if __name__ == "__main__":
	get_data()