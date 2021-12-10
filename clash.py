#summoner name > summoner id > clash data > clash team id > clash team details > summoner id to summoner name > op.gg
import requests
print('Enter a summoner name:')
summoner_name = input()
print('fetching results, please wait :}')


RIOT_API_KEY= "RGAPI-4e2d8617-d3d1-491b-9c11-08c31675df9d"
summoner_response = requests.get(F"https://oc1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={RIOT_API_KEY}")
summoner_id = summoner_response.json()['id']


clash_team_id_response = requests.get(F"https://oc1.api.riotgames.com/lol/clash/v1/players/by-summoner/{summoner_id}?api_key={RIOT_API_KEY}")
clash_team_id = clash_team_id_response.json()[0]['teamId']


clash_team_info_response = requests.get(F"https://oc1.api.riotgames.com/lol/clash/v1/teams/{clash_team_id}?api_key={RIOT_API_KEY}")


players = []
for summoner in clash_team_info_response.json()['players']:
    summoner_id_clash = summoner['summonerId']
    summoner_name_clash = requests.get(F"https://oc1.api.riotgames.com/lol/summoner/v4/summoners/{summoner_id_clash}?api_key={RIOT_API_KEY}")
    player_data = {"name":summoner_name_clash.json()['name'],"position":summoner['position']}
    players.append(player_data)

#player is , player is x, player is x, player is x, player is x
for player in players:
    name = player['name']
    position = player['position']
    print(F"{name} is {position}")

opgg_URL = "https://oce.op.gg/multi/query="

for player in players:
    player_formated = player['name'].replace(" ", "%20")
    opgg_URL += player_formated + "%2C"

# print(players)




