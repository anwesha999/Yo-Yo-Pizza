from flask import Flask 
  
app = Flask(__name__) 

@app.route('/place_order',method="POST") 
def place_order(): 
    print("Placeing order")
    # return 'Hello World'

@app.route('/get_order_status',method="POST") 
def get_order_status(): 
    print("order status")

if __name__ == '__main__': 
    app.run() 