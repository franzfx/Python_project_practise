import random

attempts = 7

def display_rules():
    print("Witaj w...")
    print("Great Guessing Game!\n")
    print("Zasady są proste: komputer wylosuje liczbę od 1 do 100 a twoim zadaniem będzie odgadnięcie jej w maksymalnie 7 próbach.\n")
    input("Wszystko jasne? Jeżeli tak, wpisz START aby rozpocząć. Powodzenia! ")

def play_game(number, attempt=1):
    if attempt > attempts:
        print("Koniec gry!\n")
        print("Poprawna odpowiedź to:", number)
        return

    guess = input(f"\nPróba {attempt}/7 - Jaka to liczba? ")

    try:
        guess = int(guess)
    except ValueError:
        print("Proszę wpisać liczbę.\n")
        return play_game(number, attempt)

    if guess < 1 or guess > 100:
        print("Proszę wpisać liczbę od 1 do 100.\n")
        return play_game(number, attempt)

    if guess == number:
        print("\nGratulacje! Udało ci się!")
        print("Udało ci się zgadnąć w", attempt, "próbach.")
        return
    
    if guess > number:
        print("Za duża. Wpisz niższą liczbę.\n")
    else:
        print("Za mała. Wpisz wyższą liczbę.\n")

    play_game(number, attempt + 1)

# Start the game

display_rules()

random_number = random.randint(1, 100)

play_game(random_number)