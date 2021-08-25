from pandas.core.frame import DataFrame
from pandas.io.parsers import read_csv
from pybaseball.statcast_pitcher import statcast_pitcher_active_spin
from statsapi import player_stats,player_stat_data,lookup_player
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

#I have a feeling I'll be referencing this a lot
StatcastBatterStatsCSV = "Statcast Batter Stats.csv"
PlayerName = 'Michael Brantley'

BatterID = Get_Player_ID(PlayerName)
#print(PlayerID)

#print (player_stats(PlayerID,type="career"))

BatterCSV = statcast_batter(SeasonStartString,TodayString,BatterID)
#ToPrint = statcast_batter(todayString,todayString,PlayerID)

pitcherID = Get_Player_ID("Patrick Sandoval")
#pitcherID = 663776
BatterCSV.to_csv(StatcastBatterStatsCSV,index=False)
#print(BatterCSV)
colnames = ['pitcher']
PitcherList = read_csv(StatcastBatterStatsCSV,usecols=colnames)
#print(PitcherList)
print(player_stat_data(pitcherID,group='pitching'))