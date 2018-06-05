# Exceptions Example

try:
	fh = open('xlines.txt')
	for line in fh.readlines():
		print(line)

except IOError as e:
	print('Something Bad Happend ({})'.format(e)) # print msg when gets any error

a = 1,2,3,5
print(a,type(a))