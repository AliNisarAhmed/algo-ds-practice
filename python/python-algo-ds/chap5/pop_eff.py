from time import time

def pop_eff(test_array, n=10):
    results = dict()

    for test_len in test_array:

        for pos in [0, 0.5, 1]:
            results[pos] = dict()
            start = time()

            for _ in range(n):
                data = [None] * test_len
                while len(data) > 1:
                    data.pop(int((len(data)-1)*pos))
            end = time()

            results[pos][test_len] = (end - start) / test_len

    return results
