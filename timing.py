import time

def calculate_time(func):
	current  = time.time()
	func()
	end = time.time()
	return print("Total Time " + str(end - current))
