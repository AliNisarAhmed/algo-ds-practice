def reverse(s):
	l = len(s)
	if l == 1:
		return s
	else:
		return reverse(s[1:]) + s[0]

print(reverse('abcd'))