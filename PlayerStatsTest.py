from statsapi import player_stats,player_stat_data,lookup_player
from __init__ import Get_Player_ID

PlayerName = 'Trea Turner'


#PlayerJson = lookup_player(PlayerName)
#PlayerID = PlayerJson[0]['id']
PlayerID = Get_Player_ID(PlayerName)

print (PlayerID)
#print (player_stats(PlayerID,type="career"))