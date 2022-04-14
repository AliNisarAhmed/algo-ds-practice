VOWELS = ['a', 'e', 'i', 'o', 'u']

def more_vowels(s, index = 0, count = 0):
	l = len(s)
	if index >= l:
		return count > (l // 2)
	else:
		if s[index] in VOWELS:
			return more_vowels(s, index + 1, count + 1)
		else:
			return more_vowels(s, index + 1, count)

print(more_vowels('abc'))