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
