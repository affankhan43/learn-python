
def main():
	func(1)
	func()
	func(8)
	func(3)

def isprime(n):
	if n == 1:
		print("1 is Special")
		return False
	for x in range(2,n):
		if n % x == 0:
			print("{} equals {} x {}".format(n , x , n // x))
			return False
		else:
			print(n, "is a prime number")
			return True

def func(a=4):
	for i in range(a,10):
		print(i,end=' ')
	print()

for n in range(1,20):
	isprime(n)

if __name__ == '__main__': main()