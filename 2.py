def fib2():
	mass = []
	for i in range(10):
		if i%2 == 0:
			mass.append('0')
		else:
			mass.append('1')
	print(mass)

def fib3():
	mass = []
	n = int(input())
	d = int(input())
	for i in range(n, 100, d):
		mass.append(i)
	print(mass)

def fib4():
	x = int(input('начало - '))
	b = int(input('шаг - '))
	mass = [x]
	while x<100:
		x += b
		mass.append(x)
	print(mass)
	
def fib5():
	num = 999
	mass = [num]
	while num>0:
		num -= 1
		if num%3==0:
			mass.append(num)
	print(mass)
def fib6():
	n = int(input('количество чисел'))
	num = 0
	num1 = 1
	res = 0
	mass = [num, num1]
	for i in range(1, n+1):
		res = num +num1
		mass.append(res)
		if i % 2 ==0:
			num1 = res
		else:
			num = res
	print(mass)	
	
def fib7():
	length = int(input('длина массива'))
	num = 1
	mass = []
	for i in range(length):
		if num % 2 != 0 and num % 3 != 0 and num % 4 != 0 and num % 5 != 0 and num % 6 != 0 and num % 7 != 0 and num % 8 != 0 and num % 9 != 0: 
			mass.append(num)
		num+=1
	print(mass)
def fib8():
	length = int(input('
		
change = input("Введите номер задачи - ")
if change == '2':
	fib2()
if change == '3':
	fib3()
if change == '4':
	fib4()
if change == '5':
	fib5()
if change == '6':
	fib6()	
if change == '7':
	fib7()	
