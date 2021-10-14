def multiply_list(list):
	result = 1
	for i in  list:
		if isinstance(i, int):
			result = result*i
		else:
			return "Invalid input"
	return result
