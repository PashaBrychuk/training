#count_statuses.py


def count_status():
	count = 0
	with open('gw_messages.log') as f:

		for line in f:
			if "TID-2182497-320000001" in line:
				count = count +1
	return count


print count_status()

