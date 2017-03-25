def indexOfAny(str, char_list):
	positions = []
	[ positions.append(idx) for idx, each in enumerate(str) if each in char_list ]
	return positions


print indexOfAny('aabbcc', ['a', 'c'])
print indexOfAny('aabbcc', ['e', 'd'])
print indexOfAny('', ['a',])
