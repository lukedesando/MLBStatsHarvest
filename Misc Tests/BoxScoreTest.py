from statsapi import boxscore, boxscore_data,linescore
gameid=632949

bxsc = boxscore(gameid)
#print(bxsc)

bxscd = boxscore_data(gameid)
#print(bxscd)

print(linescore(gameid))