def parse_input():
	equationin = input("Enter equation:")
	equationparse = equationin.split()
	num1 = equationparse[0]
	operator = equationparse[1]
	num2 = equationparse[2]
	calculator(float(num1), float(num2), operator)


def calculator(number1, number2, operator):
	if operator == '+':
		return number1 + number2
	if operator == '-':
		return number1 - number2
	if operator == '*':
		return number1 * number2
	if operator == '/':
		return number1 / number2
	if operator == '**':
		return number1 ** number2
	else:
		return "Invalid Use"