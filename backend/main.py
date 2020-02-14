from utils import *
from flask import Flask, request
from flask_cors import CORS, cross_origin
  
app = Flask(__name__) 
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/place_order',methods=["POST"]) 
@cross_origin()
def place_order():
    try:
        process_obj = request.get_json()
        res = add_new_order(process_obj) 
        if res:
            return res
        else:
            return "Failed"
    except Exception as e:
        return e

@app.route('/user_info',methods=["POST"]) 
@cross_origin()
def user_info():
    try:
        process_obj = dict(request.get_json())

        if update_user_info(process_obj):
            return "Sucess"
        else:
            return "Failed"
    except Exception as e:
        return e


@app.route('/get_order_status',methods=["POST"]) 
@cross_origin()
def get_order_status(): 
    status = dict(request.get_json())
    status = order_status(status["orderId"])
    return status

if __name__ == '__main__': 
    app.run(port=5000) 