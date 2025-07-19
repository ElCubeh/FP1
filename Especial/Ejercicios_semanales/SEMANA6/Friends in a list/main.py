import functions

friends = ['Michael', 'George', 'Martin', 'Peter', 'Mathew', 'John', 'Paul']
person = input("Dame un nombre: ")
if functions.is_friend(friends, person):
    print("Sí")
else:
    print("No")
