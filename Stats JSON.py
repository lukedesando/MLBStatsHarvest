from __init__ import Get_Player_ID
from statsapi import player_stats,player_stat_data,lookup_player


pitcherID = Get_Player_ID("Patrick Sandoval")
print(player_stat_data(pitcherID,group='pitching'))

batterID = Get_Player_ID("Juan Soto")
print(player_stat_data(batterID,group='batting'))