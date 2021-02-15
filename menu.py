import random
import time
import os


def program():
	put = os.getcwd()
	points = ' '
	names = ' '
	win = ' '
	lose = ' '
	draw = ' '
	black_Jack = ' '
	number = ' '
	porfile_put = ' '
	bust = ' '
	suget = ' '
	boy_next_door = ' '
	def igra():
		nonlocal number
		nonlocal points
		NUBMER = []
		COLODA = [ '2', '3', '4', '5' , '6' , '7' , '8', '9' , '10' , 'В' ,'Д', 'К', 'Т']
		MAST  = [' Треф',' Бубен',' Червей',' Пик']
		for i in range(1,number + 1):
			NUBMER.append(i)
		
		if (points < 10):            #
			print('\nВЫ БАНКРОТ!!!')
			return 1

		coloda = []
		jopa = []

		for i in NUBMER:
			for j in COLODA:
				for r in MAST:
					jopa = []
					jopa.append(i)
					jopa.append(j)
					jopa.append(r)
					coloda.append(jopa)


		while (True):
			


			karta = lambda  : coloda[random.randint(0, len(coloda) - 1)] # Взятие карты

			uses = []                # Для функции vzat (катры на руках и в отбое)
			igrok = [] 			     # Карты игрока         
			krupie = []              # Карты крупье
			itog = 0                 # Результата
			stavka = 0
		 


			def vzat():               	# Перемешивание колоды + взятие карты   
				nonlocal uses
				nonlocal coloda
				nonlocal igrok
				nonlocal krupie
				if (len(coloda) / 3 * 2 <= len(uses)):
					uses = krupie + igrok
				kar = karta()
				while True: 
					if (kar not in uses):
						uses.append(kar)
						return kar
					else: 
						kar = karta()

			def ruka():                	# Список карт игрока					
				nonlocal igrok
				print('\n\n\n')
				print ("Ваши карты:")
				for i in range (len(igrok)):
					print (igrok[i][1] + igrok[i][2])
				print ("\nКол-во очков: ")
				print (nominale_igrok())

			def ruka_krupie():     	   	# Список карт крупье					
				print('\n\n')
				print ("Карты крупье:")
				for i in range (len(krupie)):
					print (krupie[i][1] + krupie[i][2])
				print ("\nКол-во очков крупье: ")
				print (nominale_krupie())

			def nominale_igrok(): 		# Сумма карт игрока 					
				nonlocal igrok
				summa = 0
				for i in range(len (igrok)):
					if (igrok[i][1].isdigit()):
						summa += int(igrok[i][1])
					elif (igrok[i][1] == 'Т'):
						summa += 11
					else:
						summa += 10
				if (summa > 21):
					i = 0;
					while (i < len(igrok)) and (summa > 21):
						if (igrok[i][1] == 'Т'):
							summa -=10
						i+= 1
				return summa

			def nominale_krupie():		# Сумма карт крупье 					
				nonlocal krupie
				summa = 0
				for i in range(len (krupie)):
					if (krupie[i][1].isdigit()):
						summa += int(krupie[i][1])
					elif (krupie[i][1] == 'Т'):
						summa += 11
					else:
						summa += 10
				if (summa > 21):
					i = 0;
					while (i < len(krupie)) and (summa > 21):
						if (krupie[i][1] == 'Т'):
							summa -=10
						i+= 1
				return summa

			def games():           		# Основа		    					
				nonlocal krupie
				nonlocal igrok
				while (True):
					if (nominale_igrok() > 21):
						print("\nУ ВАС ПЕРЕБОР !!!")
						break
					vvod = input('\nЖелаете взять карту?\n1) Взять карту.\n2) Не брать карту\nВвод: ')
					if (vvod == '1'):
						igrok.append(vzat())
						ruka()
					else:
						break
				next()
				resault()       

			def next():     			# Игра с крупье     					
				nonlocal itog
				nonlocal krupie
				ruka_krupie()
				if (nominale_igrok() > 21):
					itog = 2
				else:
					while (nominale_krupie() < 18) :
						krupie.append(vzat())
						time.sleep(1)
						ruka_krupie()
					if (nominale_krupie() > 21):
						itog = 1
					elif (nominale_krupie() == nominale_igrok()):
						itog = 3
					elif (nominale_krupie() > nominale_igrok()):
						itog = 2
					else:
						itog = 1
			
			def resault(): 				# Результаты	    					
				nonlocal itog
				nonlocal points
				nonlocal stavka
				nonlocal win, lose, draw, black_Jack
				if (itog == 1):
					print ('\nВЫ ВЫЙГРАЛИ!')
					win += 1
					stavka *= 2
					points += stavka
				if (itog == 2):
					lose +=1
					print ('\nВЫ ПРОИГРАЛИ!')
				if (itog == 3):
					print ('\nНИЧЬЯ!')
					draw += 1
					points += stavka
				if (itog == 4):
					black_Jack += 1
					points += stavka * 3

			def stavka_funk():			# Система ставок    					
				nonlocal stavka
				nonlocal points
				nonlocal bust
				while (True):
					stavka = input("\n\nВаши очки: " + str(points) + '.  ВВедите вашу ставку (ставка может быть только кратна 10!!!)\nВвод: ')
					if (stavka.isdigit()):
						stavka = int(stavka)
						if (stavka % 10 == 0 and stavka >= 10):
							if (stavka > points):
								("Вам нехватает очков")
							else:
								if (bust > 0):
									cashback = stavka / 100 * bust * 10
									cashback = int(cashback)
									points = points + cashback
								points = points - stavka
								break

			def doublestavka():			# Двойные ставки    					
				nonlocal igrok
				nonlocal stavka
				nonlocal points
				print ("\nПервая карта крупье: " + krupie[0][1] + krupie[0][2])
				points = points - stavka 
				stavka *= 2
				igrok.append(vzat())
				ruka()
				if (nominale_igrok() > 21):
					print("У вас перебор")
				time.sleep(1)
				next()
				resault()

			def ochko():				# Очко			    					
				nonlocal krupie
				nonlocal stavka
				nonlocal points
				nonlocal itog
				print('Блэк Джэк!')
				print ("Первая карта крупье: " + krupie[0][1] + krupie[0][2] + "\n")
				if (krupie[0][1] == 'Т'):
					vvod = input('\nВы хотите забрать 1:2 ставку? 1) Да \n2) нет \nВвод: ')
					if (vvod  == '1'):
						itog = 1
						resault()
					else:
						print('Карты крупье: ')
						ruka_krupie()
						if (nominale_krupie() == 21):
							itog = 3
							resault()
						else:
							itog = 4
							resault()
				elif (krupie[0][1] in {'В','Д','К','10'}):
					print('Карты крупье: ')
					ruka_krupie()
					if (nominale_krupie() == 21):
						itog = 3
						resault()
					else:
						itog = 4
						resault()
				else:
					ruka_krupie()
					itog = 4
					resault()

			def srohovka():             # Страховка         					
				nonlocal stavka
				nonlocal points
				nonlocal krupie
				nonlocal itog

				if (krupie[0][1] in {'В','Д','К','10','Т'} ):
					if (points >= stavka // 2):
						vvod = input('Желаете взять строховку?\n1) Да\n2) Нет \nВвод: ')
						if (vvod == '1' ):
							if (nominale_krupie() == 21):
								ruka_krupie()
								print ('Страховка сработала!\n')
								points += stavka
								return 1
							else:
								points -= stavka // 2
								return 0
					if (nominale_krupie() == 21):
						ruka_krupie()
						print('У КРУПЬЕ БЛЭК ДЖЭК!!!')
						itog = 2
						resault()
						return 1
				return 0

			def start(): 				# Начало игры       					
				nonlocal krupie
				nonlocal igrok
				stavka_funk()
				krupie.append(vzat())
				krupie.append(vzat())
				igrok.append(vzat())
				igrok.append(vzat())
				ruka()
				if (nominale_igrok() == 21): # Очко
					ochko()

				elif (nominale_igrok() >= 10): # увеличение ставки
					print ("\nПервая карта крупье: " + krupie[0][1] + krupie[0][2] + "\n")
					if (srohovka() == 0):
						if (points >= stavka):
							vvod = input('\nУ вас больше 10 очков, желатете удвоить ставку и взять еще 1 карту? \n1) Да \n2  Нет\nВвод:  ')
							if (vvod == '1'):
								doublestavka()
							else:
								games()
						else:
							games()
				else:
					print ("\nПервая карта крупье: " + krupie[0][1] + krupie[0][2] + "\n")
					if (srohovka() == 0):
						games()

			start()
			stavka = 0
			print('Ваши очки равны: ' + str(points) )
			if (points < 10):
				print('\nВЫ БАНКРОТ!!!\n')
				return 1
			gg = input('\nЖелаете продолжить игру? \n1)Да \n2) Нет\nВвод:  ')
			if (gg != '1'):
				return 1
	def suget_funk():
		nonlocal suget, boy_next_door, names, win, lose, draw, black_Jack, bust
		def suget_funk0():
			nonlocal boy_next_door, names
			print('\n\n\nМистер Черный: Так и знал, что ты придешь ко мне, ' + names + ', выбора у тебя и небыло...' )
			time.sleep(3)
			print('\nЛадно, давай сейчас посуществу. У моего клуба есть сильный конкурент, казино Мистера Чин Гиза ')
			time.sleep(3)
			print('\nБудешь играть в его казино, сути дело пока не расскажу. Хотелось бы тебя проверить тебя')
			time.sleep(3)
			print('\nТвоя задача выйграть 5 партий, думаю для тебя это не будет сложностью')
			time.sleep(3)						
			print('\n\n\n' + names  + ': Я вас не подведу.')
			time.sleep(3)
			boy_next_door += 1

		def suget_funk1():
			nonlocal boy_next_door ,names, win, lose, draw, black_Jack
			if (not(win + lose + draw + black_Jack > 4 )):
				print('\n\n\nМистер Черный: Приходи, когда сыграешь 5 игр' )
				time.sleep(3)
				return 1
			print('\n\n\n' + names  + ': Я сыграл 5 партий.')
			time.sleep(3)			
			print('\n\n\nМистер Черный: Оу, неплохие партии, навыки есть, чуйка тоже. И все же, незнаю, незнаю...' )
			time.sleep(3)
			print('\nДумаю, нужно узнать по лучше, попробуй одержать 10  побед, не думаю что это будет сложно для тебя. ')
			time.sleep(3)
			boy_next_door +=1

		def suget_funk2():
			nonlocal names, boy_next_door, win, black_Jack
			if (not(win + black_Jack > 9)):
				print('\n\n\nМистер Черный: Приходи, когда одержишь 10 побед' )
				time.sleep(3)
				return 1
			print('\n\n\n' + names  + ': Я одержал 10 побед.')
			time.sleep(3)
			print('\n\n\nМистер Черный: Поздравляю!, вижу еще не растерял навыки. Давай так, последний тест. Проверим твою удачу ' )
			time.sleep(3)			
			print('\nОдержи 3 победы при первой раздачи. Получи 3 Блэк Джека!!!' )
			time.sleep(3)
			print('\n\n\n' + names  + ': Пфф, проще простого')
			time.sleep(3)
			boy_next_door +=1
		def suget_funk3():
			nonlocal names, boy_next_door, black_Jack, points
			if (not(black_Jack > 2)):
				print('\n\n\nМистер Черный: Приходи, когда получишь 3 Блэк Джека' )
				time.sleep(3)
				return 1
			print('\n\n\n' + names  + ': Дело сделанно. Думаю с меня хватит тестов, говори уже, зачем я тебе нужен, и что вообще происходит.')
			time.sleep(3)
			print('\n\n\nМистер Черный: Ух какие мы резкие то, ладно, вижу ты не растерял навыков.' )
			time.sleep(3)
			print('\nКороче, этот Чин Гиз, местный гигант в сфере казино, имеет кучу связей, купленную полицию и огромную репутацию в криминальном бизнесе. ')
			time.sleep(4)
			print('\nСейчас, по достоверным источникам, он решил стать монополистом в сфере казино, уничтожить всех конкурентов. Он использует любые методы ')
			time.sleep(4)
			print('\nЯ же вложил в свое казино огромные усилия, душу, и кучу бабок. И я не хочу его терять. На открытом поле боя, шансов спасти мое казино нету. ')
			time.sleep(4)
			print('\nПоэтому мне нужен ты, ты должен обанкротить его, ободрать его казино до ниточки. Мы с тобой должны это сделать любой ценой. ')
			time.sleep(4)
			print('\n\n\n' + names  + ': Ох тыж, серьезно дело, но я однажны уже прогорел, не хочу снова. У вас хоть есть какой то план? ')
			time.sleep(4)
			print('\nДа и как вы можете мне доверять после моего провала?')
			time.sleep(3)			
			print('\n\n\nМистер Черный: Я не могу доверять тебе полностью, поэтому начнем с малого. На твой счет уже перевели 20000 очков. ')
			time.sleep(4)
			print('\n10к оставь на ставки, а еще 10к потрать на покупку кешбека в магазине. Он сильно пригодится на длинной дистанции')
			time.sleep(4)
			print('\n\n\n' + names  + ': Надеюсь вы знаете, что делаете... ')
			time.sleep(3)
			boy_next_door += 1
			points += 20000





		if (boy_next_door == 0):
			suget_funk0()
		if (boy_next_door == 1):
			suget_funk1()
		if (boy_next_door == 2):
			suget_funk2()
		if (boy_next_door == 3):
			suget_funk3()
	def magazine():
		nonlocal points, bust, suget
		def tovary():
			while (True):
				nonlocal points, bust, suget
				print('\n\n\n\nМАГАЗИН\nВаши очки: ' + str(points) + '\nВыберите желаемый товар:')
				if (bust < 4):
					print('\n1) Купить кешбек уровень ' + str(bust + 1) + '(возвращает процент от ставки, равный уровень * 10) Стоимость: ' + str(1000*pow(10,bust+1)))
				else:
					print('Максимальный уровень')
				if (suget == 0):
					print('2) Купить ...')

				if (suget == 1):
					print('2) Купить ...')

				if (suget == 2):
					print('2) Купить ...')

				if (suget == 3):
					print('2) Купить ...')

				if (suget == 4):
					print(' 2) Купить ...')
				print ('9) Выход')

				
				
				vvod = input('Ввод: ')
				if (bust < 4 and vvod == '1'):
					if (1000*pow(10,bust+1) <= points):
						points = points - 1000*pow(10,bust+1)
						print('\nВы купили кешбек уровень: ' + str(bust + 1))
						bust += 1
					else:
						print('\nНе хватает денег')
				if (vvod == '9'):
					break
		tovary()

	def create_direktory():

		put = os.getcwd()
		fuck = put + '/saves'
		if (not(os.path.exists(fuck))):
			os.mkdir(fuck)
		fuck = put + '/saves/profile'
		if (not(os.path.exists(fuck))):
			os.mkdir(fuck)	
		fuck = put + '/saves/spisok.txt'
		if (not(os.path.exists(fuck))):
			f = open(fuck, 'w')
			f.close()	

	def profile():
		raspologenie = put  + "/saves/profile/" + porfile_put + ".txt"
		f2 = open(raspologenie)
		file = []
		nonlocal points, names, win, lose, draw, black_Jack, bust , suget, boy_next_door, number
		for line in f2:
			if (line[len(line) - 1] == '\n'):
				line = line[0:len(line) - 1]
			file.append(line)
		f2.close()
		points = int(file[1])
		names = file[0]
		win = int(file[2])
		lose = int(file[3])
		draw = int(file[4])
		black_Jack = int(file[5])
		number = int(file[6])
		bust = int(file[7])
		suget = int(file[8])
		boy_next_door = int(file[9])

	
	def save():
		nonlocal points, names, win, lose, draw, black_Jack, number, boy_next_door
		raspologenie = put + "/saves/profile/" + porfile_put + ".txt"
		f2 = open(raspologenie,'w')
		f2.write(str(names) +'\n')
		f2.write(str(points) +'\n')
		f2.write(str(win) +'\n')
		f2.write(str(lose) +'\n')
		f2.write(str(draw) +'\n')
		f2.write(str(black_Jack) +'\n')
		f2.write(str(number) +'\n')
		f2.write(str(bust) +'\n')
		f2.write(str(suget) +'\n')
		f2.write(str(boy_next_door) +'\n')
		f2.close()

	def glave():

		nonlocal number

		spisok_imen = []

		def remove():
			nonlocal spisok_imen 
			raspologenie = put + '/saves/spisok.txt'
			print('\nВыберете профиль для удаления (для отмены введите любое другое значение): ')
			t = 0
			for i in spisok_imen:
				t += 1
				print(t,i)
			porfile_vibor = input('\nВвод: ')
			while (True):
				if (porfile_vibor.isdigit()):
					porfile_vibor = int(porfile_vibor)
					if (porfile_vibor <= len(spisok_imen) and porfile_vibor >= 1):
						break
					else:
						return 1
				else:
					return 1
			porfile_put = spisok_imen [porfile_vibor - 1]
			f2 = open(raspologenie,'w')
			for line in spisok_imen:
				if (porfile_put != line):
					f2.write(line + '\n')
			f2.close()
			raspologenie2 = put + "/saves/profile/" + porfile_put + ".txt"
			os.remove(raspologenie2)
			spisok_fuction()
		
		def spisok_fuction():


			nonlocal spisok_imen
			raspologenie = put + '/saves/spisok.txt'
			spisok_imen = []
			f2 = open(raspologenie,'r')
			for line in f2:
				if (line[len(line) - 1] == '\n'):
					line = line[0:len(line) - 1]
				spisok_imen.append(line)
			f2.close()

		def save_spisok():
			nonlocal spisok_imen
			raspologenie = put + '/saves/spisok.txt'
			f2 = open(raspologenie,'w')
			for line in spisok_imen:
				f2.write(line + '\n')

		def create_profile():
			nonlocal spisok_imen
			while (True):
				name_files = input('Введите имя ваше имя\nВвод: ')
				if name_files not in spisok_imen:
					break
			spisok_imen.append(name_files)
			raspologenie = put + "/saves/profile/" + name_files + ".txt"
			f2 = open(raspologenie,'w')
			f2.write(name_files +'\n')
			f2.write(str(1000) +'\n')
			f2.write(str(0) +'\n')
			f2.write(str(0) +'\n')
			f2.write(str(0) +'\n')
			f2.write(str(0) +'\n')
			f2.write(str(4) +'\n')
			f2.write(str(0) +'\n')
			f2.write(str(0) +'\n')
			f2.write(str(0) +'\n')
			f2.close()
			save_spisok()
			strat_suget()



		def names_spisok():
			nonlocal spisok_imen 
			nonlocal porfile_put
			t = 0
			print('\nВыберете существующий профиль: ')
			for i in spisok_imen:
				t += 1
				print(t,i)
			while (True):
				porfile_vibor = (input('\nВведите цифру желаемого профиля\nВвод: '))
				if (porfile_vibor.isdigit()):
					porfile_vibor = int(porfile_vibor)
					if (porfile_vibor <= len(spisok_imen) and porfile_vibor >= 1):
						break
			porfile_put = spisok_imen [porfile_vibor - 1]

		def strat_suget():
			while (True) :
				vvod = input('\nЖелаете пропустить вступление: \n 1)Да \n 2)Нет \nВвод: ')
				if (vvod == '1'):
					break
				if (vvod == '2'):
					vstuplenie()
					break

		def vstuplenie():
			print('\nМистер Черный: Здравствуй, ' +  spisok_imen[0] + ', слышал о твоей беде...' )
			time.sleep(3)
			print('\nКак так вышло? Самый сильный и удачливый игрок стал банкротом?')
			time.sleep(3)
			print('\nГоворят ты поставил вабанк на неудачную ставку... Как так?')
			time.sleep(3)

			print('\n\n\n' + spisok_imen[0]  + ': Мне не повезло.')
			time.sleep(3)

			print('\n\n\nМистер Черный: Как знаешь, в любом случае сейчас ты мне нужен, а я нужен тебе.')
			time.sleep(3)
			print('\nЯ выведу тебя из долгов, дам возможность заработать, как понимаешь, не за даром...')
			time.sleep(3)

			print('\n\n\n' + spisok_imen[0]  + ': Что от меня требуется?')
			time.sleep(3)

			print('\n\n\nМистер Черный: Играть в black jack, надеюсь, что тебе и вправду не повезло тогда.')
			time.sleep(3)

			print('\n\n\n' + spisok_imen[0]  + ': Хорошо, в этот раз я буду умнее')
			time.sleep(3)

			print('\n\n\nМистер Черный: Это хорошо, тогда я покрою все твои долги и накину деньжат сверху.')
			time.sleep(3)
			print('\nНо теперь ты мой с ног до головы, помни это...')
			time.sleep(3)
			print('\nЗайди ко мне в клуб, как будешь готов.')
			time.sleep(3)			

				
			




		spisok_fuction()
		if (len(spisok_imen) == 0):
			create_profile()
		else:
			while (True):
				while (True):
					vvod =  input('\nВыберете желаемое действие: \n1) Cуществующий аккаунт \n2) Cоздать аккаунт \n3) Удаление аккаунта \n4) Выход \nВвод: ')
					if (vvod in  {'1','2','3','4'}):
						break
				if (vvod == '2'):
					create_profile()
					break
				if (vvod == '3'):
					remove()
				if (vvod == '1'):
					break
				if (vvod == '4'):
					return 1
		if (len(spisok_imen) == 0):
			create_profile()
		names_spisok()

	def satting():
		nonlocal number, points
		while (True):
			vvod = input ('\nВыберете изменения: \n1) Сменить кол - во колод, \n2) Сбросить очки, \n3) Возврат в меню \nВвод: ')
			if (vvod == '1'):
				kol_vo = input('Введите количество колод от 1 до 8:\nВвод: ')
				while(True):
					if (kol_vo in {'1','2','3','4','5','6','7','8'}):
						kol_vo = int(kol_vo)
						number = kol_vo
						break
			if (vvod == '2'):
				vvod2 = input('\nВы уверенны что хотите сбросить очки? \n1) Подтверждение 2) Отказ\nВвод: ')
				if (vvod2 == '1'):
					points = 1000
			if (vvod == '3'):
				return 1




	print('Вас приветствует игра: Black JACK')
	create_direktory()
	while (True):
		rof = 0
		rof = glave()
		if (rof == 1):
			return 1  
		profile()
		while (True):
			save()
			while (True):
				flag = input('\nВыберите режим: \n1) Игра \n2) Настройки \n3) Профиль \n4) Магазин \n5) смена профиля\n6) Кулб мистера Ч.\n7) Выход\nВвод: ')
				if (flag in {'1','2','3','4','5','6','7'}):
					break
			if (flag == '1'):
				igra()
			if (flag == '2'):
				satting()
			if (flag == '3'):
				print('\nИмя:',names,'\nОчки:',points,'\nПобеды:',win,'\nПоражения:',lose,'\nНичьи:',draw,'\nПобед блэк джеком:',black_Jack,'\n')
			if (flag == '4'):
				magazine()
			if (flag == '5'):
				break
			if (flag == '6'):
				suget_funk()
			if (flag == '7'):
				return 1

program()

