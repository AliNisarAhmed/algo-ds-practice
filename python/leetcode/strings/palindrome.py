def palindrome(s):
	return palindrome_rec(s, 0, len(s) - 1)

def palindrome_rec(s, start, stop):
	if start >= stop:
		return True
	else:
		if s[start] != s[stop]:
			return False
		else:
			return s[start] == s[stop] and palindrome_rec(s, start + 1, stop - 1)

print(palindrome('racecar'))