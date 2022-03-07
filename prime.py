num=int(input('Enter Positive Integer '))
a=2
while a<num:
	if num%a==0:
		print('it is not a prime number ')
		break
	a=a+1
else:
	print('it is a prime number')
