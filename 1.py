def a1():
	a = int(input('Введите число нулей - '))
	x = [0] * (a+2)
	x[0]=x[-1]=1
	print(x)

def a2():
	a = int(input('Введите число повторений - '))
	x = [0,1] * a
	print(x)

def a3():
	x = []
	a = 1
	y = int(input('Введите нечётное число - '))
	y /= 2
	y += 1
	for i in range(int(y)):
		x.append(a)
		a += 2
	print(x)

def a4():
	a = []
	x = int(input('Введите первый элемент (x) - ')) 
	d = int(input('Введите разность (d) - '))
	y = int(input('Введите число - '))
	y += 1
	for i in range(int(y)):
		a.append(x)
		x += d
	print(a)

def a5():
	a = []
	for i in range(0,100,2):
		a.append(i)
	print(a)
	
def a6():
	a = []
	for i in range(99,0,-3):
		a.append(i)
	print(a)

def a9():
	x = int(input('Введите число - '))
	a = []
	y = 0
	for i in range(x):
		a.append(y)
		i += 1
		y = i**2
	print(a)	
			
while True:
	x = input('Введите номер задачи - ')
	if   x == '1':
		a1()
	elif x == '2':
		a2()
	elif x == '3':
		a3()
	elif x == '4':
		a4()
	elif x == '5':
		a5()
	elif x == '6':
		a6()
	elif x == '9':
		a9()
	else:
		print('Такой задачи нет')
