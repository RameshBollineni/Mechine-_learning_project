from flask import Flask
import sys
from housing.logger import logging
from housing.expection import HousingException
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging module")
    return "Hello world"

if __name__ == "__main__":
    app.run()
