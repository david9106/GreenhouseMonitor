## Makes an aproximation, how many access will be done to the Datastore in certain amount of time
# IT DOESN'T SHOW NUMBER OF OPERATIONS
#	saving data each 20 secs
#	retrieving all data each 20 secs

import matplotlib.pyplot as plt

total = 0 #Aprox total of access
hours = 24 #3 continuos hours of access
sec_interval = 275 #each sec_interval seconds
cyc_amount = hours*60*60/sec_interval;
cyc_per_hour = 3600 / sec_interval #How many cycles pero hour

time_array = [] #Time to plot
amount_access = [] #Dots to plot each hour
plt.title("Datastore access, 1 in, all out each {!s} seconds".format(sec_interval))
plt.grid(True) #With grid
plt.ylabel("Number of access, NOT OPERATIONS")
plt.xlabel("Time (hours)")

hour_counter = 0
for cycle in range(1,cyc_amount+1):
	total = total + cycle + 1
	if cycle % cyc_per_hour == 0: #Saves the value per hour		
		time_array.append(hour_counter)
		hour_counter = hour_counter +1
		amount_access.append(total)
		print("total: {!s}, cycle: {!s}, constant: 1".format(total, cycle))
		
plt.plot(time_array, amount_access, 'bo-')
plt.show()
