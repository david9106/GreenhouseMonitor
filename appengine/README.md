# IS-Repo-Equipo2
This module uses Google app engine and webapp2 framework, it's necessary deploy this app to the cloud to use the application.
# Monitoring System for Geen House
This part have the handlers for the database and the json parser funtions to print what data is entering to the database also
this part have the templates for the web site of the application

The final user is going to be able to interact with the database of the application to see all the measures on line graphic's in a web page. The user also can be able to interact with the application to modify if he need to change the maximun and minimun measure's rate for the sms alert system

## Functions

- alta_sensor: This function save the entire data of one sensor on the database
- get_today_measures: A function to obtain the measures of one day
- get_this_week_measures: Used to obtain the measures of all the week
- get_measures_between_dates: This function works to obtain measures between to date
- get_all alerts: This function return all the measure's alerts 
- get_min_Value: The function return the minimun value of of a certain type of measure
- get_Max_Value: The function return the maximun value of of a certain type of measure
- new_Alert: Used to save a new measure alert to the system


