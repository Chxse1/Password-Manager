import getpass
import os
import random
import string
from cryptography.fernet import Fernet
from colorama import Fore
from pystyle import Colorate, Colors

os.system('cls & title Password Manager')

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
def gen_key():
  if os.stat("key.key").st_size == 0:
    write_key() 
  else:
    return

gen_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fernet = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        print(Colorate.Horizontal(Colors.rainbow, f"""
███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝"""))
        for line in f.readlines():
            data = line.rstrip()
            platform, phone, email, user, password = data.split(" | ")
            print(f"{Fore.GREEN}Platform: {platform} | Phone: {phone} | Email: {email} | User: {user} | Password: {fernet.decrypt(password.encode()).decode()}")
    input(f"{Fore.RED}Press enter to restart!{Fore.WHITE}")

def add():
    platform = input(Colorate.Horizontal(Colors.rainbow, 'Platform: '))
    phone = input(Colorate.Horizontal(Colors.rainbow, 'Phone Number: '))
    email = input(Colorate.Horizontal(Colors.rainbow, 'Email: '))
    user = input(Colorate.Horizontal(Colors.rainbow, 'Username: '))
    password = getpass.getpass(Colorate.Horizontal(Colors.rainbow, '(Invisible) Password: '))

    with open('passwords.txt', 'a') as f:
        f.write(f"{platform} | {phone} | {email} | {user} | " + fernet.encrypt(password.encode()).decode() + "\n")

def delete():
  with open('passwords.txt', 'r') as f:
    count = 0
    for line in f.readlines():
      data = line.rstrip()
      platform, phone, email, user, password = data.split(" | ")
      count += 1
      print(f"{Fore.LIGHTWHITE_EX}{count} Platform: {platform} | Phone: {phone} | Email: {email} | User: {user} | Password: {fernet.decrypt(password.encode()).decode()}")

  with open('passwords.txt', 'r', encoding='UTF-8') as file:
    lines = [line for line in file.readlines()]
  line_to_delete = int(input("Enter 000 to exit! What line in passwords.txt do you want me to delete? "))
  del lines[line_to_delete -1]
  with open('passwords.txt', 'w', encoding='UTF-8') as file:
    file.writelines(lines)

def generate():
  os.system('cls')
  length = int(input(Colorate.Horizontal(Colors.rainbow, 'Enter the length of password: ')))
  lower = string.ascii_lowercase
  upper = string.ascii_uppercase
  num = string.digits
  symbols = string.punctuation
  all = lower + upper + num + symbols
  temp = random.sample(all,length)
  password = "".join(temp)
  with open('generated.txt', 'w') as f:
    f.write(f"Your new password: {password}")
  input(Colorate.Horizontal(Colors.rainbow, f"""Your new password is "{password}"! I have put your
generated password in generated.txt!
  
Press enter to restart!"""))

while True:
    os.system('cls')
    choice = input(Colorate.Horizontal(Colors.rainbow, f"""
███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝

    [01] | View Password        [02] | Add Passwords    
    
    [03] | Delete Passwords     [04] | Generate Password

                          [0] Exit

                        Choice | """))
    if choice == "0":
        print(Fore.WHITE)
        break
    elif choice == "1" or choice == "01":
        os.system('cls')
        view()
    elif choice == "2" or choice == "02":
        os.system('cls')
        add()
    elif choice == "3" or choice == "03":
        os.system('cls')
        delete()
    elif choice == "4" or choice == "04":
        generate()
    else:
        print(f"{Fore.RED}Invalid decision!{Fore.WHITE}")
        continue