from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_price', methods=['GET','POST'])
def predict_price():
    total_sqft = request.form['total_sqft']
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bath, bhk)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print("Starting Python Flask Server for House Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)