from distutils import dir_util
from sensor.constant.training_pipeline import SCHEMA_FILE_PATH
from sensor.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from sensor.entity.config_entity import DataValidationConfig
from sensor.exception import SensorException
from sensor.logger import logging
from scipy.stats import ks_2samp
import pandas as pd
import os,sys

class DataValidation:

    def __init__(self, data_validation_artifact:DataValidationArtifact,
        data_validation_config:DataValidationConfig):
        
    try:
        pass
    except Exception as e:
        raise SensorException(e,sys)

    def validate_number_of_columns(self)->bool:
        pass

    def is_numerical_column_exist(self)->bool:
        pass

    @staticmethod
    def read_date(file_path)-> pd.DataFrame:
        pass


    def detect_dataset_drift(self):
        pass
    
    def initiate_data_validation(self)-> DataValidationArtifact:
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)