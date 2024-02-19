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

mqtt_broker_ip = "broker.emqx.io"  

def on_message(client, userdata, msg):
    global sensorData
    topic = msg.topic
    payload = msg.payload.decode('utf-8')
    sensorData[topic] = payload

    print(sensorData)
    print("mqtt : ", msg.payload.decode('utf-8') )

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
mqtt_client.on_message = on_message
mqtt_client.connect(mqtt_broker_ip, 1883, 60)
mqtt_client.subscribe("/Temperature")
mqtt_client.subscribe("/Humidity")
mqtt_client.subscribe("/Lux")
mqtt_client.subscribe("/Gforce")
mqtt_client.loop_start()


@app.route('/')
def index():
    global thresholds
    return render_template('index.html', thresholds=thresholds)

@app.route("/getSensorData", methods=['POST'])
def getSensorData():
    return jsonify(sensorData)

# Create /setThresholds post route

# Define set_thresholds() function

    # Access global thresholds

    # Check the request method to be post

        # Get temperatureMin, temperatureMax, humidityMin, humidityMax, luminanceMin, luminanceMax, gforceMin, gforceMax from the post request and save in respective variables



        # Store every value in threshold dictionary


        # Redirect to "/"

        
if __name__ == '__main__':
    app.run(debug=True)
