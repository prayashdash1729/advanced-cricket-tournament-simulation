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
        self.x_bowling = 0
        self.x_batting = 0
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
            self.x_batting = random.randint(50, 90) / 100
        else:
            self.x_bowling = random.randint(60, 90) / 100
            self.x_batting = random.randint(20, 40) / 100

        self.home_team = random.choice([self.team1, self.team2])
        self.away_team = self.team1 if self.home_team == self.team2 else self.team2
        fan_ratio_home = random.randint(20, 80)
        self.fan_ratio[self.home_team.name] = max(fan_ratio_home, 100 - fan_ratio_home)
        self.fan_ratio[self.away_team.name] = min(fan_ratio_home, 100 - fan_ratio_home)

        print(f"Field is set with following properties:\n")
        print(f"Length: {self.field_size['length']}m\nBreadth: {self.field_size['breadth']}m\n")
        print(f"Home team: {self.home_team.name}\n")
        print(f"Fan ratio: {self.home_team.name} {self.fan_ratio[self.home_team.name]} and {self.away_team.name}{self.fan_ratio[self.team2.name]}")

    def get_field(self):
        return self.field_size, self.home_team, self.away_team, self.fan_ratio


# Umpire: This class will be responsible for chunking probabilities of all the players on the field and
# predicting the outcome of a ball. The Umpire class will also keep track of scores, wickets, and overs.
# It can also make decisions on LBWs, catches, no-balls, wide-balls, etc.

class Umpire(Field):
    def __init__(self, field):
        # self.team1 = team1
        # self.team2 = team2
        self.field = field
        self.winner = None
        self.field = field
        self.max_overs = 5
        self.overs = 0.0
        self.innings = 0
        self.target = 0
        self.batting_team = None
        self.bowling_team = None
        self.scores = 0
        self.wickets = 0
        print("Umpires are ready!")

    def toss(self):
        if self.field.x_bowling >= self.field.x_batting:
            self.batting_team = self.field.home_team
            self.bowling_team = self.field.away_team
            self.innings = 1
        else:
            self.batting_team = self.field.away_team
            self.bowling_team = self.field.home_team
            self.innings = 1

        win_team = random.choice(['bat', 'bowl'])
        # if win_team == 'bat':
        #     print(f"{self.batting_team.name} won the toss and decided to bat first")
        # else:
        #     print(f"{self.bowling_team.name} won the toss and decided to bowl first")

    def predict_outcome(self):
        # Probabilities for different pitch conditions and events
        probabilities = {
            'outcomes': [0, 1, 2, 3, 4, 5, 6, 'out', 'catch', 'lbw', 'wide'],
            'wet': {
                'probability': [0.273, 0.2712, 0.069, 0.002, 0.136, 0.0, 0.110, 0.0213, 0.03905, 0.01065, 0.0678]
            },
            'damp': {
                'probability': [0.273, 0.2712, 0.069, 0.002, 0.136, 0.0, 0.110, 0.0213, 0.03905, 0.01065, 0.0678]
            },
            'dry': {
                'probability': [0.273, 0.2712, 0.069, 0.002, 0.136, 0.0, 0.110, 0.0213, 0.03905, 0.01065, 0.0678]
            }
        }
        # print(f"Pitch condition: {self.field.pitch_condition}")
        outcome = random.choices(population=probabilities['outcomes'],
                                 weights=probabilities[self.field.pitch_condition]['probability'],
                                 k=1)
        outcome = outcome[0]
        if outcome == 'out' or outcome == 'catch' or outcome == 'lbw':
            self.update_wickets()
            self.update_overs()
            print(f"{self.batting_team.name} lost a wicket")
        elif outcome == 'wide':
            self.update_score(1)
            print(f"{self.bowling_team.name} bowled a wide ball")
        else:
            self.update_score(outcome)
            self.update_overs()
            print(f"{self.batting_team.name} scored {outcome} runs")

    def update_score(self, runs):
        self.scores += runs

    def update_wickets(self):
        self.wickets += 1

    def update_overs(self):
        self.overs += 0.1  # Assuming each over has 6 balls
        if round(self.overs - self.overs//1, 1) == 0.6 and self.overs != 0 and self.overs != 5:
            self.overs = self.overs//1 + 1
            print(f"{self.overs} overs completed. Strike change for {self.batting_team.name}")


class Match(Umpire):
    def __init__(self, team1, team2):
        print("Match initiated")
        self.field = Field(team1, team2)
        self.field.set_field()
        self.umpire = Umpire(self.field)
        self.field = Field(team1, team2)
        print("Match is ready to start. Start the match by calling the start_match() function.")

    def start_match(self):
        self.umpire.toss()

        while self.umpire.wickets <= 9 and self.umpire.overs <= self.umpire.max_overs:
            self.umpire.predict_outcome()

        self.umpire.target = self.umpire.scores + 1

        print(f"First innings completed. "
              f"{self.umpire.batting_team.name} scored {self.umpire.scores} runs at a loss of {self.umpire.wickets} wickets.")

        self.umpire.innings = 2
        self.umpire.batting_team, self.umpire.bowling_team = self.umpire.bowling_team, self.umpire.batting_team
        self.umpire.overs = 0
        self.umpire.scores = 0
        self.umpire.wickets = 0

        while self.umpire.wickets <= 9 and self.umpire.overs <= self.umpire.max_overs and self.umpire.scores < self.umpire.target:
            self.umpire.predict_outcome()
            # print("test")

        if self.umpire.scores >= self.umpire.target:
            self.umpire.winner = self.umpire.batting_team
        elif self.umpire.scores == self.umpire.target - 1:
            self.umpire.winner = "Tie"
        else:
            self.umpire.winner = self.umpire.bowling_team

        print("Second innings completed")

        if self.umpire.winner == "Tie":
            print("Match tied")
        else:
            print(f"{self.umpire.winner.name} won the match")

        print("Match completed")


class Commentator:
    def __init__(self, match):
        self.match = match

    def comment(self, ball_outcome, batsman, bowler):
        # Implement logic to provide commentary based on the ball outcome and players involved
        pass






