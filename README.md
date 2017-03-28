# Move Anywhere


##Sections:

* What will I do? (jobs)
* Where will I live? (How much will I need to make to keep my 200 sqft, 2 bedroom apt?)
* Who else lives there?
* What is the weather there today?
* What will I do on the weekends?
* What will my commute be?
* Access to Doctors?
* Where will my kids go to school?
* I love to jog, where can I jog? (I like crossfit, where can I go to crossfit?)




##Data Sources:
If i move there, how would i move around, how can i get a job, how much will i make, how much will i NEED to make to get a 1 bedroom apt, what events are happening on the weekends, what is the demographic makeup, what are the public schools, quality of the air, gyms, restaurants

Data Sources:
(bike sharing, muni & public transport data), (indeed, linkedin), (padmapper, craigslist, airbnb), (twitter, local newspaper, timeout magazine), (census-data), (public school quality data), (zagat)






Steps:
Data Aggregation (probably the hardest part)

    lets start with the sources that are general to ALL cities, and filter them out, (padmapper, craiglist, indeed)


Cities:
SF:
(transportation)
http://www.bayareabikeshare.com/open-data

NY:
(transportation)
https://www.citibikenyc.com/system-data

Austin:


Links:

https://www.timeout.com/austin
https://www.indeed.com/jobs?q=data+science&l=San+Francisco%2C+CA


## Project Specs Checlist:

[ ] Server on EC2

[ ] Create a service that provides an output JSON based on your input

    http://stackoverflow.com/questions/29656866/python-beautiful-soup-and-cron

[ ] Keep a service that pulls info, processes, and outputs only aggregated, useful info.

[ ] Your service's API documentation will be public and self explanatory

[ ] A testing framework for demonstrating the app is required

[ ] A user interface is not required (maybe a simple white box is enough)
