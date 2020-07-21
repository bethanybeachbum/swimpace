# aqua_data.py

# import datetime
# today = datetime.datetime.today()
# print(f"{today:%b %d, %Y}\n")

from time import time, ctime
# import time
t = time()
print(f"The current date and time is: {ctime(t)}")
print("\n")
# Following converts time to a string
# print(time.asctime(time.gmtime()))






today_times = []

mark_best_times = { 1592419553.2260108 : 60.0, 1592419311.2260108 : 59.9, 592420211.2260108 : 59.8,   592419111.2260108 : 58.0, 1592421350.7680042 : 57.0, 1592421300.086897 : 56.0,}
lauri_best_times = { 1592419053.2260108 : 51.1, 1592418311.2260108 : 51.4, 592420210.2260108 : 51.7,   592419111.2260107 : 52.0, 1592421349.7680042 : 57.1, 1592421300.086897 : 56.1,}
brandon_best_times = { 1592419153.2260108 : 51.2, 1592418311.2260108 : 51.5, 592420209.2260108 : 51.8,   592419111.2260106 : 53.0, 1592421349.7680042 : 57.2, 1592421300.086896 : 56.2,}
brittany_best_times = { 1592418553.2260108 : 51.3, 1592417311.2260108 : 51.6, 592420208.2260108 : 51.9,   592419111.2260106 : 54.0, 1592421347.7680042 : 57.3, 1592421300.086895 : 56.3,}

print("\nDictionary keys ONLY of Mark's times: ")
print("They are converted from float time to character time: \n")
for each_time in mark_best_times.values():
	print(ctime(each_time))

print("\n ########## break #1 ############\n")
print("\nDictionary keys and values of Mark's times: ")
for k, v in mark_best_times.items():
	print( ctime(k) , v )

print("\n ########## break #2 ############\n")
print( "sort attempt on times")

for values in sorted(mark_best_times.values()):
	print(values)


print("\n ########## break #3 ############\n")

all_best_times = [mark_best_times, lauri_best_times, brittany_best_times, brandon_best_times]

for each in all_best_times:
	print(f"\n") 
	print(each)

print("\nbreak #3\n")

joe_best_times = [1]
if (joe_best_times):
	print(f"\nDo you want to add your new lap times to your best times list? (yes or no")
	answer = input()
	if(answer == "yes"):
		new_time = input("What is your new time?")
		joe_best_times[0] = new_time
		print(joe_best_times[0])
# print("Do you want to add your new lap times to your best times list?")	

