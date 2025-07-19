import functions

houses = [1, 1, 3, 2, 1, 0, 2]
search_for = 3
found = functions.house_position(houses, search_for)
print("La primera casa con", search_for, "pisos, está en la posición", found)
