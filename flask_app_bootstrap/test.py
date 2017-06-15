# Project Name: MoveAnywhere

# authors are Graham Mcalister, Eric Lehman, Francisco Calderon, Valerie Amoroso, Juan Pablo Oberhauser
#This tester scriot get our resources from a postgres database.
#There are several resources, all of which we request via this script.
#For testing purposes, we set the limit of the queries to ten observations, in the real application,
#these will be larger than the ones displayed here.

# use this server for prod, once it's on ec2
SERVER = 'http://ec2-34-208-49-29.us-west-2.compute.amazonaws.com:5000'
import requests

def get_resource(var):
    return requests.get(SERVER + '/' + var).content


if __name__ == '__main__':
    print "************************************************"
    print "************************************************"
    print "test of my flask app running at ", SERVER
    print "created by Pablo, Graham, Eric, Valerie, Francisco"
    print "************************************************"
    print "************************************************"
    print " "
    print " "
    print " "
    print "************************************************"
    print "******** First Resource: JOBS **********"
    print "************************************************"
    print get_resource('jobs')
    print " "
    print " "
    print " "
    print "************************************************"
    print "******** Second Resource: Schools **********"
    print "************************************************"
    print get_resource('schools')
    print " "
    print " "
    print " "
    print "************************************************"
    print "******** Third Resource: Events **********"
    print "************************************************"
    print get_resource('events')
    print " "
    print " "
    print " "
    print "************************************************"
    print "******** End of Testing Script **********"
    print "************************************************"
