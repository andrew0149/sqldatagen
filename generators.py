from datetime import datetime, date, timedelta
from random import randint, uniform

def generate_autoincrement_numbers(	numbers_count = 1, 
									start_number = 0):
	numbers_arr = []
	for i in range(numbers_count):
		numbers_arr.append(start_number + i)
	return numbers_arr

def generate_int_numbers(	numbers_count = 1,
							istart = 0, iend = 9):
	if (istart > iend):
		print('Borders are set in the wrong order. Order is inverted for you.')
		buffer = istart
		istart = iend
		iend = buffer

	numbers_arr = []
	for i in range(numbers_count):
		numbers_arr.append(randint(istart, iend))
	return numbers_arr

def generate_float_numbers(	numbers_count = 1,
							istart = 0, iend = 1,
							accuracy = 3):
	if (istart > iend):
		print('Borders are set in the wrong order. Order is inverted for you.')
		buffer = istart
		istart = iend
		iend = buffer

	numbers_arr = []
	for i in range(numbers_count):
		generated_number = round(uniform(istart, iend), accuracy)
		numbers_arr.append(generated_number)
	return numbers_arr
	
def generate_list_elements(	elements_count = 1, 
							list_file_path = 'words.txt'):
	with open(list_file_path, 'r') as list_file:
		elements_list = list_file.readlines()

	if (len(elements_list) == 0):
		print('Given file does not contain any elements. Using default words list.')
		return generate_list_elements(elements_count)

	elements_arr = []
	for i in range(elements_count):
		element_index = randint(0, len(elements_list) - 1)
		elements_arr.append(elements_list[element_index].replace('\n', ''))
	return elements_arr

def generate_phone_numbers(	numbers_count = 1,
							phone_format = '+7 (nnn) nnn-nn-nn'):
	digits_count = phone_format.count('n')
	mask = phone_format.split('n')

	phone_numbers_arr = []
	for i in range(numbers_count):
		digits = mask.copy()
		for j in range(digits_count):
			digits.insert(2 * j + 1, str(randint(0,9)))
		phone_numbers_arr.append(''.join(digits))
	return phone_numbers_arr

def generate_dates(	dates_count = 1, 
					istart = date(1970, 1, 1), iend = date.today()):
	days_count = (iend - istart).days
	if (days_count < 0):
		print('Dates are set in the wrong order. Order is inverted for you.')
		istart = iend
		days_count *= -1

	dates_arr = []
	for i in range(dates_count):
		day_index = randint(0, days_count)
		date_generated = istart + timedelta(days = day_index)
		dates_arr.append(date_generated.strftime('%Y-%m-%d'))
	return(dates_arr)

def generate_datetimes(	datetimes_count = 1,
						istart = datetime(1970, 1, 1, 0, 0, 0), iend = datetime.now()):
	datetime_delta = iend - istart 
	seconds_count = (datetime_delta.seconds + 60 * 60 * 24 * datetime_delta.days)

	if (seconds_count < 0):
		print('Datetimes are set in the wrong order. Order is inverted for you.')
		istart = iend
		seconds_count *= -1

	datetimes_arr = []
	for i in range(datetimes_count):
		second_index = randint(0, seconds_count)
		datetime_generated = istart + timedelta(seconds = second_index)
		datetimes_arr.append(datetime_generated.strftime('%Y-%m-%d %H:%M:%S'))
	return datetimes_arr