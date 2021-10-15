import time

def calculate_time(func):
	def time_it(*args, **kwargs):
		current = time.time()
		func(*args, **kwargs)
		return current - time.time()
	print("Total time " + str(time_it))

