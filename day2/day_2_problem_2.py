import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(script_dir, "input")

if __name__ == "__main__":
     with open(input) as f:
        games = f.readlines()
        total_sum_of_powers = 0
        
        for game in games:
            parts = game.split(":")
            rounds = parts[1].split(";")
            round_max_values = {'red': 0, 'green': 0, 'blue': 0}
            
            for round in rounds:
                parts = round.strip().split(", ")

                for part in parts:
                    num = int(re.findall("\d+", part)[0])
                    color = part.split(" ")[1] 
                    
                    if color in round_max_values:
                        round_max_values[color] = max(round_max_values[color], num)
                    

            power_of_game = round_max_values['red'] * round_max_values['green'] * round_max_values['blue']
            total_sum_of_powers += power_of_game
                
            print(f"\nGame: {game.strip()}")
            print(f"Round Max Values: {round_max_values}")
            print(f"Power of Game: {power_of_game}")
            print(f"Total Sum of Powers: {total_sum_of_powers}")