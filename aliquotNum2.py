# Improved version.
# Generator Pattern, use generator instead of a list.

def is_factor(potential, number):
	''' decide if potential is the factor of number '''
	if number % potential == 0:
		return True
	else:
		return False

def factors(number):
	''' return all factors in a number '''
	# warning: we use () instead of [], then generatos is returned instead of a list.
	return ( each for each in xrange(1, number) if is_factor(each, number) )

def factors2(number):
	''' this is the same as factors() above, just in more formal way.
		take notice on the yield keyword
	'''
	for each in xrange(1,number):
		if is_factor(each, number):
			yield each

def factors_sum(factors):
	''' sum the factors '''
	return sum(factors)

def classify(number):
	''' classify a number based on aliquot sum '''
	m_factors = factors(number) # see factors() function
	m_sum = factors_sum(m_factors) # iterate over a list.
	if m_sum > number:
		return 'abdundant'
	
	if m_sum < number:
		return 'deficient'

	return 'perfect'

def classify2(number):
	''' classify a number based on aliquot sum '''
	m_factors = factors2(number) # see the factors2() function
	m_sum = factors_sum(m_factors) # iterate over a generator.
	if m_sum > number:
		return 'abdundant'
	
	if m_sum < number:
		return 'deficient'

	return 'perfect'

print classify(6)
print classify(10)
print classify(28)

print classify2(6)
print classify2(10)
print classify2(28)

# Thinking:
# 1. factors() will return a generator instead of a list. It can be iterated on, such as in a for() loop.
# 2. Comparing to a list (object), we returned a function (generator). 
# 3. So, in FP world, a function can also be an argument of another function.
# 4. In other words, we don't need an immediate result, we need a potential. This is called 'lazy evaluaion' in FP.
# 4. Still we do not have cache here. Because cache is external state of functions.