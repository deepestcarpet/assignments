state = "login"
carpets = ["dnc", "ijklk", "deepestcarpet", "juicecan", "ceepestdarpet"]
while state == "login": # me when you're logging in
	user = str(input("Username: ")) # who are u
	level = int(input("Level: ")) # what are u made of
	exp = float(input("Experience points: ")) # how much
	confirm = int(input(f"You are {user}, level {level}, with {exp} XP. Correct? (0/1)\n")) # are you really???
	userCheck = False
	for i in range(len(carpets)):
		if user == carpets[i-1]:
			userCheck = True # YOU CAN'T BE ME THAT'S RACIST
	if confirm and userCheck == True:
		print("Only I can be me! Heck off!") # you cant be me because im me
	if confirm and userCheck == False:
		print(f"Welcome back, {user}.")
		state = "menu" # doesnt actually do anything
	if not confirm:
		print("What!!!!!") # restarts process because u LIED about urself
