import requests

def register():
    username = input("Username: ")
    password = input("Password: ")
    register = requests.post(f"http://localhost:1337/api/register/{username}/{password}").text
    print(register)

def login():
    username = input("Username: ")
    password = input("Password: ")
    login = requests.post(f"http://localhost:1337/api/login/{username}/{password}").text
    print(login)

print("What would you like to do?")
print("1. Register")
print("2. Login")
selection = input("Selection: ")

match selection:
    case "1":
        register()
    case "2":
        login()
    case _:
        print("Invalid selection.")