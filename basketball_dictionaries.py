class Player:
    players_on_team = []
    #challenge 1
    def __init__(self, player_dic):
        for key in player_dic:
            setattr(self, key, player_dic[key])
        Player.players_on_team.append(self)
    #ninja bonus
    @classmethod
    def get_team(cls, team_list):
        new_team = []
        for i in team_list:
            player = Player(i)
            new_team.append(player)
        return new_team
players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]


#challenge 2
# player_kevin = Player(players[0])
# player_jason = Player(players[1])
# player_kyrie = Player(players[2])
#challenge 3
player_objs = []
for i in range(len(players)):
    player_objs.append(None)
    player_objs[i] = Player(players[i])
print(player_objs) # testing challenge 3

# testing ninja bonus
players2 = Player.get_team(players)
print(players2)
