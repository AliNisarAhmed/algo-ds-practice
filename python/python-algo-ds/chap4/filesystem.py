import os

def diskUsage(path):

	total = os.path.getsize(path)
	if os.path.isdir(path):
		for p in os.listdir(path):
			total += diskUsage(os.path.join(path, p))
	print ('{0:<7}'.format(total), path)
	return total

diskUsage('.')