import pymongo 
import logging 
logging.basicConfig(filename="03_logging.log",level=logging.DEBUG, format='%(asctime)s %(message)s')

try:
    logging.info("connecting with the cluster")
    client = pymongo.MongoClient("mongodb+srv://sarvagras977:saru@cluster0.udp1myf.mongodb.net/")
    db=client['sarv']
    logging.info("creating data table")
    data =[
            {"name" : "aashi",
            "class": "ds masters",
            "time" : "flexible"},

            {"name" : "Indu",
            "class": "ds masters",
            "time" : "flexible"},

            {"name" : "sarvagra",
            "class": "B.tech",
            "time" : "flexible"},

            {"name" : "krish",
            "class": "B.sc",
            "time" : "fixed"}
         ]
    logging.info("Inserting data")
    coll_sarv=db["Register2"]
    coll_sarv.insert_many(data)

except Exception as e :
    logging.info("ERROR:{E}".format(E=e))

else :
    logging.info("Entered data successfully")

logging.info("now updating data")

try:
    logging.info("Previous value:")
    for i in coll_sarv.find():
        logging.info(i)
    coll_sarv.update_many({"time":"flexible"},{"$set" : {"time":"self-paced"}})
    logging.info("new value:")
    for i in coll_sarv.find():
        logging.info(i)            

except Exception as e :
    logging.info("ERROR:{E}".format(E=e))

else :
    logging.info("no error")
 

