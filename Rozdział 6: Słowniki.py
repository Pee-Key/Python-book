
# Słowniki

alien_0 = {'color':'zielony','points':5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"\nZdobyłeś {new_points} punktów!")

print("\n")

# Dodawanie nowej pary klucz-wartość

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print("\n")

# Rozpoczęcie pracy od pustego słownika

alien_1 = {}

alien_1['color'] = 'zielony'
alien_1['points'] = 5

print(alien_1)

print("\n")

# Modyfikowanie wartości słownika

alien_2 = {'color':'zielony'}
print(f"Obcy ma {alien_2['color']} kolor")
alien_2['color'] = 'żółty'
print(f"Obcy ma {alien_2['color']} kolor")

print("\n")

# Usuwanie pary klucz-wartość

alien_3 = {'color':'zielony', 'points': 5}
print(alien_3)

del alien_3['points']
print(alien_3)

print("\n")

# Słownik oidibnych obiektów
favourite_languages = {
	'janek':'python',
	'sara':'c',
	'edward':'ruby',
	'paweł':'python'
	}

language = favourite_languages	['sara'].title()
print(f"Ulubiony język programowania Sary to {language}.")

print("\n")

# Używanie netody get() w celu uzyskania dostępu do wartości
alien_4 = {'color':'zielony', 'speed':'wolno'}

point_value = alien_4.get('points','Brak przypisanych punktów.')
print(point_value)

print("\n")

# Iteracja przez słownik
# Iteracja przez wszystkie pary klucz-wartość
user_0 = {
	'username':'jkowalski',
	'first':'jan',
	'last':'kowalski',
}
# metoda .items()zwraca listę par klucz-wartość, dlatego w pętli for tworzymy dwie zmienne dla przechowywania tych wartości
for key, value in user_0.items():
	print(f"\nKlucz:{key}")
	print(f"Wartość:{value}")

print("\n")

favourite_languages = {
	'janek':'python',
	'sara':'c',
	'edward':'ruby',
	'paweł':'python'
	}
for name, language in favourite_languages.items():
	print(f"Ulubiony język {name.title()} to {language.title()}")

print("\n")

# Iteracja przez wszystkie klucze "metoda .keys()" słownika
# .keys() pobiera wszystkie klucze ze słownika
for name in favourite_languages.keys():
	print(name.title())

print("\n")

friends = ['paweł', 'sara']
for name in favourite_languages.keys():
	print(f"Witaj, {name.title()}.")

	if name in friends:
		language = favourite_languages[name].title()
		print(f"Witaj, {name.title()}! Widzę, że twoim ulubionym językiem programowaniajest {language}!")

print("\n")

# Iteracja przez uporządkowane klucze słownika
for name in sorted(favourite_languages.keys()):
	print(f"{name.title()}, dziękujemy za udział w ankiecie!")

print("\n")

# Iteracja przez wszystkie wartości słownika
print("W ankiecie zostały wymienione następujące języki programowania:")
for language in favourite_languages.values():
	print(f"- {language.title()}")

print("W ankiecie zostały wymienione następujące języki programowania:")
# .set() pobiera wszystkie unikalne elementyna liście
for language in set(favourite_languages.values()):
	print(f"- {language.title()}")

print("\n")

# Zagnieżdżanie
alien_5 = {'color':'zielony','points':5}
alien_6 = {'color':'żółty','points':10}
alien_7 = {'color':'czerwony','points':15}
aliens = [alien_5, alien_6, alien_7]

for alien in aliens:
	print(alien)

print("\n")

# Utworzenie pustej listy przeznaczonej do przechowania obcych
aliens = []
# Utworzenie 30 zielonych obcych
for alien_number in range(30):
	new_alien = {'color':'zielony', 'points':5, 'speed':'wolno'}
	aliens.append(new_alien)

# Wyświetlenie pierwszych 5 obcych
for alien in aliens[:5]:
	print(alien)
print("...")

# Wyświetlenie całkowitej liczby utworzonych obcych
print(f"Całkowita liczba obcych: {len(aliens)}")
