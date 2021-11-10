def powersum(power, *args):
	'''Возвращает сумму аргументов, возведенных в указанную степень.'''
	total = 0
	for i in args:
		total += pow(i, power)
	return total
print(powersum(2, 3, 4))
print(powersum(2, 10))
