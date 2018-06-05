# Exceptions Example

try:
	fh = open('xlines.txt')
	for line in fh.readlines():
		print(line)

except IOError as e:
	print('Something Bad Happend ({})'.format(e))
