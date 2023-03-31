from enum import IntEnum
from datetime import date, datetime
from cutie import select
from tabulate import tabulate
from generators import *

class column_data_types(IntEnum):
	Autoincrement = 1
	Integer = 2
	Float = 3
	List_element = 4
	Name = 5
	Surname = 6
	Full_name = 7
	Phone_number = 8
	Date = 9
	Date_with_timestamp = 10

def is_string_empty(string):
	return string.replace(' ', '') == ''

def parse_input_int(input_int, default_value):
	try:
		return int(input_int)
	except Exception:
		if not is_string_empty(input_int):
			print('Input invalid! Using default value.')
		return default_value

def parse_input_float(input_float, default_value):
	try:
		return float(input_float)
	except Exception:
		if not is_string_empty(input_float):
			print('Input invalid! Using default value.')
		return default_value

def parse_input_date(input_date, default_value):
	try:
		return datetime.strptime(input_date, '%Y-%m-%d').date()
	except Exception:
		if not is_string_empty(input_date):
			print('Input invalid! Using default value.')
		return default_value

def parse_input_datetime(input_datetime, default_value):
	try:
		return datetime.strptime(input_datetime, "%Y-%m-%d %H:%M:%S")
	except Exception:
		if not is_string_empty(input_datetime):
			print('Input invalid! Using default value.')
		return default_value


def generate_requested_data(rows_count, column_data_type, column_name = ''):	
	if column_data_type == column_data_types.Autoincrement:
		start_number_str = input(
			f'Enter the start index for an autoincrement column "{column_name}" \n' + 
			'[default: 0]: '
			)
		start_number = parse_input_int(start_number_str, 0)

		return generate_autoincrement_numbers(rows_count, start_number)

	if column_data_type == column_data_types.Integer:
		istart_str = input(
			f'Enter the interval START number for random int column "{column_name}" \n' + 
			'[default: 0]: '
			)
		istart = parse_input_int(istart_str, 0)

		iend_str = input(
			f'Enter the interval END number for random int column "{column_name}" \n' + 
			'[default: 9]: '
			)
		iend = parse_input_int(iend_str, 9)

		return generate_int_numbers(rows_count, istart, iend)

	if column_data_type == column_data_types.Float:
		istart_str = input(
			f'Enter the interval START number for random float column "{column_name}" \n' + 
			'[default: 0.0]: '
			)
		istart = parse_input_float(istart_str, 0.0)

		iend_str = input(
			f'Enter the interval END number for random float column "{column_name}" \n' + 
			'[default: 1.0]: '
			)
		iend = parse_input_float(iend_str, 1.0)

		accuracy_str = input(
			f'Enter the accuracy for generated float column "{column_name}" \n' + 
			'[default: 3]: ')
		accuracy = parse_input_int(accuracy_str, 3)

		return generate_float_numbers(rows_count, istart, iend, accuracy)

	if column_data_type == column_data_types.List_element:
		list_file_path = input(
			f'Enter Path to file containing words for column "{column_name}" \n' + 
			'[default: lists/words.txt]: '
			)
		try:
			list_file = open(list_file_path, 'r')
			list_file.close()
		except Exception as e:
			print(e.args[0])
			if not is_string_empty(list_file_path):
				print('Input invalid! Using default value.')
			list_file_path = 'lists/words.txt'

		return generate_list_elements(rows_count, list_file_path)

	if column_data_type == column_data_types.Name:
		return generate_list_elements(rows_count, "lists/names.txt")

	if column_data_type == column_data_types.Surname:
		return generate_list_elements(rows_count, 'lists/surnames.txt')

	if column_data_type == column_data_types.Full_name:
		return [
				name + ' ' + surname 
				for name, surname 
				in zip(	generate_requested_data(rows_count, column_data_types.Name), 
						generate_requested_data(rows_count, column_data_types.Surname)) 
				]

	if column_data_type == column_data_types.Phone_number:
		phone_format = input(
			f'Enter the format for phone numbers column "{column_name}" \n' +
			'e.g. "+3nn nnn nn nnn" where n stands for random digit \n' + 
			'[default: "+7 (nnn) nnn-nn-nn"]: ')
		
		return generate_phone_numbers(	rows_count, 
										"+7 (nnn) nnn-nn-nn" 
											if is_string_empty(phone_format) 
											else phone_format)

	if column_data_type == column_data_types.Date:
		istart_str = input(
			f'Enter the interval START date for random dates column "{column_name}" \n' + 
			'[default: "1970-01-01"]: '
			)
		istart = parse_input_date(istart_str, date(1970, 1, 1))

		iend_str = input(
			f'Enter the interval END date for random dates column "{column_name}" \n' + 
			'[default: Current date]: '
			)
		iend = parse_input_date(iend_str, date.today())
		
		return generate_dates(rows_count, istart, iend)

	if column_data_type == column_data_types.Date_with_timestamp:
		istart_str = input(
			f'Enter the interval START date with timestamp for random dates column "{column_name}" \n' + 
			'[default: "1970-01-01 00:00:00"]: '
			)
		istart = parse_input_datetime(istart_str, datetime(1970, 1, 1, 0, 0, 0))

		iend_str = input(
			f'Enter the interval END date with timestamp for random dates column "{column_name}" \n' + 
			'[default: Current date and time]: '
			)
		iend = parse_input_datetime(iend_str, datetime.now())
		
		return generate_datetimes(rows_count, istart, iend)


with open('logo.txt', 'r', encoding = 'UTF-8') as logo:
	print(logo.read())

print()

rows_count_str = input('Enter the number of rows you need [default: 100]: ')
rows_count = parse_input_int(rows_count_str, 100)

print()

column_names = [
	column_name 
	for column_name 
	in input('Enter the names of columns you need, separating them by spaces:\n').split(' ') 
		if column_name != ''
	]

columns = []
for column in column_names:

	print(f'Select the data type of column "{column}" : ')

	data_type_options = [str(data_type.name).replace('_', ' ') 
							for data_type 
							in column_data_types]
	column_data_type = select(data_type_options)

	print()

	columns.append(generate_requested_data(rows_count, column_data_type + 1, column))

print()

delimiter = input(
	'Enter the delimiter to be used in the output .CSV file\n' + 
	'[default: ","]: '
	)
if is_string_empty(delimiter):
	delimiter = ','

print()

output_file_path = input(
	'Enter the Path for the output .CSV file to be written into \n' + 
	'[default: "output.csv"]: '
	)

with open(
	'output.csv' 
		if is_string_empty(output_file_path) 
		else output_file_path, 
	'w'
) as output_file:
	for column in range(len(column_names)):
		output_file.write(column_names[column])
		if column != len(column_names) - 1:
			output_file.write(delimiter)
	for row in range(rows_count):
		output_file.write('\n')
		for column in range(len(column_names)):
			output_file.write(str(columns[column][row]))
			if column != len(column_names) - 1:
				output_file.write(delimiter)

print('Do you want to preview your table? ')
if select(['Yes', 'No']) == 0:
	print()

	table_preview = list(zip(*columns))

	is_table_big = rows_count > 10
	if is_table_big:
		table_preview = table_preview[:9]
		table_preview.append(['...' for column in column_names])	
	
	print(tabulate(table_preview, headers = column_names))