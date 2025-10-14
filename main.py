import random
import time


print("\nPy Data Lab\n")
print("")
data = []
is_on = True
command_number = 0

role = input("What is your use for Py Data Lab?\nType one of the options\nMake sure to check out this website for further information:https://pydatalab.burfiboy.repl.co/\n(general(needs no domain)/professional): ").lower()
if role == 'general':
    print("Welcome to the Py Data Lab,\nIn this lab you will explore many commands\nin the general version:\n - You have free uses\n - You can learn to be a pro")
    time.sleep(1)
    use = input("What is your use for Py Data Lab?\n- Learner\n- Teacher\n").lower()
    if use == 'learner':
        print("Welcome to the learner dashboard!\n")
    if use == 'teacher':
        print("Welcome to the teacher dashboard!\nTeaching Materials are ready-made\n")
        account = input("Would you like to link to an account")
if role == 'professional':
    password = input("Domain: ")
    if password == '2232':
        while is_on:
            commands = input(f"Command Pallete:  #{command_number}; ")
            command_number += 1
            if commands == 'give':
                give = input("\nCommand -> ")
                if give == 'print':
                    mime = input("-> ")
                    print(mime)

            if commands == 'report':
                report = input("Command -> ")
                if report == 'data':
                    data_input = input("Prompt typo -> ")
                    if data_input == 'd_report':
                        print(data)
                    if data_input == 'd_var_new':
                        set_var = input("d_var_new\ Raw duplicate -> set:set_var:d_var -> ")
                        d_var = set_var
                    if data_input == 'd_len':
                        print(len(data))
                if report == 'slice':
                    slce = input("Prompt typo -> ")
                    if slce == 'item_num':
                        item_number = input("slice input -> ")

            if commands == 'unit':
                unit = input("Command -> ")
                if unit == 'u_new':
                    new_data = input("New data; ")
                    data.append(new_data)
                    print("inserted(Check data with report)")
                if unit == 'u_remove':
                    remove_data = int(input("Item call#(delete): "))
                    data.remove(remove_data)
                if unit == 'u_refactor':
                    refactor = int(input("Item call#(replace): "))
                    data.replace(refactor)
                if unit == 'u_list_delete':
                    input("Type anything\n")
                    print("DeLeTe_AlL\n")
                    repeat = input("Repeat the text above to proceed command\n")
                    if repeat == 'DeLeTe_AlL':
                        for item in data:
                            data.remove(item)
                        data = 0
                        print("Successfully Deleted")
            if commands == 'system':
                system = input("Command -> ")
                if system == 'off':
                    print("OfF_system\n")
                    repeat = input("Copy the text above\n")
                    if repeat == 'OfF_system':
                        is_on = False
                        print("Offed\nData Cleaned and trashed")
                if system == 'copyright':
                    print("""Copyrighted: 2023
                             presents Data Science Lab
                             all rights reserved
                             copyrighted by, ARK,inc,
                             no public remixes""")