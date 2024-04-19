import sys 
import os 
from src.exception import CustomException 
from src.logger import logging 
from src.utils import load_obj
import pandas as pd

class PredictPipeline: 
    def __init__(self) -> None:
        pass

    def predict(self, features): 
        try: 
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            model_path = os.path.join("artifacts", "model.pkl")

            preprocessor = load_obj(preprocessor_path)
            model = load_obj(model_path)

            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e: 
            logging.info("Error occured in predict function in prediction_pipeline location")
            raise CustomException(e,sys)
        
class CustomData: 
        def __init__(self, assists:int, 
                     boosts:int, 
                     damageDealt:float, 
                     DBNOs:int, 
                     headshotKills:int, 
                     heals:int, 
                     killPlace:int, 
                     killPoints:int, 
                     kills:int,
                     killStreaks:int,
                     longestKill:float,
                     matchDuration:int,
                     matchType:str,
                     maxPlace:int,
                     numGroups:int,
                     rankPoints:int,
                     revives:int,
                     rideDistance:float,
                     swimDistance:float,
                     walkDistance:float,
                     weaponsAcquired:int,
                     winPoints:int): 
             self.assists = assists
             self.boosts = boosts
             self.damageDealt = damageDealt
             self.DBNOs = DBNOs
             self.headshotKills = headshotKills
             self.heals = heals
             self.killPlace = killPlace 
             self.killPoints = killPoints
             self.kills = kills
             self.killStreaks= killStreaks
             self.longestKill= longestKill
             self.matchDuration=matchDuration
             self.matchType= matchType
             self.maxPlace= maxPlace
             self.numGroups= numGroups
             self.rankPoints= rankPoints
             self.revives= revives
             self.rideDistance= rideDistance
             self.swimDistance= swimDistance
             self.walkDistance= rideDistance
             self.weaponsAcquired= weaponsAcquired
             self.winPoints= winPoints

        
        def get_data_as_dataframe(self): 
             try: 
                  custom_data_input_dict = {
                       'assists': [self.assists], 
                       'boosts': [self.boosts], 
                       'damageDealt': [self.damageDealt], 
                       'DBNOs': [self.DBNOs],
                       'headshotKills':[self.headshotKills],
                       'heals':[self.heals], 
                       'killPlace': [self.killPlace], 
                       'killPoints': [self.killPoints], 
                       'kills': [self.kills],
                       'killStreaks': [self.killStreaks],
                       'longestKill': [self.longestKill],
                       'matchDuration': [self.matchDuration],
                       'matchType': [self.matchType],
                       'maxPlace': [self.maxPlace],
                       'numGroups': [self.numGroups],
                       'rankPoints': [self.rankPoints],
                       'revives': [self.revives],
                       'rideDistance': [self.rideDistance],
                       'swimDistance': [self.swimDistance],
                       'walkDistance': [self.walkDistance],
                       'weaponsAcquired': [self.weaponsAcquired],
                       'winPoints': [self.winPoints]


                  }
                  df = pd.DataFrame(custom_data_input_dict)
                  logging.info("Dataframe created")
                  return df
             except Exception as e:
                  logging.info("Error occured in get_data_as_dataframe function in prediction_pipeline")
                  raise CustomException(e,sys)