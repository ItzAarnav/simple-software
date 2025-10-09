import time
import os
os.environ['TERM'] = 'xterm-256color'

print("Simple Software")
time.sleep(1)

print("Loading key assets...")
# Body code

switch = True
data = []
time.sleep(1)
os.system('clear')

while switch:
	print("-- Simple Software --\n")
	commands = input(" >>> ").lower()

	tokens = commands.split(";")
	command = tokens[0]
	parameter1 = tokens[1]
	parameter2 = tokens[2]

	if len(tokens) <= 3:

		# Software/Console
		if command == 'write':
			print(parameter1)
		if command == 'quit':
			quit(parameter1)
		if command == 'clear':
			print("Clearing in 5 seconds...")
			time.sleep(5)
			os.system('clear')
		if command == 'notify':
			parameter1 = parameter1.replace('"', '\\"')
			parameter2 = parameter2.replace('"', '\\"')

			# Use osascript to send the notification
			os.system(f'''osascript -e 'display notification "{parameter2}" with title "{parameter1.title()}"' ''')

		# Data
		if command == 'fetch':
			if parameter1 == 'return':
				print(data)
			if parameter1 == 'add':
				data.append(parameter2)
			if parameter1 == 'remove':
				try:
					data.remove(parameter2)
				except ValueError:
					print(f"[ERR] '{parameter2}' does not exist")
			if parameter1 == 'len':
				print(len(data))
		if command == 'slice':
			try:
				print(data[parameter1:parameter2])
			except TypeError:
				print("[ERR] indices inputted wrong")
		if command == 'script':
			if parameter1 == 'create':
				try:
					with open(parameter2, 'r') as file:
						code = file.read()
					print(f"Success: {parameter2} has been created.")
				except:
					pass