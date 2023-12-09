import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(script_dir, "input")

# max cube counts
R = 12
G = 13
B = 14

def is_game_possible(r, g, b):
    return r <= R and g <= G and b <= B

def add_cubes_by_color(round):
    cube_counts = [0, 0, 0]
    parts = round.strip().split(", ")

    for part in parts:
        num = int(re.findall("\d+", part)[0])
        color = part.split(" ")[1]

        if color == "red":
            cube_counts[0] += num
        elif color == "green":
            cube_counts[1] += num
        elif color == "blue":
            cube_counts[2] += num
        
    return tuple(cube_counts)

if __name__ == "__main__":
    with open(input) as f:
        games = f.readlines()
        total_id_sum = 0
        
        for game in games:
            possible = True
            parts = game.split(":")
            id = int(parts[0].split(" ")[1])
            rounds = parts[1].split(";")

            all_rounds_possible = True
            for round in rounds:
                r, g, b = add_cubes_by_color(round)
                if not is_game_possible(r, g, b):
                    all_rounds_possible = False
                    break

            if all_rounds_possible:
                total_id_sum += id
                
    print(f"Total ID sum: {total_id_sum}")