import datetime

year = 2016
start_date = datetime.datetime(year, 1,1)

for delta_year in range(0,50):
	print("{!s}, day: {!s}".format(start_date.year, ((start_date + datetime.timedelta(days=65)).day)))
	start_date = start_date + datetime.timedelta(days=365)
