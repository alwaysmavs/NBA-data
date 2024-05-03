from nba_api.stats.static import players
# import json

def main(inputs: dict, context):
  name = inputs["name"]
  data = players.find_players_by_full_name(name)
  player_id = data[0]["id"]
  context.output(player_id, "player_id", True)