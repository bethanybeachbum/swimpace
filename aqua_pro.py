# aqua_data.py
import sys
print("Python sys.executable:")
print(sys.executable +  "\n")
print("Python sys.version:")
print(sys.version)

import datetime


today = datetime.datetime.today()
print(f"\n{today:%b %d, %Y}")
print("Welcome to SwimPace")
# name = input("Please enter your name:")
# print(f"\nHello, {name}")

# users = []
users = ["Mark", "Lauri", "Brandon", "Brittany", "Admin" ]
user_login = input("Please type your LogIn User Name: ")
user_login = user_login.title()

if users:
	if user_login in users:
		print(f"\nWelcome back {user_login} ")
	else:
		login_create = input("Would you like to create a login? (Yes or No)")

		if (login_create.title() == "Yes"):
			# what user name do you want?
			# check user name in .upper() and .lower()
			# is the user in the list already?
			# if not:
			users.append(login_create)
			# else:
			# print("User already taken. Please choose another username.")
		else:
			print("You will proceed as a guest")
else:
	print("Congratulations.  You are the first user of this SwimPace.")


# import aqua_data
