# Given a string, and another char set.
# Find the accurance of char in the string, log the positions.

def indexOfAny(str, char_list):
	positions = []
	# warning: below will create an acutal list, but will be gc immediately.
	[ positions.append(idx) for idx, each in enumerate(str) if each in char_list ]
	return positions


print indexOfAny('aabbcc', ['a', 'c'])
print indexOfAny('aabbcc', ['e', 'd'])
print indexOfAny('', ['a',])

# Thinking:
# 1. indexOfAny() didn't mutate str and char_list, which is pure function. (no side effects)
# 2. indexOfAny() will create a list, which is memory occupation. But gladly it will be gc.
# 3. We use enumerate() to get index number, this is considered Pythonic.