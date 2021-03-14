def palindrome(str):
	rev = str[::-1]
	return rev == str

def palindrome2(str):
	i = 0
	j = len(str) - 1
	while i < j:
		if str[i] != str[j]:
			return False
		i += 1
		j -= 1
	return True

word = str(input("please enter a word"))

print(palindrome2(word))