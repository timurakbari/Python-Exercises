from minigames.Minigame import Minigame


class MoonTravel(Minigame):
    name = 'Moon Travel Calculator'

    def run(self):
        speed = int(input('Deine Geschwindigkeit in Km/h: '))
        dist = 384400
        duration_h = dist / speed
        years = int(duration_h / 8760)
        months = int(duration_h % 8760 / 720)
        days = int((duration_h % 8760) % 720 / 24)
        hours = int(((duration_h % 8760) % 720) % 24)
        print(f'Du brauchst: {years} Jahre, {months} Monate, {days} Tage und {hours} Stunden bis zum Mond. Gute Reise!')