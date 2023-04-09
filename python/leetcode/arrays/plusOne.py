from typing import List


def plusOne(digits: List[int]) -> List[int]:
    for i in reversed(range(len(digits))):
        if digits[i] == 9:
            digits[i] = 0
        else:
            # increate the right-most not 9 by 1 and exit
            digits[i] += 1
            return digits

    # we reach this point if all digits are 9
    return [1] + digits



if __name__ == "__main__":
    a = [9, 9, 9]
    print(plusOne(a))
