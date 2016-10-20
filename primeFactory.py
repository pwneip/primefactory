#!/usr/bin/env python
#title           :primeFactory.py
#description     :Given two integers, find all primes in that range 
#author          :PwnEIP
#date            :10 Oct 2017
#version         :1.0
#usage           :primeFactory.py [-s] [-h] # #
#notes           :
#python_version  :2.7.12
#==============================================================================

import sys, getopt

#check if number n is prime
#return 1 if prime
#return 0 if not prime

def usage():
	print "usage: primeFactory.py [-s] [-h] # #"
	print "\t -s to show only prime numbers show's digit"
	print "\t  sum is also prime.  ex. 61 is prime, 6+1=7 and 7 is prime"
	print "\t -h, this menu"
	sys.exit(2)

def isPrime(n):
	for i in range(2, n):
		if n % i == 0:
			return 0
	return 1

def getPrimes(start, end, sum):
	for i in range(start, end):
		if isPrime(i):
			if sum:
				#now sum the digits and check
				digitsum = int()
				for n in str(i):
					digitsum = digitsum + int(n)
				if isPrime(digitsum):
					print i
			else:
					print i

def main(argv):
	sum = bool(False)
	try:                                
		opts, args = getopt.getopt(argv, "hs", ["help", "sum"])
	except getopt.GetoptError:
		usage()
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt in ("-s", "--sum"):
			sum = bool(True)
	if len(args) == 2:
		try:
			getPrimes(int(args[0]), int(args[1]), sum)
			sys.exit(0)
		except ValueError:
			usage()	
	else:
		usage()

if __name__ == "__main__":
    main(sys.argv[1:])
