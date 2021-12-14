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
