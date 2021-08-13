from statsapi import lookup_team


teamNamesList = ['NYY', 'BOS','tampa','toronto','baltimore', "WAS", 'atl','phi','nym','mia','Kansas', 'white sox','twins','indians','tigers',"cubs",'reds','cardinals','brewers','pirates','rockies','giants','dodgers','padres','arizona','astros','athletics','mariners','angels','rangers']
for name in teamNamesList:
    TeamJson = lookup_team(name)
    IDKey = TeamJson[0]['id']
    TeamName = TeamJson[0]['name']
    print(IDKey,TeamName)