import json

with open('new_json.json', 'r') as file:
	data = json.load(file)
while True:

	print("1.) Talk to simsimi")
	print("2.) Teach Simsimi")
	print('3.) Exit')

	user = int(input('What do you want to do sir?'))

	if user == 1:
		print("Simsimi: Hi!")
		while True:
			
			user = input('You: ')
			if user == 'Exit':
				break
			elif user in data:
				print('Simsimi:' + data[user])
			else:
				print("Thats the first time I heard that")
				continue

	elif user == 2:
		while  True:
			voca = {}
			user = input('When the user says: ')
			if user == 'stop':
				break
			bot = input('Simsimi says: ')
			voca[user] = bot

			with open('new_json.json', 'r+') as file:
				data = json.load(file)
				data.update(voca)
				file.seek(0)
				json.dump(data, file)

			
	else:
		break			
