import random


def case_usage(day_number):
	match day_number:
		case 1:
			return 'Monday'
		case 2:
			return 'Tuesday'
		case 3:
			return 'Wednesday'
		case 4:
			return 'Thursday'
		case 5:
			return 'Friday'
		case 6:
			return 'Saturday'
		case 7:
			return 'Sunday'
		case _:
			return 'You entered invalid number'

	

print(case_usage(random.randint(1, 10)))
