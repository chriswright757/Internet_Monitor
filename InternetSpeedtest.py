import speedtest
import datetime
import csv
import time
import pandas as pd



while True:
    time_now = datetime.datetime.now() 
    try:        
        if time_now.minute in [0,15,30,45] and time_now.second == 0:
            s = speedtest.Speedtest()
            downspeed = round((round(s.download()) / 1048576), 2)
            upspeed = round((round(s.upload()) / 1048576), 2)
            df_result = pd.DataFrame.from_dict({
                'time': [time_now.strftime("%Y-%m-%d %H:%M:%S")],
                'downspeed': [downspeed],
                'upspeed': [upspeed]
            })
            df_result.to_csv('speedtest_results.csv', mode='a', header=False, index=False)

            # 60 seconds sleep
            time.sleep(60)
            print('time ', time_now, ' downspeed ', downspeed, ' upspeed ', upspeed)

    except:
        print('Internet Disconnected')
        time.sleep(60)

        