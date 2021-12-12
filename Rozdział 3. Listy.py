# Listy
bicycles = ['trekingowy','górski','miejski','szosowy',]
print(bicycles)

# Uzyskanie dostępu do poszczególnych elementów listy
print(bicycles[0])

# Na elementach listy można wykorzystywać metody z ciągów
print(bicycles[0].upper ())

# Numeracja indeksu 
# Pierwszy element ma indeks 0, a nie 1
print(bicycles[1])
# Nr indeksu '-1' poda ostatni element
print(bicycles[-1])
# Analogicznie '-2' itd to drugi itd element od końca
print(bicycles[-2])

# Użycie elementu liczby w ciągu
message = f"Moim pierwszym rowerem był rower {bicycles[1].title()}."
print(message)

print('\n')

# Zmienianie elementów listy
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
# Dodawanie elementów listy
	#Dodawanie na końcu listy *list.append(name)*
motorcycles.append('ktm')
print(motorcycles)

print('\n')

	# Dodawanie do pustej listy
cars = []
cars.append('bmw')
cars.append('mercedes')
cars.append('audi')
print(cars)
	# Wstawianie na listę *list.insert(position, name)*
cars.insert(0, 'skoda')
print(cars)

print('\n')

# Usuwanie elementów listy
	# Jak wybrać del czy pop()
	# Jeżeli jest potrzeba usunięcia elementu, a nie będzie on więcej używany stosuje się del
	# Jeżeli jest potrzeba usunięcia elementu, a będzie on używany stosuje się pop()
	
	# Usuwanie poleceniem *del list[element]*
	# Po usunięciu nie mamy dostępu do elementu 
cameras = ['canon','sony','nikon']
del cameras[0]
print(cameras)
	# Usuwanie poleceniem *list.pop()*
	# Po usunięciu mamy dostęp do elementu 
cameras = ['canon','sony','nikon']
print(cameras)
popped_camera = cameras.pop()
print(cameras)
print(popped_camera)
	# Przykład użycia w spisku chronologii kupionych kamer
cameras = ['canon','sony','nikon']
last_owned = cameras.pop()
print(f"Ostatnio zakupiona kamera to {last_owned.title()}.") 
	# Usunięcie z dowolnego miejsca na liście z użyciem *list.pop()*
cameras = ['canon','sony','nikon']
first_owned = cameras.pop(0)
print(f"Moja pierwsza kamera to {first_owned.title()}")

print('\n')

# Usuwanie elementu na podstawie wartości metodaą *list.remove('value')*
	# Metoda .remove() powoduje usunięcie tylko pierwszego wystąpienia podanej wartości. 
	# Jeżeli jest kilka wystąpień danej wartości, będzie potrzebne użycie pętli.
phones = ['iphone','samsung','huawei','xiaomi','htc']
print(phones)
my_previous_phone = 'xiaomi'
phones.remove('htc')
phones.remove(my_previous_phone)
print(phones)
print(f"Mój poprzedni telefon był firmy {my_previous_phone.title()}.")

print('\n')

# Organizacja listy
	# Trwałe sortowanie listy z metodą *list.sort()*
notebooks = ['asus','acer','lenovo','aorus']
notebooks.sort()
print(notebooks)
	# Lista także może być trwale posortowana odwrotnie, dlatego funkcji sort() trzeba przekazać argument *reverse=True*
notebooks.sort(reverse=True)
print(notebooks)
print('\n')
	# Tymczasowe sortowanie listy za pomocą funkcji *sorted(list)*
notebooks = ['asus','acer','lenovo','aorus']
print("Oto lista początkowa:")
print(notebooks)
print("\nOto lista posortowana:")
print(sorted(notebooks))
# Funkcja *sorted()* także przyjmuje argument reversed=True dla wyświetlenia w odwrotnej kolejności
print("\nOto lista posortowana oswrotnie:")
print(sorted(notebooks, reverse=True))
print("\nOto ponownie lista początkowa:")
print(notebooks)
print('\n')
	# Wyświetlenie w kolejności odwrotnej
	# Metoda nie sortuje w odwrotnej kolejności chronologicznej, a TRWALE odwraca kolejność listy
lenses = ['sigma','tamron','karlzeis']
print(lenses)
lenses.reverse()
print(lenses)
print('\n')

	# Określenie wielkości listy *(len(list))*
lenses.reverse()
print(len(lenses))

print('\n')