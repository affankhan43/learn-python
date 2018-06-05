a, b = 1,1

if a < b :
	print('a ({}) is less than b ({})'.format(a,b))
elif a == b:
	print('a ({}) is equals to b ({})'.format(a,b))
else:
	print('a ({}) is greater than b ({})'.format(a,b))


s = "less than" if a < b else "Not less than"
print(s)
print("foo" if a < b else "bar")