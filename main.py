from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.constant import database
from sensor.exception import SensorException
from sensor.constant.env_variable import MONGODB_URL_KEY
import sys
import os
from sensor.logger import logging
from sensor.pipeline.trainpipeline import TrainPipeline


if __name__=='__main__':
    try:      
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)
   


