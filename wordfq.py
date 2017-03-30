# Classic problem, check word frequency in an article.
# We try to write the program in a 'side effect' = 0 way.
# AKA, functional way.

def push_word(word, fq):
	''' check word in frequency fq '''
	if word in fq:
		fq[word] += 1
	else:
		fq[word] = 1

def clean_up(word):
	''' return a stripped word '''
	punchs = ['.', ',', '?']
	if word not in punchs:
		return word
	else:
		return None

if __name__ == '__main__':
	article = "This is a wonderful day , is it ?"
	
	words = article.split()
	# warning: below will create a new list in memory.
	words = [ clean_up(each) for each in words ]
	# warning: below will create a new list in memory.
	words = [ each for each in words if each ]
	# warning: below will result in side effects.
	fq = {}
	for each in words:
		push_word(each, fq)

	print fq

# Thinking:
# 1. push_word() function has side effect. It will change
# the state of fq. And fq is from outside.
# 2. push_word() needs an outside state, which line 29-31 represents.
# This is not 'pure' as functional programming.
# 3. clean_up() is a pure function, it either return the original, or new object None
# 4. line 25-27 is a 'mapping', but it creates extra memories usage in place. We will try to avoid heavy memory usage.