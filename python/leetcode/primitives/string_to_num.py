def string_to_num(s, index = 0):
	l = len(s)
	if index >= l:
		return 0
	if index == l - 1:
		return int(s[index])

	return int(s[index]) * (10 ** (l - index - 1)) + string_to_num(s, index + 1)
