import os 
import sys 
import pickle 
#import mysql.connector
import pandas as pd
from src.exception import CustomException
from sklearn.metrics import r2_score
from src.logger import logging
from sqlalchemy import create_engine
def save_function(file_path, obj): 
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok= True)
    with open (file_path, "wb") as file_obj: 
        pickle.dump(obj, file_obj)

def model_performance(X_train, y_train, X_test, y_test, models): 
    try: 
        report = {}
        for i in range(len(models)): 
            model = list(models.values())[i]
# Train models
            model.fit(X_train, y_train)
# Test data
            y_test_pred = model.predict(X_test)
            #R2 Score 
            test_model_score = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_model_score
        return report

    except Exception as e: 
        raise CustomException(e,sys)

# Function to load a particular object 
def load_obj(file_path):
    try: 
        with open(file_path, 'rb') as file_obj: 
            return pickle.load(file_obj)
    except Exception as e: 
        logging.info("Error in load_object fuction in utils")
        raise CustomException(e,sys)

def fetch_data_from_mysql():
    # Connect to MySQL database
    engine = create_engine(f'mysql+mysqlconnector://{"root"}:{"Debarpan130798"}@{"localhost"}/{"pubgproject"}')
    output_file:str=os.path.join('dataset','pubgdata.csv')
    query = "select * from pubgdata"
    df = pd.read_sql(query, engine)
    print(df)
    engine.dispose()
    os.makedirs(os.path.dirname(output_file),exist_ok=True)
    df.to_csv(output_file, index=False)

    #fetch_data_from_mysql()