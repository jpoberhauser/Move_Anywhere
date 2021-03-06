import httplib



# use this server for dev

SERVER = 'localhost:5000'



# use this server for prod, once it's on ec2

# SERVER = 'xxxxx.aws.ec2.com:5000'





def get_default():

    out = dict()

    h = httplib.HTTPConnection(SERVER)

    # want the url to look something like this

    # 'http://localhost:5000/restaurants/borough/counts'

    h.request('GET', 'http://'+SERVER)

    resp = h.getresponse()

    out = resp.read()

    return out



def get_resource(var):

    out = dict()

    h = httplib.HTTPConnection(SERVER)

    # want the url to look something like this

    # 'http://localhost:5000/resource/<var>'

    h.request('GET', 'http://'+SERVER+'/resource/'+var+'?user=steve')

    resp = h.getresponse()

    out = resp.read()

    return out





if __name__ == '__main__':

    print "************************************************"

    print "test of my flask app running at ", SERVER

    print "created by Bob Ross"

    print "************************************************"

    print " "

    print "******** default **********"

    print get_default()

    print " "

    print "******** resource **********"

    print get_resource('test')
