from minigames.BdayGreetings import BdayGreetings
from minigames.FizzBuzz import FizzBuzz
from minigames.MoonTravel import MoonTravel

if __name__ == '__main__':
    bday_greetings = BdayGreetings()
    fizz_buzz = FizzBuzz()
    moon_travel = MoonTravel()

    print('Spiele zur Auswahl:')
    print(f'a) {bday_greetings.get_name()}')
    print(f'b) {fizz_buzz.get_name()}')
    print(f'c) {moon_travel.get_name()}')

    choice = input('Deine Wahl: ')
    if choice == 'a':
        bday_greetings.run()
    elif choice == 'b':
        fizz_buzz.run()
    elif choice == 'c':
        moon_travel.run()
    else:
        print('no possible')
