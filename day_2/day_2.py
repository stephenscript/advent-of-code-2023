import re
from collections import defaultdict
import data

test_input = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

def get_game_dict(input):
  # Split the input into individual games
  games = input.strip().split('\n')

  # Process each game
  games_dict = {}

  for game in games:
      # Extract game number and details
      match = re.match(r'Game (\d+): (.+)', game)
      game_number, game_details = match.groups()

      # Split the details into individual rounds
      rounds = game_details.split(';')

      # Process each round and create a dictionary entry
      game_dict = {int(game_number): []}

      for round_entry in rounds:
          round_entry = round_entry.strip()
          round_dict = {color.strip(): int(count.strip()) for count, color in re.findall(r'(\d+) (\w+)', round_entry)}
          game_dict[int(game_number)].append(round_dict)

      # Update the result dictionary
      games_dict.update(game_dict)
  return games_dict

def get_id_sum(games_dict):

  valid_ids_sum = 0

  # Check every game
  for game_id, games in games_dict.items():
    is_possible = True

    for game in games:
      valid_count = 0
      # Check each game is valid
      for color, count in [('red', 12), ('green', 13), ('blue', 14)]:
        if (color in game and game[color] <= count):
          valid_count += 1
        
      if valid_count != len(game.items()):
        is_possible = False
    
    if is_possible:
      valid_ids_sum += game_id

  return valid_ids_sum

def get_power(games_dict):
  power = 0

  # Check every game
  for game_id, games in games_dict.items():
    red = 1
    green = 1
    blue = 1

    for game in games:
      if ('red' in game):
        red = max(game['red'], red)
      if ('green' in game):
        green = max(game['green'], green)
      if ('blue' in game):
        blue = max(game['blue'], blue)
    
    power += red * green * blue

  return power
            
print(get_id_sum(get_game_dict(test_input))) #8
print(get_id_sum(get_game_dict(data.input))) 

print(get_power(get_game_dict(test_input)))
print(get_power(get_game_dict(data.input)))