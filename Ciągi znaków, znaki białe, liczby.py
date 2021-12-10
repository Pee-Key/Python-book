# Zmiana wielkości liter

name = "jan koWAlski"
# name.title() - każde słowo z dużej litery i tylko pierwsza litera jest duża
print(name.title())
# name.upper() - Capslock
print(name.upper())
# name.lower() - wszystkie litery małe
print(name.lower())
# Zmienne w ciągach tekstowych

first_name = "jan"
last_name = "kowalski"
# "f" musi być umieszczone przed ciągiem, żeby wartości w 
# klamrach były interpretowane jako wartości zmiennych a nie ich nazwy
full_name = f"{first_name} {last_name}"
print(f"Witaj, {full_name.title()}!")
# analog
# welcome_message = f"Witaj, {full_name.title()}!"
# print(welcome_message)

# Znaki białe
 
# \t - tabulacja 
# \n - nowa linia
print("Języki:\n\tPython,\n\tC,\n\tJava.")

# Usuwanie białych znaków 

#Usuwanie tymczasowe
# zmienna.rstrip() - usuwa znaki białe po prawej stronie od ciągu
language_py = 'python '
print(language_py.rstrip())
# zmienna.lstrip() - usuwa znaki białe po lewej stronie od ciągu
language_cpp = 'C++ '
print(language_cpp.lstrip())

# Apostrofy 

# Prawidłowa interpretacja apostrofu
apostrophe_message_1 = "What`s your name?"
print(apostrophe_message_1)

# Nieprawidłowa interpretacja apostrofu
# apostrophe_message_2 = 'What's your name?'
# print(apostrophe_message_2)

# Liczby

# Całkowita +,-,* całkowita = całkowita
# całkowita / całkowita = zmiennoprzecinkowa
# '**' - potęga liczby
# całkowita + zmiennoprzecinkowa = zmiennoprzecinkowa

# Znaki podkreślenia
# Python ignoruje znaki podkreślenia "_"
universe_age = 14_000_000_000
print(universe_age)

# Wiele przypisań  
x, y, z = 1, 2, 3
print(x,y,z)

#Stała zmienna 
# Dużymi literami są oznaczane zmienne stałe
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)