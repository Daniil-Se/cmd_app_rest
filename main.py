import subprocess
import requests

class App:

	def input_command(self):
		command = input('Ожидание команды: ')
		if command == 'test':
			self.test()
		elif command == 'exit':
			self.exit()
		else:
			self.unknown_command()
	
	def test(self):
		r = requests.post('http://127.0.0.1:5000/post', json={"key": "value"})
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
