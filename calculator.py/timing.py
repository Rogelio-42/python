import time

def calculate_time(func):
	def time_it():
		current = time.time()
		func()
		return current - time.time()
	print("Total time " + str(time_it))

