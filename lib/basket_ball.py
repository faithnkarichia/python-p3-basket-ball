def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }


game=game_dict()

def num_points_per_game(player_name):
   
    
    for team in game.values():
        for player in team["players"]:
            if(player["name"]==player_name):
                return player["points_per_game"]
            
    return "Player not found"
print(num_points_per_game("Rui Hachimura"))
print("should return 11.3 points")


def player_age(player_name):
    for team in game.values():
        for player in team["players"]:
            if(player["name"]==player_name):
                return player["age"]
print(player_age("Rui Hachimura"))
print("age should be 25")


def team_colors(team_name):
    for team in game.values():
        if(team_name==team["team_name"]):
          return team["colors"]
    
print(team_colors("Washington Wizards"))


def team_names():
    names=[]
    for team in game.values():
         names.append(team["team_name"])
    return names
print(team_names())
    
def player_numbers(team_name):
    jersey_number=[]
    for team in game.values():
        for player in team["players"]:
            if(team_name==team["team_name"]):
                jersey_number.append(player["number"]) 

    return jersey_number

print(player_numbers("Washington Wizards"))


def player_stats(player_name):
    for team in game.values():
        for player in team["players"]:
            if(player_name==player["name"]):
              return player

print(player_stats("Rui Hachimura"))


def average_rebounds_by_shoe_brand(shoe_brand):
    
    rebounds=[]
    the_shoe_brand=None

    for team in game.values():
        for player in team["players"]:
            if(shoe_brand==player["shoe_brand"]):
                rebounds.append(player["rebounds_per_game"])
                the_shoe_brand=player["shoe_brand"]
                
                

    average_rebounds=sum(rebounds)/len(rebounds)
    print(f'"<{the_shoe_brand}>" : {average_rebounds:.2f}')

average_rebounds_by_shoe_brand("Adidas")


def most_career_points():
    max_points=0
    player_name=None
    for team in game.values():
        for player in team["players"]:
            if(player["career_points"]>max_points):
                max_points=player["career_points"]
                player_name=player["name"]
    print(f"{player_name} : {max_points}")
most_career_points()






def jersey_in_both_teams():
    game = game_dict()
    home_numbers = set()
    away_numbers = set()
    
    for player in game["home"]["players"]:
        home_numbers.add(player["number"])
    
    for player in game["away"]["players"]:
        away_numbers.add(player["number"])
    
    duplicates = home_numbers.intersection(away_numbers)

    if duplicates:
        # convert to sorted list and join as a string
        formatted = ", ".join(str(num) for num in sorted(duplicates))
        print(f"Jersey numbers in both teams: {formatted}")
    else:
        print("No duplicate jersey numbers found.")

jersey_in_both_teams()




def longest_name():
    longest_name_so_far = ""
    
    for team in game_dict().values():
        for player in team["players"]:
            if len(player["name"]) > len(longest_name_so_far):
                longest_name_so_far = player["name"]

    print(longest_name_so_far)

longest_name()






              

    
    







