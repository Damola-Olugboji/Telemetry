import sys
import os.path
save_path = '/media/pi/CIRCUITPY'
filename = "sensor_info"
import time

complete = os.path.join(save_path, filename +".bin")
file1 = open(complete, 'wb')

while True:
    try:
        file1.write(b"strong")
        time.sleep(0.5)
    except KeyboardInterrupt:
        file1.close()
        break
