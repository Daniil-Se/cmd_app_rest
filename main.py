import subprocess
import requests

class App:

	def input_command(self):
		command = input('Ожидание команды: ')
		if command == 'post':
			self.push_post()
		elif command == 'get':
			self.push_get()	
		elif command == 'exit':
			self.exit()
		else:
			self.unknown_command()
	
	def push_post(self):
		r = requests.post('http://127.0.0.1:5000/post', 
						   json={"Name": "John",
						   		 "Age": '23',
						   		 "Shopping_list": ['milk', 'chocolate']})
		print(r.status_code, r.json())
		self.input_command()

	def push_get(self):
		r = requests.get('http://127.0.0.1:5000/get')
		print(r.status_code, r.json())
		self.input_command()

	def unknown_command(self):
		print('\n-- unknown command -- \n')
		print('''\tСписок доступных команд для ввода:
			     \n\ttest - функция теста (отправка POST на localhost)
			     \n\texit - функция выхода из приложения
			     ''')
		self.input_command()

	def exit(self):
		print('\nsuccessful exit\n')	



if __name__ == '__main__':
	App().input_command()
