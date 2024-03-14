from minigame_collection.minigames.Minigame import Minigame


class BdayGreetings(Minigame):
    name = 'Birthday Greetings'

    def run(self):
        greeting = 'Hallo'
        name = input('Wie heißt Du?: ')
        print(greeting + ' ' + name)

        age = int(input('Wie alt bist Du?: '))
        double = age * 2

        if age >= 22:
            print('Oha')

        print('Du siehst aus wie ' + str(double))
        for bday in range(age):
            print('Gratuliere nachträglich zum ' + str(bday + 1) + '. Geburtstag')
