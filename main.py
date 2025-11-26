# Monte Carlo (a million trials) meets Monty Hall
import random

if __name__ == '__main__':
    trials = 1000000
    for switch in (False, True):
        wins = 0
        for trial in range(trials):
            # The prize could be anywhere
            winning_door = random.randint(0, 2)
            # Pick a door. Any door.
            first_choice = random.randint(0, 2)
            # Monty Hall always reveals a goat you didn't pick
            goats = list({0, 1, 2} - {winning_door, first_choice})
            goat = goats[random.randint(0, len(goats)-1)]
            # Will you switch, or not?
            other_door = ({0, 1, 2} - {first_choice, goat}).pop()
            second_choice = first_choice if not switch else other_door
            if second_choice == winning_door:
                wins += 1
        win_percent = round((float(wins) / trials) * 100, 3)
        print(f'Switch doors: {"Yes" if switch else "No "} Wins: {wins} Losses: {losses} Win Rate: {win_percent}%')
