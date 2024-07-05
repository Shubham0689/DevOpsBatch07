import psutil
from datetime import datetime
try:
    while True:
        cpupercentage=psutil.cpu_percent()
        if cpupercentage>80:
            print("Alert! CPU usage exceed threshold:{cpupercentage}% at {datetime.now().time()}")
except KeyboardInterrupt:
    print("Loop interrupted by user")
except Exception as e:
    print(f"An error occurred: {e}")
            
