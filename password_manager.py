from cryptography.fernet import Fernet

'''def generate_key():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)'''

def load_key():
  file = open("key.key", "rb")
  key = file.read()
  file.close()
  return key

print("Welcome to Password Manager.")

master_pwd = input("Enter your master password: ")
#generate_key()
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def add():
  name = input ("Enter your account name\n")
  pwd = input("Enter your password\n")
  with open("passwords.txt", "a") as f:
    f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
  with open("passwords.txt", "r") as f:
    for line in f:
      data = line.rstrip()
      user , passw = data.split("|")
      print("User: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())

while True:
  mode = input("Would you like to add a new account information (add), view your existing accounts (view) or (q) to quit \n").lower()

  if mode == "q":
    print("By")
    break

  elif mode == "add":
    add()

  elif mode == "view":
    view()

  else :
    print("Invalid mode. Please try again.")