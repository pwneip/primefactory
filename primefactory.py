#!/usr/bin/python
import sys

#check if number n is prime
#return of 1 is prime
#return of 0 is not prime
def isPrime(n):
	for i in range(2, n):
		if n % i == 0:
			return 0
	return 1

start = 1000000
end = 1100000


#get primes for range
def getPrimes(start, end):
	for i in range(start, end):
		if isPrime(i):
			sum = int()
			for n in str(i):
				sum = sum + int(n)
			if isPrime(sum):
				print i

#check args, get primes
if len(sys.argv) != 3:
	print "usage: primefactory # #"
else:
	getPrimes(int(sys.argv[1]), int(sys.argv[2]))
