from random import randrange, randint
import math

def minmax(arr):
	min = arr[0]
	max = arr[0]

	for i in range(1, len(arr)):
		if arr[i] < min:
			min = arr[i]
		if arr[i] > max:
			max = arr[i]
	return (min, max)

print(minmax([6, 5, 4, 3, 2, 1]))


def calcSumTo(n):
	sum = 0
	for i in range(1, n):
		sum += i
	return sum


def calcSumTo2(n):
	return sum([k for k in range(1, n)])

def calcPos(n):
	return sum([k for k in range(1, n) if k % 2 != 0])

print(calcPos(5))

#-------------------

def choice(arr):
	return arr[randrange(0, len(arr) - 1)]

print(choice([1, 2, 3, 4, 5]))

# --------

def productIsOdd(arr):
	first_odd = None

	for n in arr:
		if first_odd is None and n % 2 != 0:
			first_odd = n
		elif n % 2 != 0:
			return True
	return False

# print(productIsOdd([1, 2, 4, 6, 8, 9]))

# -----------------

def unique(arr):
	return len(set(arr)) == len(arr)

print(unique([1, 2, 3, 4, 5, 5]))

# ----- C-18

# [k * j for k, j in zip(range(10), range(1, 11))]
# [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]

# ----- C-19

print([chr(97+x) for x in range(26)])


# ------- C-20

def myShuffle(data):
	l = len(data)
	for i in range(1, l):
		choice = randint(i, l - 1)
		data[choice], data[i - 1] = data[i - 1], data[choice]

def fisherYates(data):
	l = len(data)
	i = l - 1
	while i > 0:
		s = randint(0, i)
		arr[i], arr[s] = arr[s], arr[i]
		i -= 1

arr = [1, 2, 3, 4, 5, 6, 7, 8]
myShuffle(arr)
print(arr)


# ------------------

def read_inputs(filepath):
	fp = open(filepath)
	lines = []
	while True:
		try:
			line = fp.readline()
			print(line[:-1])
			if line == '': raise EOFError
			lines.append(line[:-1])
		except EOFError:
			for line in reversed(lines):
				print(line)
				return

read_inputs('./r13.py')

# -----------------------------

def dotProduct(arr1, arr2):
	return [k * j for k, j in zip(arr1, arr2)]

a, b = [1,2,3,4,5,6], [2,3,4,5,6,7]
print(dotProduct(a, b))



# -------------------- C -1.24

def countVowels(str):
	count = 0
	for c in str:
		if c in "aeiou":
			count += 1
	return count

print(countVowels("abcdef"))


# ----------- C-1.26

def arithmetic_check(a, b, c):
	return a + b == c or b - c == a or a * b == c

print(arithmetic_check(9,2,3))


# --------- C-1.26 factors in order

#Approach 3
def factors2(n):
	k = 1
	remaining = []
	while k*k<n:
			if n%k == 0:
					yield k
					remaining.append(n//k)
			k+=1
			if k*k == n:
					yield k
	for factor in reversed(remaining):
		yield factor

# ------ C- 1.28

def p_norm(v, p = 2):
	sum = 0
	for n in v:
		sum += n ** p
	return sum ** (1 / p)

print(p_norm([4,3]))
print(p_norm([4,3, 4, 5], 3))

# ---------------- P-1.29

def perms(str):
	if len(str) == 1:
		return [str]
	perm_list = []
	for a in str:
		remaining = [x for x in str if x != a]
		p = perms(remaining)
		for t in p:
			perm_list.append([a] + t)
	return perm_list

# ------------- P - 1.31

# Make Change

# currency are: 1, 0.5, 0.25, 0.1

def makeChange(charge, given): # given > charge
	diff = given - charge
	count1 = count5 = count25 = count01 = 0
	while diff > 0:
		if diff >= 1:
			count1 += 1
			diff -= 1
		elif diff >= 0.5:
			count5 += 1
			diff -= 0.5
		elif diff >= 0.25:
			count25 -= 1
			diff -= 0.25
		else:
			count01 -= 0.1
			diff -= 0.1
	return [(1, count1), (0.5, count5), (0.25, count25), (0.1, count01)]

def makeChange2(charge, given, denoms = [1, 0.5, 0.25, 0.1]):
	diff = given - charge
	change = {}
	for d in denoms:
		amount, residual = divmod(diff, d)
		if amount: change[d] = int(amount)
	return change

print(makeChange2(5, 10))


# ------ P-1.35

def test_birthday_paradox(num_people):
	birthdays = [randrange(0, 365) for _ in range(num_people)]
	b_set = set()
	for bd in birthdays:
		if bd in b_set:
			return True
		else:
			b_set.add(bd)
	return False

def paradox_stats(num_people = 23, num_trials = 1000):
	success = 0
	for i in range(num_trials):
		if test_birthday_paradox(num_people): success += 1
	return success / num_trials

print(paradox_stats())