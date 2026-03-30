import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        item_weight: float,
        item_mrp: float,
        item_fat_content: str,
        outlet_size: str,
        outlet_location_type: str,
        item_type: str):

        self.item_weight = item_weight

        self.item_mrp = item_mrp

        self.item_fat_content = item_fat_content

        self.outlet_size = outlet_size

        self.outlet_location_type = outlet_location_type

        self.item_type = item_type

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "item_weight": [self.item_weight],
                "item_mrp": [self.item_mrp],
                "item_fat_content": [self.item_fat_content],
                "outlet_size": [self.outlet_size],
                "outlet_location_type": [self.outlet_location_type],
                "item_type": [self.item_type],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

