
import socket
import time
import datetime
import os
import pandas as pd 

def send_ping_request(host="1.1.1.1", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,port))
    except OSError as error:
        return False
    else:
        s.close()
        return True

ping_freq = 2

while True:
    if send_ping_request():
            time.sleep(ping_freq)

    else:
        down_time = datetime.datetime.now()
        print('Down Time', down_time.strftime("%Y-%m-%d %H:%M:%S"))

        while not send_ping_request():
            time.sleep(1)

        up_time = datetime.datetime.now()

        df_result = pd.DataFrame.from_dict({
                'down_time': [down_time.strftime("%Y-%m-%d %H:%M:%S")],
                'up_time': [up_time.strftime("%Y-%m-%d %H:%M:%S")],
                'duration': [round((up_time-down_time).total_seconds(),0)]
            })

        hdr = False  if os.path.isfile('internet_down_time.csv') else True
        df_result.to_csv('internet_down_time.csv', mode='a', header=hdr, index=False)

        print('Up Time', up_time.strftime("%Y-%m-%d %H:%M:%S"))


    