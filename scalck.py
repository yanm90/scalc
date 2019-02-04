# yanm90
# 2019

def user_input(text):
	"""
	Input User Data.
	"""
	while True:
		try:
			number = int(input(text))
		except ValueError:
			print('Incorrect value entered')
			continue
		else:
			break
	return (number)


def need_force(text):
	"""
	Input User Data.
	If incorrect then value is defined.
	"""
	try:
		number = int(input(text))
	except ValueError:
		number = 42
		print('Required distillate strength:', number, 'degrees')
	return (number)


choise = input('\nPress Enter to dilute all distillate\n'
			   'Press "v" and Enter to assign volume of distillate\n')


if choise == 'v':
	n = user_input('Existing distillate strength, degrees: ')
	m = need_force('Required distillate strength, degrees: ')
	z = user_input('Required volume of distillate, ml: ')

	p = z * m / n
	x = z - p

	if x < 0:
		print('\nWater dilution to increase strength is not possible')
	else:
		print('\nNeed pour', int(x), 'ml water and', int(p), 'ml distillate')
else:
	p = user_input('Volume of distillate available, ml: ')
	n = user_input('Existing distillate strength, degrees: ')
	m = need_force('Required distillate strength, degrees: ')

	x = p * n / m - p

	if x > 0:
		print ('Need pour', int(x), 'ml water')
	elif x == 0:
		print ('\nNo need to dilute. You already have', n, 'degrees')
	else:
		print('\nWater dilution to increase strength is not possible')