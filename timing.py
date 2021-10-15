import time

def calculate_time(func):
	current  = time.time()
	func()
	end = time.time()
	print("Total time " + str(end - current))
	return func
