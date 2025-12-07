import json
import time
import paho.mqtt.client as mqtt

student_name = "ELKANA VILVIN EASTER"
unique_id = "42611034"
topic = "home/elkanae-2025/sensor"

broker = "192.168.1.15"   
port = 1883

mqtt_username = "mqttuser"
mqtt_password = "mqttpassword123"  

def main():
    client = mqtt.Client()
    client.username_pw_set(mqtt_username, mqtt_password)
    client.connect(broker, port, 60)
    client.loop_start()

    while True:
        temperature = 25
        humidity = 60
        light = 320

        payload = {
            "student_name": student_name,
            "unique_id": unique_id,
            "temperature": temperature,
            "humidity": humidity,
            "light": light
        }

        message = json.dumps(payload)
        print("Publishing:", message)

        client.publish(topic, message, qos=0, retain=True)
        time.sleep(5)

if __name__ == "__main__":
    main()
