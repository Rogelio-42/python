def tripler(func):
	def three(*args, **kwargs):
		func(*args, **kwargs)
		func(*args, **kwargs)
		func(*args, **kwargs)
		return
	return three
