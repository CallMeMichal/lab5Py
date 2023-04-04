f = open("students.txt")
zawartosc =f.read()
print(zawartosc)


#slownik jest to mapa z javy
users={}
print(users)
#       klucz i wartosc
users={"joe": "joe@gmail.com",
       "lukasz": "email@gmail.com",
       "test": "test@gmail.com",
       "admin": "admin@gmail.com"
       }
print(users)

user1 = {"name": "lukasz", "email": "email@gmail.com"}
user2 = {"name": "joe", "email": "joe@gmail.com"}
user3 = {"name": "tesr", "email": "test@email"}
user4 = {"name": "admin", "email": "admin@email.com"}

users.get("email")
print(users["lukasz"])

#dodawanie do klucza wartosci

users["alice"] = "alice@gmail.com"

for e in users:
    print(e)#jednoznaczne z users.keys

#wypisze wszystkie klucze i wartosci
print(users.items())


for key,value in users.items():
    print("key is "+ str(key) +" values"+ str(value))


#usuwanie całej klucz wartosc
if "password" in user1:
    del user1["password"]

#sortowanie metodą sorted , domyslnie jest po kluczu