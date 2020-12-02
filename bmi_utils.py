import json
import pandas as pd 

class BMIUtils:
    def __init__(self):
        with open('table.json') as f:                   #reading the table 1 json data
            data_table = json.load(f)
        self.table = pd.json_normalize(data_table)      #converting table 1 data to dataframe

    def calculate_bmi(self,mass,height):
        bmi = round(float(mass / (height/100)**2),2)    #calculating bmi using formula 1
        return bmi

    def calculate_range(self,bmi):
        table = self.table
        try:
            record = table.iloc[(table['Bmi']-bmi).abs().argsort()[:1]] #finding bmi withing a specific range
            data = {
                "Category":record["Category"].iat[0],       #finding category record for bmi range using table 1
                "HealthRisk" :record["HealthRisk"].iat[0]   #finding health risk record for bmi range using table 1
            }
        except Exception as e:
            data = {
                "Category": "No data",       
                "HealthRisk" : "No Data"   
            }
        return data
                    
        


