import paho.mqtt.client as mqtt
import mysql.connector

def on_connect(client, userdata, rc):
    print("Connect with result code " + str(rc))
    client.subscribe("image")

def on_message(client, userdata, msg):
    #hostname = "172.23.134.94"
    hostname = "localhost"
    #hostname = "127.0.0.1"
    conn = mysql.connector.connect(user="root", password="admin123", host= hostname, database="WildlifeDB", port=3306)
    cursor = conn.cursor()
    cursor.execute("select Otherfeatures from WildLifeData order by id  desc LIMIT 1")
    for row in cursor.fetchall():
        imageName = row

    imgNameSubStr = str(imageName)[3:-3]

    print(imgNameSubStr);

    f = open('/home/pi/WildlifeResearchApp/static/images/' + imgNameSubStr, 'w')
    f.write(msg.payload)
    f.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("172.27.246.86")
client.loop_forever()
