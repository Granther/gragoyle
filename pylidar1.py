import PyLidar3
import time # Time module
import torch

#Serial port to which lidar connected, Get it from device manager windows
#In linux type in terminal -- ls /dev/tty* 
#port = input("Enter port name which lidar is connected:") #windows
port = "/dev/ttyUSB0" #linux
Obj = PyLidar3.YdLidarX4(port) #PyLidar3.your_version_of_lidar(port,chunk_size) 
if(Obj.Connect()):
    print(Obj.GetDeviceInfo())
    gen = Obj.StartScanning()
    t = time.time() # start time 
    while (time.time() - t) < 30: #scan for 30 seconds
        raw_data = next(gen)
        data = list(raw_data.values())[90:273] # This is so we get a clean 176, nicely divisible by 8
        n_dist = len(data) // 7
        for i in range(7+1):
            i*=n_dist
            print(f"i: {i} | {data[i]}")
        time.sleep(0.05) # 20 times per sec
    Obj.StopScanning()
    Obj.Disconnect()
else:
    print("Error connecting to device")

