from minigame_collection.minigames.Minigame import Minigame


class FizzBuzz(Minigame):
    name = 'FizzBuzz'

    def run(self):
        num = int(input('Gib ne ganze Zahl: '))
        result = ''
        if num % 3 == 0:
            result = 'Fizz'
        if num % 5 == 0:
            result += 'Buzz'
        print(result)
