import requests
import json
import time
import PyLidar3
import time # Time module
import asyncio
import numpy as np

HZ = 5
MAX_D = 1000 # mm AKA m
N_SECS = 300

SERVER_IP = "10.10.1.40" 
URL = f"http://{SERVER_IP}:5000/data"

#Serial port to which lidar connected, Get it from device manager windows
#In linux type in terminal -- ls /dev/tty* 
#port = input("Enter port name which lidar is connected:") #windows
def main_loop():
    # port = "/dev/ttyUSB0" #linux
    port = "COM3"
    Obj = PyLidar3.YdLidarX4(port) #PyLidar3.your_version_of_lidar(port,chunk_size) 
    if(Obj.Connect()):
        print(Obj.GetDeviceInfo())
        gen = Obj.StartScanning()
        t = time.time() # start time 
        while (time.time() - t) < N_SECS: #scan for 30 seconds
            raw_data = next(gen)
            data = list(raw_data.values())[90:273] # This is so we get a clean 176, nicely divisible by 8
            n_dist = len(data) // 7
            vest_data = [data[i*n_dist] for i in range(7+1)]
            #asyncio.run(play_on_vest(vest_data))
            send_payload(vest_data)
            time.sleep(1 // HZ) # 10 hz
        Obj.StopScanning()
        Obj.Disconnect()
    else:
        print("Error connecting to device")

def send_payload(p):
    payload = {
        "vest_data": p
    }

    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(URL, data=json.dumps(payload), headers=headers)
    except requests.exceptions.RequestException as error:
        print(f"Connection failed: {error}")

if __name__ == "__main__":
    main_loop()