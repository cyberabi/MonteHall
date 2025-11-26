import random
if __name__ == '__main__':
    trials = 1000000  # Monte Carlo (a million trials) meets Monty Hall
    for switch in (False, True):
        wins = 0
        for trial in range(trials):
            winning_door = random.randint(0, 2)  # The prize could be anywhere
            first_choice = random.randint(0, 2)  # Pick a door. Any door.
            revealable_goats = list({0, 1, 2} - {winning_door, first_choice})
            goat = random.choice(revealable_goats)  # Monty shows a goat you didn't pick
            other_door = ({0, 1, 2} - {first_choice, goat}).pop()
            second_choice = first_choice if not switch else other_door  # Will you switch, or not?
            wins = wins + 1 if second_choice == winning_door else wins
        win_percent = round((float(wins) / trials) * 100, 3)
        print(f'Switch doors: {"Yes" if switch else "No "} Wins: {wins} Losses: {trials-wins} Win Rate: {win_percent}%')