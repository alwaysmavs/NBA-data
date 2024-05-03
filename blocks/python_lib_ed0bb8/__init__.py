import pandas as pd
from nba_api.stats.endpoints import playercareerstats

def main(inputs: dict, context):
  id = inputs["player_id"]
  address = inputs["address"] + "/output.csv"
  career = playercareerstats.PlayerCareerStats(player_id=id)
  data = career.get_data_frames()[0]
  df = pd.DataFrame(data)
  print(address)
  df.to_csv(address, index=False)
  context.output(id, "career", True)