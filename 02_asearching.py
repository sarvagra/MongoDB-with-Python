import pymongo 
import logging 
logging.basicConfig(filename="02_logging.log",level=logging.DEBUG, format='%(asctime)s %(message)s')

try:
    logging.info("connecting with the cluster")
    client = pymongo.MongoClient("mongodb+srv://sarvagras977:saru@cluster0.udp1myf.mongodb.net/")
    db=client['sarv']
    logging.info("creating data table")
    data =[
            {"name" : "aashi",
            "class": "ds masters",
            "time" : "fixed"},

            {"name" : "Indu",
            "class": "ds masters",
            "time" : "flexible"},

            {"name" : "sarvagra",
            "class": "B.tech",
            "time" : "flexible"},

            {"name" : "krish",
            "class": "B.sc",
            "time" : "flexible"}
         ]
    logging.info("Inserting data")
    coll_sarv=db["Register"]
    coll_sarv.insert_many(data)

except Exception as e :
    logging.info("ERROR:{E}".format(E=e))

else :
    logging.info("Entered data successfully")

try:
    logging.info("Searching Element")
    for i in coll_sarv.find({"name":"aashi"}):
        logging.info(i)
                 

except Exception as e :
    logging.info("ERROR:{E}".format(E=e))

else :
    logging.info("no error")
 

