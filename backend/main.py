from utils import *
from flask import Flask, request
  
app = Flask(__name__) 

@app.route('/place_order',methods=["POST"]) 
def place_order():
    try:
        process_obj = request.get_json()
        print(process_obj["name"])
        return 'Sucess'
    except Exception as e:
        return e


@app.route('/get_order_status',methods=["POST"]) 
def get_order_status(): 
    print("order status")

if __name__ == '__main__': 
    app.run(port=5000) 