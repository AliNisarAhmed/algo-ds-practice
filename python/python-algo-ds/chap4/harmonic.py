def harmonic(i):
	if i == 1:
		return 1
	return (1 / i) + harmonic(i - 1)

def recursive_convert(str):
	k = len(str)
	if k == 1:
		return int(str)
	return int(str[0]) * (10 ** (k - 1)) + recursive_convert(str[1:])

print(recursive_convert('1234'))

def minmax(arr):
	k = len(arr)
	if k == 0:
		raise ValueError("Array cannot be empty")
	if k == 1:
		return (arr[0], arr[0])
	rest = arr[1:]
	(rmin, rmax) = minmax(rest)
	return (min(arr[0], rmin), max(arr[0], rmax))

print(minmax([1, 2, 3,4, 5]))


# 4.10

def log_two(n):
	if n < 2:
		return 0
	return 1 + log_two(n // 2)

print(log_two(8))


# C-411

def uniqueN2(arr, i = 0):
	if i == len(arr) - 1:
		return True
	return (not arr[i] in arr[i + 1:]) and uniqueN2(arr, i + 1)

print(uniqueN2([1, 2, 3, 4]))
print(uniqueN2([1, 2, 3, 4, 1]))

# C-4.12

def product(m, n):
	if m == 0 or n == 0:
		return 0
	if m == 1:
		return n
	if n == 1:
		return m
	return m + product(m, n - 1)

print(product(4, 3))


# C-4.13
# https://www.cs.cmu.edu/~cburch/survey/recurse/hanoiex.html

def towerOfHanoi(disk, source = [], dest = [], spare = []):
	if disk == 0:
		dest.append(source.pop())
	else:
		towerOfHanoi(disk - 1, source, spare, dest)
		dest.append(source.pop())
		towerOfHanoi(disk - 1, spare, dest, source)


source = [4, 3, 2, 1, 0]
dest = []
spare = []
print(source)
print(dest)
towerOfHanoi(4, source, dest, spare)
print(source)
print(dest)

# C-4.15

def print_subsets(arr):
	if len(arr) == 0:
		return [[]]
	r = print_subsets(arr[1:])
	for i in range(len(r)):
		print([arr[0]] + r[i])
		print(r[i])
		r[i] = [arr[0]] + r[i]
	return r

print_subsets([1, 2, 3])