import random

class Player:
    def __init__(self, name, bowling, batting, fielding, running, experience):
        self.name = name
        self.bowling = bowling
        self.batting = batting
        self.fielding = fielding
        self.running = running
        self.experience = experience

    def __str__(self):
        return f"{self.name} {self.bowling} {self.batting} {self.fielding} {self.running} {self.experience}"


class Team(Player):
    def __init__(self, name):
        self.name = name
        self.players = []
        self.captain = None

    def add_player(self, name, bowling, batting, fielding, running, experience):
        if len(self.players) >= 15:
            print(f"Team {self.name} has 15 players already.")
            return
        elif len(self.players) >= 11:
            print(f"Team {self.name} has {len(self.players)} players now. You can only add up to 15 players in a team")

        player = Player(name, bowling, batting, fielding, running, experience)
        self.players.append(player)

    def choose_captain(self, name):
        for player in self.players:
            if player.name == name:
                self.captain = player
                print(f"{player.name} is now the captain of {self.name}")
                return

        print(f"No player named {name} in {self.name}")

    def get_captain(self):
        return self.captain

    def get_players(self):
        return self.players

    def __str__(self):
        return f"{self.name} {[player.name for player in self.players]}"


class Field(Team):
    def __init__(self, team1, team2):
        self.field_size = {'length': 0., 'breadth': 0.}
        self.fan_ratio = {team1.name: 0, team2.name: 0}
        self.pitch_condition = None
        self.x_bowling = None
        self.x_batting = None
        self.team1 = team1
        self.team2 = team2
        self.home_team = None
        self.away_team = None

    def set_field(self):
        dim1 = random.randint(600, 800) / 10  # in mtrs
        dim2 = random.randint(600, 800) / 10
        self.field_size['length'] = max(dim1, dim2)
        self.field_size['breadth'] = min(dim1, dim2)
        self.pitch_condition = random.choice(['dry', 'wet', 'damp'])
        if self.pitch_condition == 'dry':
            self.x_bowling = random.randint(30, 60) / 100
            self.x_batting = random.randint(60, 90) / 100
        elif self.pitch_condition == 'wet':
            self.x_bowling = random.randint(70, 90) / 100
            self.x_batting = random.randint(90, 50) / 100
        else:
            self.x_bowling = random.randint(60, 90) / 100
            self.x_batting = random.randint(20, 40) / 100

        self.home_team = random.choice([self.team1, self.team2])
        self.away_team = self.team1 if self.home_team == self.team2 else self.team2
        fan_ratio_home = random.randint(20, 80)
        self.fan_ratio[self.home_team.name] = max(fan_ratio_home, 100 - fan_ratio_home)
        self.fan_ratio[self.away_team.name] = 100 - fan_ratio_home[self.home_team]

        print(f"Field is set with following properties:\n")
        print(f"Length: {self.field_size['length']}m\nBreadth: {self.field_size['breadth']}m\n")
        print(f"Home team: {self.home_team.name}\n")
        print(f"Fan ratio: {self.home_team.name} {self.fan_ratio[self.home_team.name]} and {self.away_team.name}{self.fan_ratio[self.team2.name]}")

    def get_field(self):
        return self.field_size, self.home_team, self.away_team, self.fan_ratio



# Umpire: This class will be responsible for chunking probabilities of all the players on the field and
# predicting the outcome of a ball. The Umpire class will also keep track of scores, wickets, and overs.
# It can also make decisions on LBWs, catches, no-balls, wide-balls, etc.


class Umpire(Team, Player, Field):
    def __init__(self):



class Match(Umpire, Team, Player, Field):
    def __init__(self):



class Commentator(Match):
    def __init__(self):







