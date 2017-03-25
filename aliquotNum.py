# aliquot number is the sum of factors of a number:
# 1,2,3 are factors of 6 (except 6 itself)
# aliquot sum is: 1+2+3=6
# if aliquot == number, perfect
# if aliquot < number, deficient
# if aliquot > number, abdundant

# How to decide the classification of a given number?

def is_factor(potential, number):
	if number % potential == 0:
		return True
	else:
		return False

def factors(number):
	return [ each for each in xrange(1, number) if is_factor(each, number) ]

def factors_sum(factors):
	return sum(factors)

def classify(number):
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
