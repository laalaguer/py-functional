# 1. Input a list of names
# 2. Get rid of single letter name
# 3. Capitalize each name
# 4. Output a string, with each name seperated by comma

def clean_up(name):
	if len(name) < 2:
		return None
	else:
		return name

def capitalize(name):
	return name.title()

def concat(names):
	return ','.join(names)


names = ['john', 'w', 'a', 'b', 'Mary Watson']
formatted_names = [ capitalize(each) for each in names if clean_up(each) ]
print concat(formatted_names)
