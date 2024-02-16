def bday_greetings():
    greeting = "Grüße"
    name = input("Gib Name: ")
    print(greeting + " " + name)

    age = int(input(": "))
    double = age * 2

    if age >= 22:
        print("damn")

    print("u look like " + str(double))
    for bday in range(age):
        print("Gratuliere nachträglich zum " + str(bday + 1) + ". Geburtstag")


def fizz_buzz(digit: int) -> str:
    result = 0
    if digit % 3 == 0:
        result = "Fizz"
    if digit % 5 == 0:
        result += "Buzz"
    return result


def get_moon_travel_duration(speed: int) -> str:
    dist = 384400
    duration_h = dist / speed
    years = int(duration_h / 8760)
    months = int(duration_h % 8760 / 720)
    days = int((duration_h % 8760) % 720 / 24)
    hours = int(((duration_h % 8760) % 720) % 24)
    return f"Du brauchst: {years} Jahre, {months} Monate, {days} Tage und {hours} Stunden bis zum Mond. Gute Reise!"


if __name__ == '__main__':
    print("Spiele zur Auswahl:")
    print("a) Geburtstags Greetings")
    print("b) FizzBuzz")
    print("c) Moon Travel Calculator")
    choice = input("Deine Wahl: ")
    if choice == "a":
        bday_greetings()
    elif choice == "b":
        num = int(input("Gib ne ganze Zahl: "))
        print(fizz_buzz(num))
    elif choice == "c":
        num = int(input("Deine Geschwindigkeit in Km/h: "))
        print(get_moon_travel_duration(num))
    else:
        print("no possible")
