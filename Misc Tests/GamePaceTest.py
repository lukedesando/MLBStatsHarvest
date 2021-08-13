from statsapi import game_pace,game_pace_data,game_highlights,game_highlight_data,game_scoring_plays,game_scoring_play_data
gameid=632949

pace = game_pace(2011)
#print(pace)

pacedata=game_pace_data(2011)
#print(pacedata)

ghlts = game_highlights(632949)
#print (ghlts)

gsp=game_scoring_plays(gameid)
#print(gsp)