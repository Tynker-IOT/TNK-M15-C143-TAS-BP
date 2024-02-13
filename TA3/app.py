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

# Create images array with three empty images


sensorData = {}

mqtt_broker_ip = "broker.emqx.io"  

def on_message(client, userdata, msg):
    # Access global images
    global sensorData
    topic = msg.topic
    payload = msg.payload.decode('utf-8')
    sensorData[topic] = payload
    # Set images key with an array of images to be displayed on the truck
    # Check if topic is "/Temperature"
    
        # Check if temperature is less the threshold max
    
            # Set images[0] to inRangeImages[0]
    
        # Else
    
            # Set images[0] to outsideRangeImages[0]
    
    
    
    # Repeat the same for /Lux and /Humidity
    
    











    # Set store images at images key in sensorData
    
    
    print("mqtt : ", msg.payload.decode('utf-8') )

mqtt_client = mqtt.Client()
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

@app.route('/setThresholds', methods=['POST'])
def set_thresholds():
    global thresholds
    if request.method == 'POST':
        temperatureMin = request.form.get('temperatureMin')
        temperatureMax = request.form.get('temperatureMax')

        humidityMin = request.form.get('humidityMin')
        humidityMax = request.form.get('humidityMax')

        luminanceMin = request.form.get('luminanceMin')
        luminanceMax = request.form.get('luminanceMax')

        gforceMin = request.form.get('gforceMin')
        gforceMax = request.form.get('gforceMax')

        thresholds = {
            'temperatureMin': temperatureMin,
            'temperatureMax': temperatureMax,
            'humidityMin': humidityMin,
            'humidityMax': humidityMax,
            'luminanceMin': luminanceMin,
            'luminanceMax': luminanceMax,
            'gforceMin': gforceMin,
            'gforceMax': gforceMax
        }

        return redirect("/")
        
if __name__ == '__main__':
    app.run(debug=True)
