
# THE EXPLANATION IS IN THE DOCUMENTATION MODULE, ALL THE MODULES AND FUNCTIONS ARE THERE.
# Green House Monitoring System - Server Module
This module uses Google app engine and webapp2 framework, it's necessary to deploy this app to the cloud to use the application.

This part have the handlers for the database and the json parser funtions to print what data is entering to the database also
this part have the templates for the web site of the application.

The final user is going to be able to interact with the database of the application to see all the measures on line graphic's in a web page. The user also can be able to interact with the application to modify if he need to change the maximun and minimun measure's rate for the sms alert system.

#Getting Started
These instructions will get a copy of the project up and deployed on a live system (in this case Google Cloud Platform).

##Prerequisites
You need to have a Google account to deploy the app on Google Cloud Platform

To make this application work you need create a new Cloud Platform Console project or use one project ID of an existing project form the [Google Cloud Platform Console](https://console.cloud.google.com/iam-admin/projects?_ga=1.45758564.1991591100.1474994604)

Next you need to download and install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/quickstart-windows) then start the SDK shell and initilize it, these instruction can be found in the previous url.

## Deployment
Clone this application to your local machine.

Then you have to deploy the application using the SDK shell, first you have to move to the repository location:

```
cd IS-Repo-Equipo2/appengine
```

and then use the next command: 

 ```
 gcloud app deploy
```
The SDK would ask if you want to deploy the application to the Google Cloud Platform so you can ask yes to continue, and that's all to have the application functional on the server.

## Functions

- alta_sensor: This function save the entire data of one sensor on the database
- get_today_measures: A function to obtain the measures of one day
- get_this_week_measures: Used to obtain the measures of all the week
- get_measures_between_dates: This function works to obtain measures between to date
- get_all alerts: This function return all the measure's alerts 
- get_min_Value: The function return the minimun value of of a certain type of measure
- get_Max_Value: The function return the maximun value of of a certain type of measure
- new_Alert: Used to save a new measure alert to the system

## Built With
* [Google App Engine](https://cloud.google.com/appengine/docs)
* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [Twilio](https://www.twilio.com/) - voice & video messaging
* [Amcharts](https://www.amcharts.com/) - JavaScript Charts & Maps
	
##Authors
 - G. Karosuo
 - Islas Alejandro
 - Gutierrez David F.
 - Gutierrez Martin
 - Blanco Erick V.

