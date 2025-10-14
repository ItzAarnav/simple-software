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
    if len(tokens) >= 2:
        parameter1 = tokens[1]
    else:
        parameter1 = 'pass'
    if len(tokens) == 3:
        parameter2 = tokens[2]
    else:
        parameter2 = 'pass'

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
        if command == 'notes':
            print("-- Notes --\n[1] This software is a passion project by ItzAarnav.\n[2] Script command is under "
                  "experimentation\n[3] Unofficial software; it is not licensed")
        if command == 'script':
            print("[ERR] This command is locked.")
        # if parameter1 == 'create':
        # 	try:
        # 		file = open(parameter2, 'x')
        # 		print(f"Success: {parameter2} has been created.")
        # 		print("Edit the file with the scripts you need.")
        # 	except FileExistsError:
        # 		print("[ERR] This file already exists.")
        # if parameter1 == 'run':
        # 	try:
        # 		with open(parameter2, 'r') as file:
        # 			syntax = file.read()
        # 		exec(syntax)
        # 	except:
        # 		print("[ERR] There was an error in your scripts.")
    else:
        print("[ERR] Perhaps you added an extra parameter")
