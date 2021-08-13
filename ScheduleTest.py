from statsapi import schedule,lookup_player,lookup_team

#schedule: (date=None, start_date=None, end_date=None, team="", opponent="", sportId=1, game_id=None) -> list

TeamName = 120

#print (schedule(game_id=632949))
print (schedule(team=TeamName))

#print(statsapi.lookup_player("Jose Ramirez"))