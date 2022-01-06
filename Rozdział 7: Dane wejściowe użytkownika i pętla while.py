# Dane wejściowe - funkcja input()
message = input("Enter your message and I`ll show it on the screen: ")
print(message)

print("\n")

promt = "Powiedz kim jesteś, a my spersonalizujemy wyświetlany komunikat."
promt += "\nJak masz na imię? "

name = input(promt)
print(f"\nWitaj, {name}!")

print("\n")

# Wykorzystanie fukcji int() do akceptowania liczbowych danych wejściowych
numb = int(input("Ile masz lat?"))
print(f"O, masz {numb} lat!")

print("\n")

# Operator modulo (%)
number = int(input("Podaj liczbę, a my sprawddzimy czy jest parzysta czy nie. Liczba: "))

if number % 2 == 0:
	print(f"Liczba {number} jest parzysta!")
else:
	print(f"Liczba {number} jest nieparzysta!")

print("\n")

# Wprowadzenie do pętli while
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

print("\n")

# Umożliwienie urzytkownikowi decyzji o zakończeniu programu
# Do zakończenia pętli można także użyć polecenia break lub flagi (przy użyciu bool-zmiennej)
prompt = "Powiedz coś, a to się wyświetli: "
prompt += "\nNapisz 'koniec', aby zakończyć działanie programu. "
print(prompt)

message = ""
while message != 'koniec':
	message = input()

	if message != 'koniec':
		print(message)

print("\n")

# Użycie polecenia continue
curr_numb = 0
while curr_numb < 10:
	curr_numb += 1
	if curr_numb % 2 == 0:
		continue

	print(curr_numb)

print("\n")
