def unique3(arr, start, stop):
	if stop - start <= 1: return True
	elif not unique3(arr, start, stop - 1): return False
	elif not unique3(arr, start + 1, stop): return False
	else: return arr[start] != arr[stop - 1]