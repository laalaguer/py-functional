def push_word(word, fq):
	if word in fq:
		fq[word] += 1
	else:
		fq[word] = 1

def clean_up(word):
	punchs = ['.', ',', '?']
	if word not in punchs:
		return word
	else:
		return None

if __name__ == '__main__':
	article = "This is a wonderful day , is it ?"
	
	words = article.split()
	words = [ clean_up(each) for each in words ]
	words = [ each for each in words if each ]
	fq = {}
	for each in words:
		push_word(each, fq)

	print fq
