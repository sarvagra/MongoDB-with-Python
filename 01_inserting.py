import os
import pymongo 
import logging 
logging.basicConfig(filename="01_logging.log",level=logging.DEBUG, format='%(asctime)s %(message)s')

try:
    logging.info("connecting with the cluster")
    client = pymongo.MongoClient(os.getenv('pw'))
    db=client['sarv']
    logging.info("creating data table")
    data =  {"name" : "sarvagra",
        "class": "ds masters",
        "time" : "flexible"
        }
    logging.info("Inserting data")
    coll_sarv=db["my_record"]
    coll_sarv.insert_one(data)

except Exception as e :
    logging.info("ERROR:{E}".format(E=e))

else :
    logging.info("Entered data successfully")


