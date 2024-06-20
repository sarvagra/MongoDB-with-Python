import pymongo
import logging
logging.basicConfig(filename="00_logging.log",level=logging.DEBUG, format='%(asctime)s %(message)s')

logging.info("connecting to your database")
try:
    client = pymongo.MongoClient("mongodb+srv://sarvagras977:saru@cluster0.udp1myf.mongodb.net/")
    db=client.test 
    logging.info(db)

except Exception as e :
    logging.info("ERROR : {E}".format(E=e))

else :
    logging.info("Connection Established Successfully")