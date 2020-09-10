import sqlite3
import os
import random

try:
	conn = sqlite3.connect('data.db')
	cur = conn.cursor()
	cur.execute('SELECT * FROM config')
	conn.close()
	"""Проверка на то, есть ли база данных, если есть, подолжает код"""
	result = str(input('У вас уже есть база данных, хотите её пересоздать?[Y/N]: '))
	if result == 'Y' or result == 'y' or result == 'yes' or result == 'Yes' or result == 'YES':
		os.rename('data.db', f'backup{str(random.randint(1, 999))}_data.db')
		print('СОЗДАН БЕКАП БД!!!')
		conn = sqlite3.connect('data.db')
		cur = conn.cursor()
		cur.execute('''CREATE TABLE config(
	"token" TEXT,
  	"qiwi_token" TEXT,
  	"qiwi_number" TEXT,
  	"qiwi_pkey" TEXT,
  	"admin_id" TEXT,
  	"admin_chat" TEXT
)''')
		conn.commit()
		token = str(input('Введите токен бота, получить его можно после создание в боте:@botfather: '))
		number = str(input('Введите номер киви кошелька(без +, начиная с 7): '))
		qiwi_token = str(input('Введите токен киви: '))
		pkey = str(input('Введите publicKey, полученный на сайте p2p.qiwi.com: '))
		admin_id = int(input('Введите id админа: '))
		admin_chat = str(input('Введите id чата админов: '))
		cur.execute(f'''INSERT INTO config VALUES('{token}', '{qiwi_token}', '{number}', '{pkey}', '{admin_ids}', '{admin_chat}')''')
		conn.commit()
		print('Все успешно настроено! Запустите main.py')
	else:
		print('\nОтмена операции')
except Exception as e:
	print(e)
	"""Если нет базы данных"""
	print('Привет!')
	result = str(input('Хочешь создать и настроить базу данных?[Y/N]: '))
	if result == 'Y' or result == 'y' or result == 'yes' or result == 'Yes' or result == 'YES':
		conn = sqlite3.connect('data.db')
		cur = conn.cursor()
		cur.execute('''CREATE TABLE config(
	"token" TEXT,
  	"qiwi_token" TEXT,
  	"qiwi_number" TEXT,
  	"qiwi_pkey" TEXT,
  	"admin_id" TEXT,
  	"admin_chat" TEXT
)''')
		conn.commit()
		admin_ids = []
		token = str(input('Введите токен бота, получить его можно после создание в боте:@botfather: '))
		number = str(input('Введите номер киви кошелька(без +, начиная с 7): '))
		qiwi_token = str(input('Введите токен киви: '))
		pkey = str(input('Введите publicKey, полученный на сайте p2p.qiwi.com: '))
		admin_id = int(input('Введите id админа: '))
		admin_chat = str(input('Введите id чата админов: '))
		cur.execute(f'''INSERT INTO config VALUES('{token}', '{qiwi_token}', '{number}', '{pkey}', '{admin_ids}', '{admin_chat}')''')
		conn.commit()
		print('Все успешно настроено! Запустите main.py')
	else:
		print('Отмена операции')	
