import random
from time import sleep
from colorama import init
from colorama import Fore, Back, Style
init()

'''Имена используются для создания рабочих и поситителей'''
Name = [ 'Иван', 'Дмитрий', 'Владимир', 'Алексей', 'Сергей', 'Данил', 'Михаил', 'Виталий', 'Борис',
'Андрей', 'Амир', 'Вадим', 'Влад', 'Глеб', 'Дамир',] 

#menu
menu = {
	'кофе' : 150,
	'чай' : 50,
	'коктель' : 200,
	'вода' : 0
}

levelHouse = 1
budget = 30000
price_of_uplevelhouse = 5000

'''Общий класс'''
class Person:
	'''Инициализация'''
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('(Cоздан человек: {0})'.format(self.name))

	def tell(self):
		#Вывод информации
		print('Имя: {0}, возраст: {1}'.format(self.name, self.age))	
		

class Worker(Person):
	#кол-во рабочих
	population = 0
	#усталость рабочих
	fatigue = 0
	'''Инициализация'''
	def __init__(self, name, age, salary):
		Person.__init__(self, name, age)
		self.salary = salary
		print('(Создан рабочий: {0})'.format(self.name))
		Worker.population += 1
	
	def tell(self):
		#Вывод информации
		Person.tell(self)
		print('Зарплата: {0:d} '.format(self.salary))

	def howMany():
		print('Кол-во рабочих: {0:d} '.format(Worker.population))
		
	howMany = staticmethod(howMany)

class Visitor(Person):
	population = 0

	'''Инициализация'''
	def __init__(self, name, age, maney):
		Person.__init__(self, name, age)
		self.maney = maney
		print('(Пришёл посетитель: {0})'.format(self.name))
		Visitor.population += 1

	def tell(self):
		#Вывод информации
		Person.tell(self)
		print('Кол-во денег: {0:d}'.format(self.maney))

	def howMany():
		print('Кол-во посетителей: {0:d} '.format(Visitor.population))
	
	howMany = staticmethod(howMany)

'''>>>menu'''
def services():
	print('Вы работаете в кофейне')
	print('Ваше меню: {0}'.format(menu))
	print()
'''Посититель делает заказ'''
def makeOrder():
	global budget
	price_of_the_product = menu.get(order)
	'''Выполняется если у поситителя хватило денег'''
	if maney >= price_of_the_product:
		print('{0} купил {1}'.format(name, order))
		'''Вам перечесляются деньги'''
		budget += maney
		print('Ваши деньги: {0:d}'.format(budget))
	else:
		print('У {0} не хватило денег =('.format(name))
	print()


'''Система усталости
1 рабочий == 1 ход
'''
def fatigue():
	Worker.fatigue +=1
	if Worker.fatigue == Worker.population:
		print('Рабочие устали!')
		sleep(10)
		Worker.fatigue -= Worker.fatigue
	print()
'''>>>info'''
def info():
	print('Уровень заведения: {0:d}, бюджет: {1:d}'.format(levelHouse, budget))
	Worker.howMany()
	print()
'''текст зелёного цвета'''
print( Fore.GREEN )
while True:
	Q1 = input('Что хотите сделать?\n1)Выйти\n2)Узнать информацию обо мне\n3)Нанять рабочего\n4)Впустить посетителя\n'
		'5)Вывести информацию\n6)Улучшить заведение\n').lower()

	if Q1 == '1':
		break
	elif Q1 == '2':
		services()
	elif Q1 == '3':
		if Worker.population < levelHouse:
			name = random.choice(Name)
			age = random.randint(18, 50)
			salary = random.randint(10000, 40000)
			#budget = 100000
			print('Имя: {0}, Возраст: {1:d}, Зарплата: {2:d}'.format(name, age, salary))

			Q2 = input('Будите его нанимать?\n').lower()
			if Q2 == 'да' and budget >= salary:
				w = Worker(name, age, salary)
				budget = budget - salary
				print('Ваш бюджет: {0:d}'.format(budget))
			elif Q2 == 'нет':
				continue
			elif budget < salary:
				print('У вас не хватает денег!')
		else:
			print('Привышен лимит!') 
		print()
	elif Q1 == '4':
		if Worker.population > 0:
			name = random.choice(Name)
			age = random.randint(18, 50)
			maney = random.randint(10, 300)

			'''Переписать потом в def'''
			v = Visitor(name, age, maney)
			visitors = []
			visitors.append(v)
			v.tell()
			'''---------------^---------------'''

			order = random.choice(list(menu.keys()))
			print('Посетитель хочет заказать {0}'.format(order))

			makeOrder()
			fatigue()
		else:
			print('У вас нет рабочих')
		print()
	elif Q1 == '5':
		info()
	elif Q1 == '6':
		price_of_uplevelhouse += price_of_uplevelhouse
		print('Стоимость улучшения: {0:d}'.format(price_of_uplevelhouse))
		if budget >= price_of_uplevelhouse:
			Q3 = input('Будете улучшать?\n').lower()
			if Q3 == 'да':
				budget -= price_of_uplevelhouse
				levelHouse += 1
				print('Вы улучшили заведение!')
				print('Ваш бюджет: {0:d}'.format(budget))
		elif budget < price_of_uplevelhouse:
			print('У вас не хватает денег!')
		print()

	
		
