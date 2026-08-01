import PyLidar3
import time # Time module
import torch
import bhaptics_python
import asyncio
import numpy as np

HZ = 5
MAX_D = 1000 # mm AKA m

#Serial port to which lidar connected, Get it from device manager windows
#In linux type in terminal -- ls /dev/tty* 
#port = input("Enter port name which lidar is connected:") #windows
def main_loop():
    #port = "/dev/ttyUSB0" #linux
    port = "COM3"
    Obj = PyLidar3.YdLidarX4(port) #PyLidar3.your_version_of_lidar(port,chunk_size) 
    if(Obj.Connect()):
        print(Obj.GetDeviceInfo())
        gen = Obj.StartScanning()
        t = time.time() # start time 
        while (time.time() - t) < 300: #scan for 30 seconds
            raw_data = next(gen)
            data = list(raw_data.values())[90:273] # This is so we get a clean 176, nicely divisible by 8
            n_dist = len(data) // 7
            vest_data = [data[i*n_dist] for i in range(7+1)]
            asyncio.run(play_on_vest(vest_data))
            time.sleep(1 // HZ) # 10 hz
        Obj.StopScanning()
        Obj.Disconnect()
    else:
        print("Error connecting to device")

async def init_vest_api():
    app_id = "6a6d2b878ff8aa3fd8764770"
    api_key = "DUkpVNUApnpvfISOjc5y"
    app_name = ""

    result = await bhaptics_python.registry_and_initialize(app_id, api_key, app_name)
    print(f"Initialization result: {result}")

    device_info = await bhaptics_python.get_device_info_json()
    print(f"Connected device info: {device_info}")

async def play_on_vest(data):
    np_data = (100 - (np.clip(data, 0, MAX_D) / 10).astype(int)) .tolist()
    print(np_data)
    def get_vals(f,b):
        return [*f, *([0]*16), *b, *([0] * 16)]
    #values = [50] * 4 + [0] * 16 + [50] * 4 + [0] * 16  # Activate first 16 of 32 motors
    f = np_data[2:6]; b = [np_data[-1], np_data[-2], np_data[0], np_data[1]]
    print(data, "\n", f, b)
    vals = get_vals(f, b)
    await bhaptics_python.play_dot(0, int(1000 // HZ), vals)
    await asyncio.sleep(int(1 // HZ))

if __name__ == "__main__":
    #asyncio.run(init_vest_api())
    #main_loop()
    asyncio.run(play_on_vest(np.arange(994, 1004)))