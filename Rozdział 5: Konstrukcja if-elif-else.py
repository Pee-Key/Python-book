# Konstrukcje if
# 
# Konstrukcja wygląda następująco:
# 
# if test_warunkowy:
#    dowolna_akcja		
# else:
#    dowolna_akcja_2
# 

cars = ['audi','bmw','subaru','toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

print('\n')

# Sprawdzanie nierówności
requested_topping = 'pieczarki'

if requested_topping != 'anchois':
	print("Proszę anchois!")

print('\n')

# Porównania liczbowe
answer = 17

if answer != 42:
	print("To nie jest prawidłowa odpowiedź. Spróbuj ponownie")

print('\n')

# if-else
age = 12

if age < 4:
	print("Cena biletu to 0zł")
elif age <18:
	print("Cena biletu to 25zł")
else:
	print("Cena biletu to 40zł")
# Analogicznie
if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40
print(f"Cena biletu wynosi {price}zł.")

print('\n')

# Sprawdzanie wielu warónków
requested_topping = ['pieczarki','podwójny ser']

if 'pieczarki' in requested_topping:
	print('Dodaję pieczarki')
if 'peperoni' in requested_topping:
	print('Dodaję peperoni')
if 'podwójny ser' in requested_topping:
	print('Dodaję podwójny ser')
print("\nTwoja pizza jest już gotowa)")

print('\n')

toppings = ['pieczarki','boczek','podwójny ser']

for topping in toppings:
	if topping in toppings:
		print("Przepraszamy, ale obecnie nie mamy boczku.")
	else:
		print(f"Dodaję {topping}.")
	print("\nTwoja pizza jest już gotowa!")
	
print('\n')

