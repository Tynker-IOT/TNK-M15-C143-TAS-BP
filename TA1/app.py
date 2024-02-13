from flask import Flask, render_template, request, jsonify, redirect
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

app = Flask(__name__)

thresholds = {
            'temperatureMin': 15,
            'temperatureMax': 20,
            'humidityMin': 0,
            'humidityMax': 30,
            'luminanceMin': 0,
            'luminanceMax': 10,
            'gforceMin': 0,
            'gforceMax': 1
        }

inRangeImages=["static/icecream.png",
         "static/testtubenormal.png",
         "static/bread.png"]
outsideRangeImages = ["static/icecreammelt.gif",
                      "static/testtubelight.gif",
                      "static/breadfungus.gif"]


sensorData = {}

# Create mqtt_broket_ip and store broker address in it


# Define callback function on_message() with three arguments client, userdata and msg for handling incoming MQTT messages

    # Access sensorData as global

    # Get topic from the msg

    # Decode the payload

    # Store payload as value at topic key in sensorData


    # Print sensorData


# Create an MQTT client instance

# Set the callback function for incoming messages

# Connect to the MQTT broker

# Subscribe to the desired MQTT topics


# Start the MQTT loop to listen for incoming messages



@app.route('/')
def index():
    global thresholds
    return render_template('index.html', thresholds=thresholds)

@app.route("/getSensorData", methods=['POST'])
def getSensorData():
    return jsonify(sensorData)

    
if __name__ == '__main__':
    app.run(debug=True)
