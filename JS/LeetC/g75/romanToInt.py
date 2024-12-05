values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def romanToInt(s):
    sum = 0
    for i in range(len(s) - 1, 0, -1):
        if values[s[i]] < values[s[i + 1]]:
            sum -= values[s[i]]
        else:
            sum += values[s[i]]

    return sum
