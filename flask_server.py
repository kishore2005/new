from flask import Flask, request, jsonify, send_from_directory
import webbrowser
import threading

app = Flask(__name__)

# Global variable to store coordinates
coordinates = {}

@app.route('/location', methods=['POST'])
def location():
    global coordinates
    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']
    coordinates = {'latitude': latitude, 'longitude': longitude}
    print(f"Received Latitude: {latitude}, Longitude: {longitude}")
    return jsonify(status="success", latitude=latitude, longitude=longitude)

@app.route('/get_coordinates', methods=['GET'])
def get_coordinates():
    global coordinates
    return jsonify(coordinates)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()
    app.run(debug=True)
