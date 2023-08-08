"""
Author:     Prayash Dash, IIT BHU, Varanasi.
Email:      prayashdash2003@gmail.com
Year:       2023
Name:       Cricket Simulator
Github:     https://github.com/prayashdash1729/advanced-cricket-tournament-simulation
"""

from models import Player, Match, Team, Field, Commentator, Umpire

if __name__ == '__main__':
    # Start by initialising teams
    india = Team("India")
    aus = Team("Australia")

    # Add players to your team. You have to add 11 players to your team.
    # Each player has the following properties:
    # name, bowling, batting, fielding, running, experience

    india.add_player("Virat Kohli", 5, 10, 8, 9, 10)
    india.add_player("Rohit Sharma", 6, 9, 7, 8, 10)
    india.add_player("Shikhar Dhawan", 2, 9, 7, 8, 9)
    india.add_player("KL Rahul", 2, 8, 7, 8, 8)
    india.add_player("Rishabh Pant", 0, 8, 7, 8, 8)
    india.add_player("Hardik Pandya", 7, 8, 7, 8, 8)
    india.add_player("Ravindra Jadeja", 8, 8, 10, 10, 8)
    india.add_player("Bhuvneshwar Kumar", 8, 6, 7, 8, 8)
    india.add_player("Jasprit Bumrah", 9, 6, 7, 8, 8)
    india.add_player("Mohammed Shami", 9, 6, 7, 8, 8)
    india.add_player("Yuzvendra Chahal", 9, 6, 7, 8, 8)

    aus.add_player("Aaron Finch", 5, 8, 8, 9, 8)
    aus.add_player("David Warner", 2, 9, 7, 8, 10)
    aus.add_player("Steve Smith", 7, 10, 8, 8, 9)
    aus.add_player("Marnus Labuschagne", 6, 9, 7, 8, 7)
    aus.add_player("Glenn Maxwell", 6, 8, 7, 8, 8)
    aus.add_player("Marcus Stoinis", 7, 8, 7, 8, 7)
    aus.add_player("Alex Carey", 0, 7, 8, 8, 7)
    aus.add_player("Pat Cummins", 9, 6, 7, 8, 8)
    aus.add_player("Mitchell Starc", 9, 7, 7, 8, 9)
    aus.add_player("Josh Hazlewood", 9, 5, 7, 8, 9)
    aus.add_player("Adam Zampa", 9, 6, 7, 8, 8)

    # Choose your captains
    india.choose_captain("Virat Kohli")
    aus.choose_captain("Aaron Finch")

    # Start the match
    match = Match(india, aus)
    match.start_match()
