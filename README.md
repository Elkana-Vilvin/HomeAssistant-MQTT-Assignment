# Home Assistant MQTT Assignment

## Student Details
Name:Elkana Vilvin Easter  
Register Number: 42611034  

---

## Project Overview
This project sends sensor values from a Python script to Home Assistant using MQTT.  
Home Assistant receives the values through the Mosquitto MQTT broker and shows them on the dashboard.

---

## Technologies Used
- Home Assistant OS (in VirtualBox)
- Mosquitto MQTT Broker (Add-on)
- Python (paho-mqtt library)
- MQTT JSON Messages

---

## MQTT Topic Used



---

## Python Script
The script sends 3 sensor values every 5 seconds:
- Temperature (25)
- Humidity (60)
- Light (320)

It also includes:
- Name
- Register number
- MQTT topic

---

## Configuration.yaml (Home Assistant)
MQTT sensors are added in configuration.yaml to read JSON values sent from Python.

---

## Output
The Home Assistant dashboard shows:
- Elkana Temperature (°C)
- Elkana Humidity (%)
- Elkana Light (lx)

All values update in real-time.

---

## Files Included
- Python script: `elkana_mqtt.py`
- PDF Report
- Screenshots

---

## Conclusion
MQTT communication between Python and Home Assistant works correctly.  
Values update in real-time on the dashboard.
