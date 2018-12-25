
#coins with 5 and 7

def  change(amount):
	assert(24 <= amount <= 1000)
	if amount == 24:
		return [5,5,7,7]
	if amount == 25:
		return [5,5,5,5,5]
	if amount == 26:
		return [5,7,7,7]
	if amount == 27:
		return [5,5,5,5,7]
	if amount == 28:
		return [7,7,7,7]
	if amount == 29:
		return [5,5,5,7,7]
	if amount == 30:
		return [5,5,5,5,5,5]

	coins = change(amount - 7)
	coins.append(7)
	return coins
