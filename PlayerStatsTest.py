from pandas.core.frame import DataFrame
from pybaseball.statcast_pitcher import statcast_pitcher_active_spin
from statsapi import player_stats,player_stat_data,lookup_player
import __init__
from __init__ import Get_Player_ID
import pandas
from datetime import date,timedelta
#import statcast_pitcher_spin
from pybaseball import statcast_pitcher, statcast_batter

# Dates
today = date.today()
TomorrowString = str(today + timedelta(days=1))
YesterdayString = str(today + timedelta(days=-1))
AboutAWeekAgoString = str(today + timedelta(days=-7))
TodayString = str(today)
SeasonStartString = '2021-04-01'

print(TodayString)

PlayerName = 'Michael Brantley'

#PlayerJson = lookup_player(PlayerName)
#PlayerID = PlayerJson[0]['id']
PlayerID = Get_Player_ID(PlayerName)

print (PlayerName)
print (PlayerID)
#print (player_stats(PlayerID,type="career"))

ToPrint = statcast_batter(SeasonStartString,TodayString,PlayerID)
#ToPrint = statcast_batter(todayString,todayString,PlayerID)

ToPrint.to_csv("Statcast Batter Stats.csv",index=False)
print(ToPrint)