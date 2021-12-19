# Praca z listą

# Iteracja przez całą listę z użyciem petli for
magicians = ['david','alice','caroline']
for magician in magicians:
	print(f"{magician.title()}, to była doskonała sztuczka!")
	print(f"Nie mogę się doczekać twojej kolejnej sztuczki, {magician.title()}.\n")
print("Dziękuję wszystkim. Tobył naprawdę wspaniały występ!\n\n\n")

# Użycie funkcji *range()*
# range(1,5) = from =1 to <5
for value in range(1,5):
	print(value)

print("\n")

# Użycie funkcji *range()* do utworzenia listy liczb
numbers = list(range(1,6))
print(numbers)

print("\n")

# Użycie funkcji *range()*
# range(2,11,2) = from =2 to <11 by step 2
even_numbers = list(range(2,11,2))
print(even_numbers)

print("\n")

squares = []
for number in  range(1,11):
	square = number
	number ** 2
	squares.append(square)
print(squares)

print("\n")

# Proste dane statstyczne
# min() - minimum
# max() - maximum
# sum() - suma liczb
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits),"\n",max(digits),"\n",sum(digits))

print("\n")

# Lista składana (list comprehension)
numb_squares = [value1**2 for value1 in range(1,11)]
print(numb_squares)

print("\n")

# Wycinek lsty
players = ['karol','martyna','michał','florian','ela']
print(players[1:3])
print(players[-2:])

print('\n')

# Iteracja przez wycinek
print("Oto trzech pierwszysch graczy naszej drużyny:")
for player in players[:3]:
	print(player.title())

print('\n')

# Kopiowanie listy
my_food = ['pizza','falafel','cake']
# friend_food = my_food wskazuje, że f_f jest równa m_f, więc każda zmiana m_f = zmianie f_f
friend_food = my_food[:]
my_food.append('icecream')
friend_food.append('pasta')
print("Moje ulubione potrawy to:")
print(my_food)
print("\nUlubione potrawy mojego przyjaciela to:")
print(friend_food)


print('\n')

# Krotka
# Krotka jest bardzo podobna do listy, ale używa nawias okrągły i po jej zdefiniowaniu dostęp do elementów
# dostajemy przez ich indeks

dimensions = (200,50)
# dimensions[0] = 250 - błąd 
print(dimensions[0])
print(dimensions[1])

print('\n')


# Jednowymiarowa krotka
# trzeba pamiętać, żeby po elemencie wstawić przecinek
my_t = (3,)
print(my_t)

print('\n')

# Nadpisanie krotki
dims = (200,50)
print("Wymiary początkowe:")
for dim in dims:
	print(dim)
dims = (400,100)
print("\nWymiary po modyfikacji:")
for dim in dims:
	print(dim)
