# aliquot number is the sum of factors of a number:
# 1,2,3 are factors of 6 (except 6 itself)
# aliquot sum is: 1+2+3=6
# if aliquot == number, perfect
# if aliquot < number, deficient
# if aliquot > number, abdundant

# How to decide the classification of a any given number?

def is_factor(potential, number):
	''' decide if potential is the factor of number '''
	if number % potential == 0:
		return True
	else:
		return False

def factors(number):
	''' return all factors in a number '''
	# warning: below will create an actual list, memory issue!
	return [ each for each in xrange(1, number) if is_factor(each, number) ]

def factors_sum(factors):
	''' sum the factors '''
	return sum(factors)

def classify(number):
	''' classify a number based on aliquot sum '''
	m_factors = factors(number)
	m_sum = factors_sum(m_factors)
	if m_sum > number:
		return 'abdundant'
	
	if m_sum < number:
		return 'deficient'

	return 'perfect'

print classify(6)
print classify(10)
print classify(28)

# Thinking:
# 1. all the functions here don't mutate the input args (no side effect)
# 2. factors() function does not have a cache, slow! If we know 6 has factors [1,2,3]
# e.g. When we see 12, we know it has a factor 6, then 12 must have [1,2,3] as its factors by default.
# 3. factors() function, xrange(1, number) wise? Shall be xrange(1, number/2) better.
# 4. factors() function will create a [] in memroy as return value. meory issue!