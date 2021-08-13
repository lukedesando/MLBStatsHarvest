import statsapi

def Get_Player_ID(PlayerName):
    "Because I'm Lazy"
    PlayerJson = statsapi.lookup_player(PlayerName)
    PlayerID = PlayerJson[0]['id']
    return PlayerID